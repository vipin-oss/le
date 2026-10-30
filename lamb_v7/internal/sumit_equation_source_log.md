# Paper A (Sumit): equation source log

Rule: an entry is [R] only if I opened the source and can point to the equation or the sentence. Anything
else is [T] textbook, [D] instruction, [P] proposed, or [S] secondary (someone else quoting the number).

| Eq. | Term | Source | What I actually read | Status |
|---|---|---|---|---|
| (N1) | NSGT differential law, operator on inertia and on c:eps | Lim, Zhang & Reddy, JMPS 78 (2015) 298, 10.1016/j.jmps.2015.02.001 | Nothing of the paper itself: Elsevier PDF closed. The equation numbers (18) and (19) are from the introduction of Barretta & Marotti de Sciarra, IJES 130 (2018) 187, 10.1016/j.ijengsci.2018.05.009, read in full: "replaced by Lim et al. (2015) with the differential law Eq. (18)" and "constitutive boundary conditions (CBC) Eq. (19)". | [S] |
| (N2) | Equivalent momentum form | own one-line derivation from (N1) | Multiply the balance by the operator and commute it with the divergence. | derivation, to be confirmed by the scholar |
| (A1) beta_ij theta | thermal stress, Duhamel | textbook thermoelasticity | Formula standard; no equation number needed. | [T] |
| (A2) p_i theta | pyroelectric polarisation | textbook | Standard; no source read this round. | [T] |
| (A4) | Gauss law with mobile charge | Yang & Zhou, IJSS 42 (2005) 3171, 10.1016/j.ijsolstr.2004.10.011 | Crossref title ("Amplification of acoustic waves in piezoelectric semiconductor plates") and abstract only. Equations NOT read. | [T] + [S] |
| (A5) | drift, diffusion, recombination | as above | Same. | [T] |
| (A5) beta_th lap(theta) | thermodiffusion | textbook irreversible thermodynamics | Standard cross-effect; no equation number. | [T] |
| (A7) | Pi_th = T_0 S_n, ratio Pi/beta | textbook thermoelectricity (Kelvin relation), used in a PSC continuum by Qu, Pan, Zhu, Jin & Roy, IJES 182 (2023) 103775, 10.1016/j.ijengsci.2022.103775 | Abstract read: "thermodynamically consistent constitutive equations ... drift-diffusion current, Fourier's law ... Seebeck effect, and Peltier effect". Their equations NOT read. | [T] + [S] |
| (A6) | MGT operator, base form K*=0, one derivative cancelled | form fixed by Dr. Vipin [D]; attendant paper Gupta et al., IJNMHFF 35(9) (2025) 3400, 10.1108/HFF-04-2025-0254 | Crossref title and abstract read: "Piezo-semiconductor-void interplay in the size-dependent dynamics of Rayleigh waves within the Moore-Gibson-Thompson framework". Their heat equation NOT read. | [D] + [S] |
| (A6) | -q Pi_th d(dn)/dt | see (A7) | | [T] |
| (A6) | E_g dn/tau_R pair | energy balance of the electron gas | | [P] |
| constants | ZnO c, e, eps, rho | Ozgur et al., JAP 98 (2005) 041301, 10.1063/1.1992666 | Read earlier in the round: piezo constants quoted across studies as e31 -0.39..-0.66 (mostly -0.52), e33 0.92..1.30 (mostly 1.20) C/m2. No single self-consistent measured set located. | partial [R] |
| Lambda_ph | phonon mean free path of ZnO | Krahl et al., JPCC 124 (2020) 24731, 10.1021/acs.jpcc.0c06461 | The paper reports thermal conductivity of ZnO-benzene multilayer films. Lambda is OUR gray-medium estimate from their kappa, not a number they state. | estimate, labelled as such |

## Week-one reading for Sumit

1. Lim, Zhang & Reddy, section 2, equations (17) to (19). Confirm the differential law and the CBC.
2. Qu, Pan, Zhu, Jin & Roy, sections 2 and 3, the dissipation inequality and the resulting Peltier term.
3. Yang & Zhou, section 2, the drift-diffusion pair and the plate boundary conditions.
4. Gupta et al., the MGT heat equation and the void terms, to see which terms they keep.
5. Sharma, Pal & Chand, the secular equations and the attenuation definition, so that our attenuation is
   comparable with a published one.
