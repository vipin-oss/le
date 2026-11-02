# Verified metadata for the P8 coverage extension.
# Every record below was returned by a Crossref `query.bibliographic` call on 2026-11-02;
# DOI, volume and pages are transcribed from that response, not from memory.
# verification: R0 = title/metadata only (what Crossref returns), R1 = abstract seen,
# R2 = full text read, R3 = equations checked.
# P9 (2026-11-02) upgraded Mindlin1965 to R3 from the library PDF; the other 71 remain R0.

AREA_A = [
    dict(key="Toupin1962", area="a", kind="article",
         authors=[("Toupin", "R. A.")], year="1962",
         title="Elastic materials with couple-stresses",
         journal="Archive for Rational Mechanics and Analysis", volume="11", pages="385-414",
         doi="10.1007/BF00253945", ver="R0",
         shows="Defines the linear couple-stress elastic continuum: the rotation gradient enters the "
               "strain energy, so a characteristic length appears and the short-wave branch bends "
               "downwards instead of staying linear.",
         fits="s12_size", inout="outside the heat-flux template: changes the elastic operator, not G(s)"),
    dict(key="Toupin1964", area="a", kind="article",
         authors=[("Toupin", "R. A.")], year="1964",
         title="Theories of elasticity with couple-stress",
         journal="Archive for Rational Mechanics and Analysis", volume="17", pages="85-112",
         doi="10.1007/BF00253050", ver="R0",
         shows="Sets out the several variants of couple-stress theory and their boundary conditions, "
               "the reference point for what a couple-stress problem needs besides the displacement field.",
         fits="s12_size", inout="outside the template"),
    dict(key="Mindlin1964", area="a", kind="article",
         authors=[("Mindlin", "R. D.")], year="1964",
         title="Micro-structure in linear elasticity",
         journal="Archive for Rational Mechanics and Analysis", volume="16", pages="51-78",
         doi="10.1007/BF00248490", ver="R0",
         shows="Introduces the elastic continuum with microstructure: each material point carries a "
               "micro-deformation, which yields extra kinetic and potential terms and hence extra branches.",
         fits="s12_size", inout="outside the template"),
    dict(key="Mindlin1965", area="a", kind="article",
         authors=[("Mindlin", "R. D.")], year="1965",
         title="Second gradient of strain and surface-tension in linear elasticity",
         journal="International Journal of Solids and Structures", volume="1", pages="417-438",
         doi="10.1016/0020-7683(65)90006-5", ver="R3",
         note="P9: library PDF read. Energy density W(eps, grad eps, grad grad eps) = eq. (1), p. 418; "
              "full quadratic form with lambda, mu, a1-a5, b1-b7, c1-c3 = eq. (19), p. 421; "
              "stress tau_pq = eq. (20a), p. 422; internal length defined by l^2 = a/ mu, p. 422. "
              "No thermal field anywhere in the paper: the heat kernel is neither used nor modified.",
         shows="Derives the first strain-gradient theory (second gradient of displacement) and shows "
               "that it reproduces surface tension, the paper behind the 'form A / form B' nonlocal "
               "stress laws that the review uses in s12_size.",
         fits="s12_size", inout="outside the template; supplies the elastic operator that multiplies G(s)"),
    dict(key="GreenRivlin1964", area="a", kind="article",
         authors=[("Green", "A. E."), ("Rivlin", "R. S.")], year="1964",
         title="Multipolar continuum mechanics",
         journal="Archive for Rational Mechanics and Analysis", volume="17", pages="113-147",
         doi="10.1007/BF00253051", ver="R0",
         shows="General multipolar (dipolar and higher) continuum: the kinematics carry gradients of "
               "the deformation to a chosen order, which is the formal home of every gradient enrichment.",
         fits="s12_size", inout="outside the template"),
    dict(key="FleckHutchinson1993", area="a", kind="article",
         authors=[("Fleck", "N. A."), ("Hutchinson", "J. W.")], year="1993",
         title="A phenomenological theory for strain gradient effects in plasticity",
         journal="Journal of the Mechanics and Physics of Solids", volume="41", pages="1825-1857",
         doi="10.1016/0022-5096(93)90072-N", ver="R0",
         shows="The phenomenological strain-gradient plasticity that made length scales standard in "
               "small-scale mechanics; the stiffness enhancement it predicts is the mechanical half of "
               "what a size-dependent thermoelastic model must reproduce.",
         fits="s12_size", inout="outside the template"),
    dict(key="Lam2003", area="a", kind="article",
         authors=[("Lam", "D. C. C."), ("Yang", "F."), ("Chong", "A. C. M."), ("Wang", "J."), ("Tong", "P.")],
         year="2003", title="Experiments and theory in strain gradient elasticity",
         journal="Journal of the Mechanics and Physics of Solids", volume="51", pages="1477-1508",
         doi="10.1016/S0022-5096(03)00053-X", ver="R0",
         shows="The three length-scale strain-gradient theory together with the micro-bending, "
               "micro-torsion and micro-indentation measurements used to identify the lengths.",
         fits="s12_size", inout="outside the template; gives the calibration route for the length l"),
    dict(key="Yang2002", area="a", kind="article",
         authors=[("Yang", "F."), ("Chong", "A. C. M."), ("Lam", "D. C. C."), ("Tong", "P.")], year="2002",
         title="Couple stress based strain gradient theory for elasticity",
         journal="International Journal of Solids and Structures", volume="39", pages="2731-2743",
         doi="10.1016/S0020-7683(02)00152-X", ver="R0",
         shows="Modified couple-stress theory with a symmetric couple-stress tensor: one length scale, "
               "and a much smaller set of extra constants than the full form — the version used in most "
               "recent thermoelastic damping papers.",
         fits="s12_size", inout="outside the template"),
    dict(key="Eringen1990ThermoMicrostretch", area="a", kind="article",
         authors=[("Eringen", "A. C.")], year="1990",
         title="Theory of thermo-microstretch elastic solids",
         journal="International Journal of Engineering Science", volume="28", pages="1291-1301",
         doi="10.1016/0020-7225(90)90076-U", ver="R0",
         shows="Thermoelasticity of microstretch solids: a scalar microstretch, a micro-rotation and "
               "the temperature are coupled, giving a theory in which the thermal and microstructural "
               "branches interact through the constitutive law.",
         fits="s13_multiphysics", inout="outside the template: extra balance laws, G(s) unchanged"),
    dict(key="LazarMaugin2005", area="a", kind="article",
         authors=[("Lazar", "M."), ("Maugin", "G. A.")], year="2005",
         title="Nonsingular stress and strain fields of dislocations and disclinations in first strain "
               "gradient elasticity",
         journal="International Journal of Engineering Science", volume="43", pages="1157-1184",
         doi="10.1016/j.ijengsci.2005.01.006", ver="R0",
         shows="Works out the first strain-gradient (Mindlin form) fields of defects, which removes the "
               "classical singularities — the concrete demonstration that the gradient length regularises "
               "short wavelengths.",
         fits="s12_size", inout="outside the template"),
    dict(key="GutkinAifantis1999", area="a", kind="article",
         authors=[("Gutkin", "M. Yu."), ("Aifantis", "E. C.")], year="1999",
         title="Dislocations in the theory of gradient elasticity",
         journal="Scripta Materialia", volume="40", pages="559-566",
         doi="10.1016/S1359-6462(98)00424-2", ver="R0",
         shows="Solves the dislocation problem in Aifantis' gradient elasticity and shows the "
               "screening of the classical stress singularity over the gradient length.",
         fits="s12_size", inout="outside the template"),
    dict(key="Mawassy2023", area="a", kind="article",
         authors=[("Mawassy", "N."), ("Reda", "H."), ("Hammoud", "A."), ("Yan", "D.-J."), ("Ganghoffer", "J.-F.")],
         year="2023", title="Effect of damage on Rayleigh wave propagation in second gradient lattice materials",
         journal="Wave Motion", volume="121", pages="103185",
         doi="10.1016/j.wavemoti.2023.103185", ver="R0",
         shows="Rayleigh-wave dispersion in a second-gradient lattice material with damage, i.e. a "
               "surface wave whose speed depends on an internal length — the size-effect counterpart of "
               "the review's elastic Rayleigh baseline.",
         fits="s10_surface", inout="outside the template: elastic operator only"),
    dict(key="GodaGanghoffer2026", area="a", kind="article",
         authors=[("Goda", "I."), ("Ganghoffer", "J.-F.")], year="2026",
         title="Wave dispersion analysis of pantographic compliant metamaterials via strain gradient homogenization",
         journal="Composite Structures", volume="392", pages="120589",
         doi="10.1016/j.compstruct.2026.120589", ver="R0",
         shows="Homogenises a pantographic lattice to a strain-gradient continuum and reads the "
               "dispersion branches of that continuum, the clearest recent bridge between lattice "
               "microstructure and gradient-modelled waves.",
         fits="s12_size", inout="outside the template"),
    dict(key="Borjalilou2020", area="a", kind="article",
         authors=[("Borjalilou", "V."), ("Asghari", "M.")], year="2020",
         title="Thermoelastic damping in strain gradient microplates according to a generalized theory of thermoelasticity",
         journal="Journal of Thermal Stresses", volume="43", pages="401-420",
         doi="10.1080/01495739.2020.1722771", ver="R0",
         shows="Couples a generalized (non-Fourier) heat law to strain-gradient plate elasticity and "
               "computes the thermoelastic damping of the microplate, so both the size effect and the "
               "lag appear in the same loss curve.",
         fits="s04b_flexted", inout="inside: the heat law is a template member; the elasticity is not"),
    dict(key="Alihemmati2022", area="a", kind="article",
         authors=[("Alihemmati", "J."), ("Tadi Beni", "Y.")], year="2022",
         title="Generalized thermoelasticity of microstructures: Lord-Shulman theory with modified strain "
               "gradient theory",
         journal="Mechanics of Materials", volume="172", pages="104412",
         doi="10.1016/j.mechmat.2022.104412", ver="R0",
         shows="Lord-Shulman thermoelasticity combined with modified strain-gradient elasticity, and the "
               "dispersion of the resulting microstructure waves.",
         fits="s12_size", inout="inside for the heat law (LS), outside for the elasticity"),
    dict(key="Zeng2025", area="a", kind="article",
         authors=[("Zeng", "S."), ("Aouadi", "M.")], year="2025",
         title="Temporal behavior in nonlocal strain gradient porous thermoelasticity with relaxed microtemperatures",
         journal="Journal of Thermal Stresses", volume="48", pages="512-528",
         doi="10.1080/01495739.2025.2458107", ver="R0",
         shows="Nonlocal strain-gradient porous thermoelasticity with relaxed microtemperatures; a "
               "well-posedness and decay study, i.e. the qualitative side that the review's admissibility "
               "test rarely reaches.",
         fits="s17_open", inout="outside the template in three directions at once (nonlocal, porous, microtemperatures)"),
    dict(key="HosseiniLi2022", area="a", kind="article",
         authors=[("Hosseini", "S. M."), ("Li", "F.")], year="2022",
         title="Thermal shock-induced Moore-Gibson-Thompson generalized coupled thermoelasticity analysis "
               "based on the strain gradient Love-Bishop theory in a nanorod resonator",
         journal="Meccanica", volume="57", pages="623-640",
         doi="10.1007/s11012-021-01456-7", ver="R0",
         shows="MGT heat conduction inside a strain-gradient nanorod resonator under thermal shock — a "
               "template member (MGT) with a size-dependent elastic operator.",
         fits="s12_size", inout="inside for the heat law (MGT), outside for the elasticity"),
    dict(key="Li2018CoupleStress", area="a", kind="article",
         authors=[("Li", "Y."), ("Li", "L."), ("Wei", "P."), ("Wang", "C.")], year="2018",
         title="Reflection and refraction of thermoelastic waves at an interface of two couple-stress "
               "solids based on Lord-Shulman thermoelastic theory",
         journal="Applied Mathematical Modelling", volume="55", pages="536-550",
         doi="10.1016/j.apm.2017.10.040", ver="R0",
         shows="Interface problem with both a non-Fourier heat law and couple-stress elasticity: "
               "reflection and refraction coefficients that carry the internal length as well as the lag.",
         fits="s11_interfaces", inout="inside for the heat law (LS), outside for the elasticity"),
]

AREA_B = [
    dict(key="Sigalas1992", area="b", kind="article", authors=[("Sigalas","M. M."),("Economou","E. N.")],
         year="1992", title="Elastic and acoustic wave band structure",
         journal="Journal of Sound and Vibration", volume="158", pages="377-382",
         doi="10.1016/0022-460X(92)90059-7", ver="R0",
         shows="Shows that a periodic array of elastic inclusions has band gaps for elastic waves — the "
               "opening statement of the elastic band-gap literature.",
         fits="s16c_taxonomy", inout="outside the template: periodic elastic operator, no heat law"),
    dict(key="Kushwaha1993", area="b", kind="article",
         authors=[("Kushwaha","M. S."),("Halevi","P."),("Dobrzynski","L."),("Djafari-Rouhani","B.")],
         year="1993", title="Acoustic band structure of periodic elastic composites",
         journal="Physical Review Letters", volume="71", pages="2022-2025",
         doi="10.1103/PhysRevLett.71.2022", ver="R0",
         shows="Computes the acoustic band structure of a two-component periodic elastic composite and "
               "names the phononic crystal: gaps appear for both polarisations at wavelengths set by the lattice.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Liu2000", area="b", kind="article",
         authors=[("Liu","Z."),("Zhang","X."),("Mao","Y."),("Zhu","Y. Y."),("Yang","Z."),("Chan","C. T."),("Sheng","P.")],
         year="2000", title="Locally resonant sonic materials", journal="Science", volume="289",
         pages="1734-1736", doi="10.1126/science.289.5485.1734", ver="R0",
         shows="A locally resonant gap two orders of magnitude below the Bragg condition, from coated "
               "inclusions; the mechanism behind every locally resonant metamaterial.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Khelif2010", area="b", kind="article",
         authors=[("Khelif","A."),("Mohammadi","S."),("Eftekhar","A. A."),("Adibi","A."),("Aoubiza","B.")],
         year="2010", title="Locally resonant surface acoustic wave band gaps in a two-dimensional phononic "
               "crystal of pillars on a surface",
         journal="Physical Review B", volume="81", pages="214303",
         doi="10.1103/PhysRevB.81.214303", ver="R0",
         shows="Surface (Rayleigh-type) band gaps from surface pillars, i.e. a surface-wave gap whose "
               "frequency the geometry sets.",
         fits="s10_surface", inout="outside the template: elastic surface wave"),
    dict(key="Lu2009", area="b", kind="article",
         authors=[("Lu","M.-H."),("Feng","L."),("Chen","Y.-F.")],
         year="2009", title="Phononic crystals and acoustic metamaterials",
         journal="Materials Today", volume="12", pages="34-42",
         doi="10.1016/S1369-7021(09)70315-3", ver="R0",
         shows="Short review that separates Bragg-gap phononic crystals from locally resonant acoustic "
               "metamaterials and lists the device consequences.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Hussein2014", area="b", kind="article",
         authors=[("Hussein","M. I."),("Leamy","M. J."),("Ruzzene","M.")],
         year="2014", title="Dynamics of phononic materials and structures: historical origins, recent "
               "progress, and future outlook",
         journal="Applied Mechanics Reviews", volume="66", pages="040802",
         doi="10.1115/1.4026911", ver="R0",
         shows="The standard review of phononic materials: dispersion computation, band-gap mechanisms, "
               "damping and finite-structure effects, and the terminology the review would adopt.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Christensen2015", area="b", kind="article",
         authors=[("Christensen","J."),("Kadic","M."),("Wegener","M."),("Kraft","O.")],
         year="2015", title="Vibrant times for mechanical metamaterials",
         journal="MRS Communications", volume="5", pages="453-462", doi="10.1557/mrc.2015.51", ver="R0",
         shows="Review of mechanical metamaterials, including the elastodynamic branch and the role of "
               "internal resonators.",
         fits="s16c_taxonomy", inout="outside the template",
         note="Crossref lists Wegener twice in the author list; four distinct names are used here"),
    dict(key="Ma2016", area="b", kind="article", authors=[("Ma","G."),("Sheng","P.")],
         year="2016", title="Acoustic metamaterials: from local resonances to broad horizons",
         journal="Science Advances", volume="2", pages="e1501595", doi="10.1126/sciadv.1501595", ver="R0",
         shows="Review that derives the effective mass and bulk modulus of locally resonant media and "
               "traces the mechanisms from single resonators to broadband devices.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Cummer2016", area="b", kind="article",
         authors=[("Cummer","S. A."),("Christensen","J."),("Alu","A.")],
         year="2016", title="Controlling sound with acoustic metamaterials",
         journal="Nature Reviews Materials", volume="1", pages="16001",
         doi="10.1038/natrevmats.2016.1", ver="R0",
         shows="Review of acoustic metamaterials written around effective parameters and transformation "
               "acoustics, with the limits of each design.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Vasileiadis2021", area="b", kind="article",
         authors=[("Vasileiadis","T."),("Varghese","J."),("Babacic","V."),("Gomis-Bresco","J."),
                  ("Navarro Urrios","D."),("Graczykowski","B.")],
         year="2021", title="Progress and perspectives on phononic crystals",
         journal="Journal of Applied Physics", volume="129", pages="160901",
         doi="10.1063/5.0042337", ver="R0",
         shows="Review of phononic crystals across length scales, including hypersonic and thermal-phonon "
               "regimes — the closest existing bridge from phononics to heat transport.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Cang2022", area="b", kind="article",
         authors=[("Cang","Y."),("Jin","Y."),("Djafari-Rouhani","B."),("Fytas","G.")],
         year="2022", title="Fundamentals, progress and perspectives on high-frequency phononic crystals",
         journal="Journal of Physics D: Applied Physics", volume="55", pages="193002",
         doi="10.1088/1361-6463/ac4941", ver="R0",
         shows="Review of GHz–THz phononic crystals, i.e. the band where the review's own thermal "
               "frequencies and nanostructure sizes sit.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Wang2015Topo", area="b", kind="article",
         authors=[("Wang","P."),("Lu","L."),("Bertoldi","K.")],
         year="2015", title="Topological phononic crystals with one-way elastic edge waves",
         journal="Physical Review Letters", volume="115", pages="104302",
         doi="10.1103/PhysRevLett.115.104302", ver="R0",
         shows="Designs a phononic crystal with a topological gap and a one-way edge mode, showing that "
               "band structure can be engineered beyond simple gaps.",
         fits="s17_open", inout="outside the template"),
    dict(key="Hu2014", area="b", kind="article",
         authors=[("Hu","A."),("Zhang","X."),("Wu","F."),("Yao","Y.")],
         year="2014", title="Enlargement of the locally resonant Lamb wave band gap of the phononic crystal "
               "plate at the deep sub-wavelength scale",
         journal="Materials Research Express", volume="1", pages="045801",
         doi="10.1088/2053-1591/1/4/045801", ver="R0",
         shows="Widens a locally resonant Lamb-wave gap in a plate at deep sub-wavelength scale — the "
               "plate counterpart of the review's Lamb problem in s10b_lamb.",
         fits="s13b_bg", inout="outside the template"),
    dict(key="Yao2011", area="b", kind="article",
         authors=[("Yao","Y."),("Wu","F."),("Zhang","X."),("Hou","Z.")],
         year="2011", title="Thermal tuning of Lamb wave band structure in a two-dimensional phononic "
               "crystal plate",
         journal="Journal of Applied Physics", volume="110", pages="124907",
         doi="10.1063/1.3669391", ver="R0",
         shows="Tunes a Lamb-wave band structure through temperature-dependent elastic constants — the "
               "one place where a thermal field and a phononic gap are coupled in the same model.",
         fits="s13_multiphysics", inout="outside the template, but the natural point of contact with it"),
    dict(key="VanBelle2019", area="b", kind="article",
         authors=[("Van Belle","L."),("Claeys","C."),("Deckers","E."),("Desmet","W.")],
         year="2019", title="The impact of damping on the sound transmission loss of locally resonant "
               "metamaterial plates",
         journal="Journal of Sound and Vibration", volume="461", pages="114909",
         doi="10.1016/j.jsv.2019.114909", ver="R0",
         shows="Quantifies how much damping changes the predicted gap performance of a locally resonant "
               "plate — the loss term the review's damping sections can supply physically.",
         fits="s04b_flexted", inout="outside the template: mechanical damping, not the heat law"),
    dict(key="Ha2022", area="b", kind="article", authors=[("Ha","T. D.")], year="2022",
         title="A wide band gap phononic crystal strip for quality factor improvement in a length "
               "extensional mode MEMS resonator",
         journal="Archive of Applied Mechanics", volume="92", pages="1493-1505",
         doi="10.1007/s00419-022-02125-1", ver="R0",
         shows="Uses a phononic strip as an anchor to raise the Q of a length-extensional MEMS resonator, "
               "i.e. band-gap engineering applied to the loss problem the review treats.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Li2004Diode", area="b", kind="article",
         authors=[("Li","B."),("Wang","L."),("Casati","G.")],
         year="2004", title="Thermal diode: rectification of heat flux",
         journal="Physical Review Letters", volume="93", pages="184301",
         doi="10.1103/PhysRevLett.93.184301", ver="R0",
         shows="Demonstrates rectification of a heat flux in an asymmetric nonlinear lattice — the "
               "thermal counterpart of a photonic or phononic diode.",
         fits="s17_open", inout="outside the template: lattice heat transport, no continuum G(s)"),
    dict(key="Li2021Thermal", area="b", kind="article",
         authors=[("Li","Y."),("Li","W."),("Han","T."),("Zheng","X."),("Li","J."),("Li","B."),("Fan","S."),("Qiu","C.-W.")],
         year="2021", title="Transforming heat transfer with thermal metamaterials and devices",
         journal="Nature Reviews Materials", volume="6", pages="488-507",
         doi="10.1038/s41578-021-00283-2", ver="R0",
         shows="Review of thermal metamaterials: transformation thermodynamics, effective conductivities "
               "and the devices (cloaks, concentrators) built from them, all in the Fourier framework.",
         fits="s16c_taxonomy", inout="outside the template: assumes Fourier conduction, so its limits are the review's subject"),
]

AREA_C = [
    dict(key="Hutson1962", area="c", kind="article",
         authors=[("Hutson","A. R."),("White","D. L.")], year="1962",
         title="Elastic wave propagation in piezoelectric semiconductors",
         journal="Journal of Applied Physics", volume="33", pages="40-47",
         doi="10.1063/1.1728525", ver="R0",
         shows="Couples the elastic, piezoelectric and carrier equations of a semiconductor (CdS) and "
               "shows that the acoustic wave is attenuated or amplified according to the drift field.",
         fits="s13_multiphysics", inout="outside the template: adds a carrier balance law to the field set"),
    dict(key="White1962", area="c", kind="article", authors=[("White","D. L.")], year="1962",
         title="Amplification of ultrasonic waves in piezoelectric semiconductors",
         journal="Journal of Applied Physics", volume="33", pages="2547-2554",
         doi="10.1063/1.1729015", ver="R0",
         shows="Gives the acoustoelectric gain condition for a drifting carrier gas and predicts net "
               "amplification — the mechanism that makes the piezo-semiconductor a lossless or active medium.",
         fits="s13_multiphysics", inout="outside the template"),
    dict(key="Palma1987", area="c", kind="article",
         authors=[("Palma","F."),("Saccani","L."),("Das","P.")], year="1987",
         title="Surface acoustic wave propagation and acoustoelectric interaction in multilayered "
               "piezoelectric semiconductors",
         journal="Superlattices and Microstructures", volume="3", pages="181-185",
         doi="10.1016/0749-6036(87)90055-3", ver="R0",
         shows="Surface-wave propagation in a layered piezo-semiconductor with acoustoelectric coupling — "
               "the layered interface problem of s11 with carriers switched on.",
         fits="s11_interfaces", inout="outside the template"),
    dict(key="Cross2006", area="c", kind="article", authors=[("Cross","L. E.")], year="2006",
         title="Flexoelectric effects: charge separation in insulating solids subjected to elastic strain gradients",
         journal="Journal of Materials Science", volume="41", pages="53-63",
         doi="10.1007/s10853-005-5916-6", ver="R0",
         shows="Explains flexoelectricity — polarisation proportional to the strain gradient — and why it "
               "survives in centrosymmetric crystals where piezoelectricity does not.",
         fits="s12_size", inout="outside the template: couples a gradient of strain, not the heat flux"),
    dict(key="Zubko2013", area="c", kind="article",
         authors=[("Zubko","P."),("Catalan","G."),("Tagantsev","A. K.")], year="2013",
         title="Flexoelectric effect in solids", journal="Annual Review of Materials Research",
         volume="43", pages="387-421", doi="10.1146/annurev-matsci-071312-121634", ver="R0",
         shows="The reference review of flexoelectricity: symmetry, magnitudes, measurement and the "
               "coupling to strain gradients and surface effects.",
         fits="s12_size", inout="outside the template"),
    dict(key="Wang2006Nano", area="c", kind="article",
         authors=[("Wang","Z. L."),("Song","J.")], year="2006",
         title="Piezoelectric nanogenerators based on zinc oxide nanowire arrays",
         journal="Science", volume="312", pages="242-246", doi="10.1126/science.1124005", ver="R0",
         shows="Converts mechanical energy with ZnO nanowire arrays through the piezopotential, the "
               "device that made ZnO the reference piezo-semiconductor.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Wang2007Nano", area="c", kind="article", authors=[("Wang","Z. L.")], year="2007",
         title="Nanopiezotronics", journal="Advanced Materials", volume="19", pages="889-892",
         doi="10.1002/adma.200602918", ver="R0",
         shows="Introduces the piezotronic transistor concept: the piezopotential in a ZnO nanowire gates "
               "carrier transport, joining elasticity, polarisation and carriers in one device.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Dai2018", area="c", kind="article",
         authors=[("Dai","X."),("Zhu","F."),("Qian","Z."),("Yang","J.")], year="2018",
         title="Electric potential and carrier distribution in a piezoelectric semiconductor nanowire in "
               "time-harmonic bending vibration",
         journal="Nano Energy", volume="43", pages="22-28", doi="10.1016/j.nanoen.2017.11.002", ver="R0",
         shows="Solves the coupled bending-vibration problem of a piezo-semiconductor nanowire and "
               "reports the carrier redistribution produced by the oscillating field.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Xiao2025", area="c", kind="article",
         authors=[("Xiao","Z."),("Liu","J."),("Zhang","C."),("Chen","W.")], year="2025",
         title="Nonlinear analysis of thermo-deformation-polarization-carrier coupling response of "
               "piezoelectric semiconductor plates",
         journal="European Journal of Mechanics - A/Solids", volume="111", pages="105560",
         doi="10.1016/j.euromechsol.2024.105560", ver="R0",
         shows="Four-field nonlinear plate theory for a piezo-semiconductor in which temperature, "
               "deformation, polarisation and carrier density are solved together — the closest published "
               "relative of the review's thermopiezoelectric section.",
         fits="s13_multiphysics", inout="partly inside: a thermal field enters, but through a Fourier-type law"),
    dict(key="Zhao2022", area="c", kind="article",
         authors=[("Zhao","L."),("Li","P."),("Jin","F.")], year="2022",
         title="Non-homogeneous cross section variation enhanced flexoelectric coupling in semiconductor "
               "beams and its application in charge carrier redistribution",
         journal="Journal of Applied Physics", volume="131", pages="084502",
         doi="10.1063/5.0078779", ver="R0",
         shows="Shows that a varying cross-section raises the flexoelectric coupling in a semiconductor "
               "beam and redistributes the carriers — flexoelectricity as a design variable.",
         fits="s12_size", inout="outside the template"),
    dict(key="Mahdy2020", area="c", kind="article",
         authors=[("Mahdy","A. M. S."),("Mohamed","M. S."),("Lotfy","Kh."),("Kadry","M."),("El-Bary","A.")],
         year="2020", title="Plasma-elastic-thermal propagation of a rotator semiconductor magneto-electric "
               "medium during microtemperature and photothermal excitation processes subjected to mechanical ramp type",
         journal="Waves in Random and Complex Media", volume="32", pages="2084-2104",
         doi="10.1080/17455030.2020.1843738", ver="R0",
         shows="Solves the plasma–elastic–thermal system of a semiconductor with microtemperature and "
               "photothermal excitation: three wave families (plasma, thermal, elastic) in one dispersion problem.",
         fits="s13_multiphysics", inout="partly inside: a lagged/generalized heat law is used"),
    dict(key="Khamis2020", area="c", kind="article",
         authors=[("Khamis","A. K."),("El-Bary","A. A."),("Lotfy","Kh."),("Bakali","A.")], year="2020",
         title="Photothermal excitation processes with refined multi dual phase-lags theory for "
               "semiconductor elastic medium",
         journal="Alexandria Engineering Journal", volume="59", pages="1-9",
         doi="10.1016/j.aej.2019.11.016", ver="R0",
         shows="Photothermal excitation of a semiconductor solved with a refined multi dual-phase-lag "
               "heat law, i.e. a DPL member of the review's template carried into the plasma problem.",
         fits="s13_multiphysics", inout="inside: the heat law is a template member"),
    dict(key="Abbas2018", area="c", kind="article",
         authors=[("Abbas","I. A."),("Aly","K. A."),("Dahshan","A.")], year="2018",
         title="Analytical solutions of plasma and thermoelastic waves photogenerated by a focused laser "
               "beam in a semiconductor material",
         journal="Silicon", volume="10", pages="2609-2616", doi="10.1007/s12633-018-9797-0", ver="R0",
         shows="Closed-form solution for the plasma and thermoelastic waves launched by a focused laser "
               "pulse in a semiconductor — the semiconductor version of the review's laser-ultrasonics example.",
         fits="s15_applications", inout="partly inside: a generalized heat law is used"),
    dict(key="Levine1984", area="c", kind="article",
         authors=[("Levine","D."),("Steinhardt","P. J.")], year="1984",
         title="Quasicrystals: a new class of ordered structures",
         journal="Physical Review Letters", volume="53", pages="2477-2480",
         doi="10.1103/PhysRevLett.53.2477", ver="R0",
         shows="Defines the quasiperiodic order of quasicrystals: long-range order without translational "
               "periodicity, which is why their elasticity needs a phason field as well as a phonon field.",
         fits="s16c_taxonomy", inout="outside the template: a second displacement-like field appears"),
    dict(key="Shechtman1984", area="c", kind="article",
         authors=[("Shechtman","D."),("Blech","I."),("Gratias","D."),("Cahn","J. W.")], year="1984",
         title="Metallic phase with long-range orientational order and no translational symmetry",
         journal="Physical Review Letters", volume="53", pages="1951-1953",
         doi="10.1103/PhysRevLett.53.1951", ver="R0",
         shows="The diffraction evidence for an icosahedral metallic phase — the experimental discovery "
               "that created the quasicrystal field.",
         fits="s16c_taxonomy", inout="outside the template"),
    dict(key="Chellappan2015", area="c", kind="article",
         authors=[("Chellappan","V."),("Gopalakrishnan","S."),("Mani","V.")], year="2015",
         title="Wave propagation of phonon and phason displacement modes in quasicrystals: determination "
               "of wave parameters",
         journal="Journal of Applied Physics", volume="117", pages="074904",
         doi="10.1063/1.4907212", ver="R0",
         shows="Extracts wave speeds for the coupled phonon–phason modes of a quasicrystal, which is what "
               "a dispersion treatment of a two-field elastic continuum looks like.",
         fits="s13_multiphysics", inout="outside the template: elastic two-field continuum"),
    dict(key="LiZhou2023", area="c", kind="article",
         authors=[("Li","Y."),("Zhou","Y.")], year="2023",
         title="Dynamic response of a piezoelectric quasicrystal rod with the generalized thermoelasticity",
         journal="Acta Mechanica", volume="235", pages="323-335", doi="10.1007/s00707-023-03747-4", ver="R0",
         shows="Combines a generalized thermoelastic heat law with a piezoelectric quasicrystal rod: the "
               "only type of study that carries the review's template into a phason-bearing solid.",
         fits="s13_multiphysics", inout="inside for the heat law; outside for the quasicrystal elasticity"),
    dict(key="Nishimura2005", area="c", kind="article",
         authors=[("Nishimura","K."),("Shigekawa","N."),("Yokoyama","H."),("Hohkawa","K.")], year="2005",
         title="Temperature dependence of surface acoustic wave characteristics of GaN layers on sapphire substrates",
         journal="Japanese Journal of Applied Physics", volume="44", pages="L564",
         doi="10.1143/JJAP.44.L564", ver="R0",
         shows="Measures how the SAW velocity and coupling on GaN/sapphire move with temperature — the "
               "device-level data a thermoelastic surface-wave model has to face.",
         fits="s10_surface", inout="outside the template"),
]

AREA_D = [
    dict(key="Biot1941", area="d", kind="article", authors=[("Biot","M. A.")], year="1941",
         title="General theory of three-dimensional consolidation", journal="Journal of Applied Physics",
         volume="12", pages="155-164", doi="10.1063/1.1712886", ver="R0",
         shows="The poroelastic consolidation theory: a pore-pressure field diffuses while the skeleton "
               "deforms, the template that every porous thermoelastic model reuses with temperature in place of pressure.",
         fits="s15_applications", inout="outside the heat-flux template: a second diffusing field"),
    dict(key="SureshMortensen1997", area="d", kind="article",
         authors=[("Suresh","S."),("Mortensen","A.")], year="1997",
         title="Functionally graded metals and metal-ceramic composites: Part 2 Thermomechanical behaviour",
         journal="International Materials Reviews", volume="42", pages="85-116",
         doi="10.1179/imr.1997.42.3.85", ver="R0",
         shows="The reference review of functionally graded materials: how a graded composition changes "
               "thermal stress, cracking and fatigue, and what the grading profile is for.",
         fits="s15_applications", inout="outside the template: the grading enters the fields, not G(s)"),
    dict(key="Eerenstein2006", area="d", kind="article",
         authors=[("Eerenstein","W."),("Mathur","N. D."),("Scott","J. F.")], year="2006",
         title="Multiferroic and magnetoelectric materials", journal="Nature", volume="442",
         pages="759-765", doi="10.1038/nature05023", ver="R0",
         shows="Review of materials in which magnetic and electric orders coexist and couple — the "
               "material basis for the magneto-electro-elastic continuum.",
         fits="s13_multiphysics", inout="outside the template"),
    dict(key="Nan2008", area="d", kind="article",
         authors=[("Nan","C.-W."),("Bichurin","M. I."),("Dong","S."),("Viehland","D."),("Srinivasan","G.")],
         year="2008", title="Multiferroic magnetoelectric composites: historical perspective, status, and "
               "future directions",
         journal="Journal of Applied Physics", volume="103", pages="031101",
         doi="10.1063/1.2836410", ver="R0",
         shows="The standard review of magnetoelectric composites, including the homogenised "
               "magneto-electro-elastic constitutive law that wave studies then use.",
         fits="s13_multiphysics", inout="outside the template: two extra fields in the constitutive law"),
    dict(key="Iijima1991", area="d", kind="article", authors=[("Iijima","S.")], year="1991",
         title="Helical microtubules of graphitic carbon", journal="Nature", volume="354",
         pages="56-58", doi="10.1038/354056a0", ver="R0",
         shows="Reports multi-walled carbon nanotubes — the origin of the nanotube reinforcement and "
               "nanoresonator literature the review's size section touches.",
         fits="s12_size", inout="outside the template"),
    dict(key="Lee2008", area="d", kind="article",
         authors=[("Lee","C."),("Wei","X."),("Kysar","J. W."),("Hone","J.")], year="2008",
         title="Measurement of the elastic properties and intrinsic strength of monolayer graphene",
         journal="Science", volume="321", pages="385-388", doi="10.1126/science.1157996", ver="R0",
         shows="Nanoindentation values for the elastic modulus and strength of monolayer graphene — the "
               "numbers behind graphene resonator models.",
         fits="s12_size", inout="outside the template"),
    dict(key="Vengallatore2005", area="d", kind="article", authors=[("Vengallatore","S.")], year="2005",
         title="Analysis of thermoelastic damping in laminated composite micromechanical beam resonators",
         journal="Journal of Micromechanics and Microengineering", volume="15", pages="2398-2404",
         doi="10.1088/0960-1317/15/12/023", ver="R0",
         shows="Extends the Zener-type computation to a laminated beam, where each layer contributes its "
               "own relaxation — the composite counterpart of the review's flexural damping section.",
         fits="s04b_flexted", inout="inside: classical Fourier conduction, with the elastic operator layered"),
    dict(key="Zhong2017", area="d", kind="article",
         authors=[("Zhong","Z.-Y."),("Zhou","J.-P."),("Zhang","H.-L.")], year="2017",
         title="Thermoelastic damping in functionally graded microbeam resonators",
         journal="IEEE Sensors Journal", volume="17", pages="3381-3390",
         doi="10.1109/JSEN.2017.2694550", ver="R0",
         shows="Computes the damping peak of a graded microbeam and shows how the grading profile shifts "
               "and flattens the Zener peak.",
         fits="s04b_flexted", inout="inside: classical Fourier conduction"),
    dict(key="Fazzolari2018", area="d", kind="article", authors=[("Fazzolari","F. A.")], year="2018",
         title="Thermoelastic vibration and stability of temperature-dependent carbon nanotube-reinforced "
               "composite plates",
         journal="Composite Structures", volume="196", pages="199-214",
         doi="10.1016/j.compstruct.2018.04.026", ver="R0",
         shows="Free vibration and thermal buckling of CNT-reinforced plates with temperature-dependent "
               "properties, in a refined layerwise expansion.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Zorammuana2015", area="d", kind="article",
         authors=[("Zorammuana","C."),("Singh","S. S.")], year="2015",
         title="Elastic waves in thermoelastic saturated porous medium", journal="Meccanica",
         volume="51", pages="593-609", doi="10.1007/s11012-015-0225-x", ver="R0",
         shows="Wave speeds and attenuation in a thermoelastic saturated porous solid: three body waves "
               "plus a thermal mode, with the porous couplings explicit.",
         fits="s13_multiphysics", inout="partly inside: a thermoelastic skeleton with a pore fluid"),
    dict(key="SinghLianngenga2017", area="d", kind="article",
         authors=[("Singh","S. S."),("Lianngenga","R.")], year="2017",
         title="Effect of micro-inertia in the propagation of waves in micropolar thermoelastic materials with voids",
         journal="Applied Mathematical Modelling", volume="49", pages="487-497",
         doi="10.1016/j.apm.2017.05.008", ver="R0",
         shows="Shows that micro-inertia adds a dispersive branch to a micropolar thermoelastic solid with "
               "voids, and quantifies what is lost if it is dropped.",
         fits="s13_multiphysics", inout="partly inside: thermoelastic with extra balance laws"),
    dict(key="Kalkal2020Refl", area="d", kind="article",
         authors=[("Kalkal","K. K."),("Sheoran","D."),("Deswal","S.")], year="2020",
         title="Reflection of plane waves in a nonlocal micropolar thermoelastic medium under the effect of rotation",
         journal="Acta Mechanica", volume="231", pages="2849-2866",
         doi="10.1007/s00707-020-02676-w", ver="R0",
         shows="Reflection coefficients for a nonlocal micropolar thermoelastic half-space in rotation — "
               "three enrichments (nonlocality, micropolar inertia, rotation) in one boundary-value problem.",
         fits="s13_multiphysics", inout="partly inside: a generalized heat law with nonlocal and micropolar elasticity"),
    dict(key="Peng2023", area="d", kind="article",
         authors=[("Peng","W."),("Pan","B."),("Meng","L.")], year="2023",
         title="Thermoelastic damping analysis of functionally graded sandwich microbeam resonators "
               "incorporating nonlocal and surface effects",
         journal="Mechanics of Advanced Materials and Structures", volume="31", pages="9334-9344",
         doi="10.1080/15376494.2023.2270996", ver="R0",
         shows="Damping of a graded sandwich microbeam with nonlocal elasticity and surface energy, i.e. "
               "three size mechanisms acting on the same loss peak.",
         fits="s04b_flexted", inout="partly inside: Fourier conduction with nonlocal elasticity"),
    dict(key="Meng2026", area="d", kind="article",
         authors=[("Meng","J."),("Zhang","X."),("He","T.")], year="2026",
         title="Thermoelastic buckling of functionally graded GPL/CNT-reinforced composite microbeam under "
               "nonlocal heat conduction and nonlocal strain-gradient theory",
         journal="Physica Scripta", volume="101", pages="055005", doi="10.1088/1402-4896/ae3d6d", ver="R0",
         shows="Puts a nonlocal (space-fractional-like) heat law together with nonlocal strain-gradient "
               "elasticity in a buckling problem — a direct test of the review's claim that the two "
               "nonlocalities must be distinguished.",
         fits="s12_size", inout="partly inside: the heat law is nonlocal, hence outside the local template"),
    dict(key="Pearce2011", area="d", kind="article", authors=[("Pearce","J.")], year="2011",
         title="Mathematical models of laser-induced tissue thermal damage",
         journal="International Journal of Hyperthermia", volume="27", pages="741-750",
         doi="10.3109/02656736.2011.580822", ver="R0",
         shows="Reviews the damage integrals used to convert a computed tissue temperature history into "
               "an injury prediction — what a bioheat calculation is actually for.",
         fits="s15_applications", inout="outside the template"),
    dict(key="Li2026Bio", area="d", kind="article",
         authors=[("Li","X."),("Ning","B."),("Song","X."),("Wang","Z.")], year="2026",
         title="Non-Fourier bioheat conduction and tissue damage during laser brain hyperthermia with "
               "variable thermal properties",
         journal="International Communications in Heat and Mass Transfer", volume="176", pages="111369",
         doi="10.1016/j.icheatmasstransfer.2026.111369", ver="R0",
         shows="Non-Fourier (hyperbolic) bioheat with temperature-dependent properties, used to predict "
               "damage in laser brain hyperthermia — the applied end of the review's tissue discussion.",
         fits="s15_applications", inout="inside: a lagged heat law carried into a biological medium"),
]

AREA_D.append(dict(key="Noda1991", area="d", kind="article", authors=[("Noda","N.")], year="1991",
    title="Thermal stresses in materials with temperature-dependent properties",
    journal="Applied Mechanics Reviews", volume="44", pages="383-397",
    doi="10.1115/1.3119511", ver="R0",
    shows="Review of thermoelasticity when the properties themselves depend on temperature: the "
          "nonlinearity that every constant-property wave theory linearises away.",
    fits="s15_applications", inout="outside the template: the coefficients in G(s) become field-dependent"))
AREA_D.append(dict(key="Gibson2010", area="d", kind="article", authors=[("Gibson","R. F.")], year="2010",
    title="A review of recent research on mechanics of multifunctional composite materials and structures",
    journal="Composite Structures", volume="92", pages="2793-2810",
    doi="10.1016/j.compstruct.2010.05.003", ver="R0",
    shows="Review of multifunctional composites in which structural and thermal (or electrical, magnetic) "
          "functions are carried by the same material — the design context for graded and laminated models.",
    fits="s15_applications", inout="outside the template"))
