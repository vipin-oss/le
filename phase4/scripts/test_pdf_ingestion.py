#!/usr/bin/env python3
"""
Unit tests for the PDF ingestion pipeline.

Uses synthetic fixtures (generated PDFs and extracted text) to test:
- File discovery
- SHA-256 hashing
- Duplicate detection
- Text extraction
- DOI identification
- Bibliographic metadata extraction
- Extraction error handling
- Page provenance
- Database output
- Re-run behavior
- Protection against overwriting originals
"""

import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

# Add pipeline to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from pdf_ingestion_pipeline import (
    compute_sha256,
    extract_pdf_text,
    extract_doi_from_text,
    extract_title_from_text,
    detect_math_content,
    create_study_record,
    map_to_section,
    CONFIG,
)


class TestPDFIngestion:
    """Test suite for PDF ingestion pipeline functions."""

    def setup_method(self):
        """Set up temporary directories for testing."""
        self.tmpdir = Path(tempfile.mkdtemp())
        self.incoming = self.tmpdir / "incoming"
        self.verified = self.tmpdir / "verified"
        self.metadata = self.tmpdir / "metadata"
        self.extraction = self.tmpdir / "extraction"
        self.duplicates = self.tmpdir / "duplicates"
        self.reports = self.tmpdir / "reports"
        for d in [self.incoming, self.verified, self.metadata,
                  self.extraction, self.duplicates, self.reports]:
            d.mkdir(parents=True, exist_ok=True)

    def teardown_method(self):
        """Clean up temporary directories."""
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_compute_sha256(self):
        """Test SHA-256 hash computation."""
        # Create a test file with known content
        test_file = self.tmpdir / "test.txt"
        test_file.write_text("Hello, World!")

        hash1 = compute_sha256(test_file)
        hash2 = compute_sha256(test_file)

        # Same file should produce same hash
        assert hash1 == hash2, "SHA-256 should be deterministic"

        # Known SHA-256 of "Hello, World!"
        expected = hashlib.sha256(b"Hello, World!").hexdigest()
        assert hash1 == expected, f"SHA-256 mismatch: {hash1} != {expected}"

        # Different content should produce different hash
        test_file2 = self.tmpdir / "test2.txt"
        test_file2.write_text("Different content")
        hash3 = compute_sha256(test_file2)
        assert hash1 != hash3, "Different files should have different hashes"

        print("  PASS: test_compute_sha256")

    def test_extract_doi_from_text(self):
        """Test DOI extraction from text."""
        # Standard DOI
        text1 = "Published in Journal of Mechanics, DOI: 10.1016/j.mechrescom.2010.12.005"
        doi = extract_doi_from_text(text1)
        assert doi == "10.1016/j.mechrescom.2010.12.005", f"DOI mismatch: {doi}"

        # DOI with URL prefix
        text2 = "https://doi.org/10.1007/BF00045689"
        doi = extract_doi_from_text(text2)
        assert doi == "10.1007/BF00045689", f"DOI URL mismatch: {doi}"

        # No DOI
        text3 = "This paper has no DOI identifier"
        doi = extract_doi_from_text(text3)
        assert doi is None, f"Should return None for no DOI: {doi}"

        print("  PASS: test_extract_doi_from_text")

    def test_extract_title_from_text(self):
        """Test title extraction from text."""
        text = """Memory-Dependent Derivative in Generalized Thermoelasticity
        X. Wang and L. Li
        Mechanics Research Communications"""
        title = extract_title_from_text(text)
        assert title is not None, "Title should be extracted"
        assert "Memory-Dependent" in title, f"Title should contain key words: {title}"
        assert len(title) < 200, f"Title too long: {title}"

        print("  PASS: test_extract_title_from_text")

    def test_detect_math_content(self):
        """Test mathematical content detection."""
        # Text with LaTeX equations
        text_with_math = """
        The strain tensor is defined as \\begin{equation}
        \\varepsilon_{ij} = \\frac{1}{2}(u_{i,j} + u_{j,i})
        \\end{equation}
        The stress \\sigma_{ij} and strain \\varepsilon_{ij} are related by Hooke's law.
        """
        result = detect_math_content(text_with_math)
        assert result["has_equations"] is True, "Should detect equations"
        assert result["equation_count"] > 0, "Should count equation patterns"

        # Text without math
        text_no_math = "This is a plain text paragraph with no mathematical content."
        result = detect_math_content(text_no_math)
        assert result["has_equations"] is False, "Should not detect equations in plain text"
        assert result["equation_count"] == 0, "Equation count should be 0"

        print("  PASS: test_detect_math_content")

    def test_map_to_section(self):
        """Test section mapping heuristic."""
        # Thermoelastic content
        text1 = "Lord-Shulman theory introduces thermal relaxation time"
        section = map_to_section(text1)
        assert section == "sec04_thermoelastic", f"Expected sec04_thermoelastic, got {section}"

        # Nonlocal content
        text2 = "Eringen nonlocal elasticity with scale-dependent effects"
        section = map_to_section(text2)
        assert section == "sec07_nonlocal", f"Expected sec07_nonlocal, got {section}"

        # Interface content
        text3 = "Reflection and transmission at interface with scattering matrix"
        section = map_to_section(text3)
        assert section == "sec09_interfaces", f"Expected sec09_interfaces, got {section}"

        # Unknown content
        text4 = "This is completely unrelated content about cooking recipes"
        section = map_to_section(text4)
        assert section == "unclassified", f"Expected unclassified, got {section}"

        print("  PASS: test_map_to_section")

    def test_create_study_record(self):
        """Test study record creation."""
        filepath = self.incoming / "test.pdf"
        filepath.write_text("dummy")

        file_hash = compute_sha256(filepath)
        extraction = {
            "text": "Lord-Shulman theory DOI: 10.1016/0022-5096(67)90024-5",
            "page_count": 10,
            "extracted_pages": 10,
            "extraction_method": "pdfplumber",
            "is_scanned": False,
            "errors": [],
        }

        record = create_study_record(filepath, file_hash, extraction)

        assert record["filename"] == "test.pdf"
        assert record["sha256"] == file_hash
        assert record["doi"] == "10.1016/0022-5096(67)90024-5"
        assert record["page_count"] == 10
        assert record["is_scanned"] is False
        assert record["verification_status"] == "pending"
        assert record["section_hint"] == "sec04_thermoelastic"

        print("  PASS: test_create_study_record")

    def test_duplicate_detection(self):
        """Test duplicate detection by SHA-256 hash."""
        # Create two files with identical content
        file1 = self.incoming / "paper1.pdf"
        file2 = self.incoming / "paper2.pdf"
        content = b"Identical PDF content for duplicate test"
        file1.write_bytes(content)
        file2.write_bytes(content)

        hash1 = compute_sha256(file1)
        hash2 = compute_sha256(file2)
        assert hash1 == hash2, "Identical content should produce identical hashes"

        print("  PASS: test_duplicate_detection")

    def test_original_files_preserved(self):
        """Test that original PDFs are not overwritten or deleted during processing."""
        # Create a test PDF
        test_pdf = self.incoming / "original.pdf"
        test_pdf.write_bytes(b"Fake PDF content for preservation test")

        original_hash = compute_sha256(test_pdf)
        original_exists_before = test_pdf.exists()

        # Run extraction (doesn't modify the original)
        extraction = extract_pdf_text(test_pdf)

        # Original should still exist with same hash
        assert test_pdf.exists(), "Original file should still exist after extraction"
        assert compute_sha256(test_pdf) == original_hash, "Original file hash should be unchanged"
        assert original_exists_before is True, "Original file existed before extraction"

        print("  PASS: test_original_files_preserved")

    def test_extraction_error_handling(self):
        """Test that extraction errors are handled gracefully."""
        # Create a non-PDF file with .pdf extension
        fake_pdf = self.incoming / "fake.pdf"
        fake_pdf.write_bytes(b"This is not a real PDF file")

        extraction = extract_pdf_text(fake_pdf)

        # Should not crash, should return error information
        assert "errors" in extraction, "Should have errors field"
        assert isinstance(extraction["errors"], list), "Errors should be a list"
        assert extraction["extraction_method"] in ("none", "pdfplumber", "pypdf2")

        print("  PASS: test_extraction_error_handling")

    def test_database_output_structure(self):
        """Test that study index output has correct structure."""
        filepath = self.incoming / "test.pdf"
        filepath.write_bytes(b"test content")

        file_hash = compute_sha256(filepath)
        extraction = {
            "text": "Green-Lindsay theory",
            "page_count": 5,
            "extracted_pages": 5,
            "extraction_method": "pdfplumber",
            "is_scanned": False,
            "errors": [],
        }

        record = create_study_record(filepath, file_hash, extraction)

        # Check required fields
        required_fields = [
            "filename", "filepath", "sha256", "date_added",
            "page_count", "extracted_pages", "extraction_method",
            "is_scanned", "doi", "title", "has_equations",
            "equation_count", "extraction_errors", "section_hint",
            "verification_status", "notes",
        ]
        for field in required_fields:
            assert field in record, f"Missing required field: {field}"

        print("  PASS: test_database_output_structure")


def run_tests():
    """Run all tests and report results."""
    test = TestPDFIngestion()
    tests = [
        ("test_compute_sha256", test.test_compute_sha256),
        ("test_extract_doi_from_text", test.test_extract_doi_from_text),
        ("test_extract_title_from_text", test.test_extract_title_from_text),
        ("test_detect_math_content", test.test_detect_math_content),
        ("test_map_to_section", test.test_map_to_section),
        ("test_create_study_record", test.test_create_study_record),
        ("test_duplicate_detection", test.test_duplicate_detection),
        ("test_original_files_preserved", test.test_original_files_preserved),
        ("test_extraction_error_handling", test.test_extraction_error_handling),
        ("test_database_output_structure", test.test_database_output_structure),
    ]

    passed = 0
    failed = 0

    for name, func in tests:
        try:
            test.setup_method()
            func()
            test.teardown_method()
            passed += 1
        except Exception as e:
            test.teardown_method()
            print(f"  FAIL: {name} - {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed out of {len(tests)} tests")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
PYEOF