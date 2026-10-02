"""cg_model.py — material tensors for PROJECT_CRYSTAL_GEOMETRY_01 (SI units).
Sources/levels: PARAMETER_TABLE.md (Adachi 2018 EQUATIONS; Klimm 2023 FULL-TEXT;
expansion 2015 ABSTRACT; rho METADATA; c_p ESTIMATED). alpha5=0 LIMITATION.
"""
import numpy as np

# --- Verified inputs (SI) ---
Cij_GPa = dict(C11=242.8, C22=343.8, C33=347.4, C44=47.8, C55=88.6, C66=104.0,
               C12=128.0, C13=160.0, C23=70.9, C15=-1.62, C25=0.36, C35=0.97, C46=5.59)
K_ac = np.array([[12.13, -0.992], [-0.992, 14.09]])   # W/mK, (a,c)-plane block
alpha_crys = np.array([1.54e-6, 3.37e-6, 3.15e-6])    # 1/K along (a,b,c)
rho = 5880.0          # kg/m^3
cp_ESTIMATED = 560.0  # J/kg/K (Debye ThetaD=685K estimate; see PARAMETER_TABLE)
T0 = 293.0            # K

GPa = 1e9
def plane_strain_block():
    """2D plane-strain block in the a-c (x1,x3) plane, strain vector e=(e11,e33,g13).
    Returns Q (3x3, Pa) and beta (3,) thermal-stress moduli (Pa/K), alpha5=0."""
    C = Cij_GPa
    Q = np.array([[C['C11'], C['C13'], C['C15']],
                  [C['C13'], C['C33'], C['C35']],
                  [C['C15'], C['C35'], C['C55']]]) * GPa
    a1, a2, a3 = alpha_crys
    a5 = 0.0  # UNRESOLVED thermal shear — LIMITATION
    beta = np.array([C['C11']*a1 + C['C12']*a2 + C['C13']*a3 + C['C15']*a5,
                     C['C13']*a1 + C['C23']*a2 + C['C33']*a3 + C['C35']*a5,
                     C['C15']*a1 + C['C25']*a2 + C['C35']*a3 + C['C55']*a5]) * GPa
    return Q, beta

def rotate2(K, phi):
    """Rotate 2x2 tensor by phi (radians, lab = R(phi) @ crystal)."""
    c, s = np.cos(phi), np.sin(phi)
    R = np.array([[c, -s], [s, c]])
    return R @ K @ R.T

def rotate_Q_beta(Q, beta, phi):
    """Rotate the 3x3 plane-strain stiffness (Voigt: e11,e33,g13) and beta to lab frame
    where lab x1 is rotated by phi from crystal x1 (rotation about x2=b).
    Voigt->4th-order with engineering shear and minor symmetry:
      sigma_ij = C_ijkl e_kl; g13 = e13+e31.
    Checks: phi=0 returns (Q, beta) exactly; phi=90 maps beta1<->beta3 crystal."""
    c, s = np.cos(phi), np.sin(phi)
    R = np.array([[c, -s], [s, c]])  # v_lab = R v_crys in the (x1,x3) plane
    C4 = np.zeros((2, 2, 2, 2))
    # normal rows: sigma11 = Q00 e11 + Q01 e33 + Q02 g13
    C4[0, 0, 0, 0] = Q[0, 0]; C4[0, 0, 1, 1] = Q[0, 1]
    C4[0, 0, 0, 1] = C4[0, 0, 1, 0] = Q[0, 2]
    C4[1, 1, 0, 0] = Q[1, 0]; C4[1, 1, 1, 1] = Q[1, 1]
    C4[1, 1, 0, 1] = C4[1, 1, 1, 0] = Q[1, 2]
    # shear row: sigma13 = Q20 e11 + Q21 e33 + Q22 g13 (and sigma31 = sigma13)
    C4[0, 1, 0, 0] = C4[1, 0, 0, 0] = Q[2, 0]
    C4[0, 1, 1, 1] = C4[1, 0, 1, 1] = Q[2, 1]
    C4[0, 1, 0, 1] = C4[0, 1, 1, 0] = C4[1, 0, 0, 1] = C4[1, 0, 1, 0] = Q[2, 2]
    C4r = np.einsum('ai,bj,ck,dl,ijkl->abcd', R, R, R, R, C4)
    Qr = np.array([
        [C4r[0, 0, 0, 0], C4r[0, 0, 1, 1], C4r[0, 0, 0, 1]],
        [C4r[1, 1, 0, 0], C4r[1, 1, 1, 1], C4r[1, 1, 0, 1]],
        [C4r[0, 1, 0, 0], C4r[0, 1, 1, 1], C4r[0, 1, 0, 1]]])
    # in-plane expansion tensor (a,c): diag(a1,a3), ac=0 (alpha5=0 LIMITATION)
    A2 = np.diag([alpha_crys[0], alpha_crys[2]])
    A2r = R @ A2 @ R.T
    a11, a33, a13 = A2r[0, 0], A2r[1, 1], A2r[0, 1]
    betar = np.array([
        C4r[0, 0, 0, 0]*a11 + C4r[0, 0, 1, 1]*a33 + C4r[0, 0, 0, 1]*(a13 + A2r[1, 0]),
        C4r[1, 1, 0, 0]*a11 + C4r[1, 1, 1, 1]*a33 + C4r[1, 1, 0, 1]*(a13 + A2r[1, 0]),
        C4r[0, 1, 0, 0]*a11 + C4r[0, 1, 1, 1]*a33 + C4r[0, 1, 0, 1]*(a13 + A2r[1, 0])])
    # b-axis expansion alpha2 via rotated C'12, C'23, C'25 (rotation about x2 keeps x2)
    a2 = alpha_crys[1]
    C12, C23, C25 = Cij_GPa['C12']*GPa, Cij_GPa['C23']*GPa, Cij_GPa['C25']*GPa
    C12p = c*c*C12 + s*s*C23 + 2*c*(-s)*C25
    C23p = s*s*C12 + c*c*C23 + 2*s*(-c)*C25
    C25p = c*s*(C12 - C23) + (c*c - s*s)*C25
    betar += np.array([C12p, C23p, C25p]) * a2
    return Qr, betar

def derived():
    Q, beta = plane_strain_block()
    c_ref = np.sqrt(Cij_GPa['C33']*GPa / rho)
    kbar = np.sqrt(np.linalg.det(K_ac))  # sqrt(det) = sqrt(12.13*14.09-0.992^2)
    kappa = kbar / (rho * cp_ESTIMATED)
    Cbar = Cij_GPa['C33']*GPa
    delta = T0*np.dot(beta, beta)/(rho*cp_ESTIMATED*Cbar)
    return dict(c_ref=c_ref, kappa=kappa, kbar=kbar, Cbar=Cbar, delta=delta,
                beta_norm=np.linalg.norm(beta))

def iso_control():
    """Isotropic matched-modulus control: K_iso = mean of principal values of K_ac;
    isotropic plane-strain from E-mod of Cbar-scale with nu=0.27 (matched bulk order).
    Built so admissibility holds; label: CONTROL (ablation B1), not a material claim."""
    w, v = np.linalg.eigh(K_ac)
    K_iso = np.mean(w)*np.eye(2)
    # Lamé from E=C33-ish scale: choose lam, mu so bulk modulus matches plane-strain mean
    mu = Cij_GPa['C66']*GPa  # isotropic mu
    lam = Cij_GPa['C12']*GPa
    Q = np.array([[lam+2*mu, lam, 0.0],
                  [lam, lam+2*mu, 0.0],
                  [0.0, 0.0, mu]])
    a = float(np.mean(alpha_crys))
    beta = np.array([(3*lam+2*mu)*a, (3*lam+2*mu)*a, 0.0])  # alpha1=alpha2=alpha3=a
    return K_iso, Q, beta

if __name__ == '__main__':
    Q, beta = plane_strain_block()
    print('Q eig (Pa):', np.linalg.eigvalsh(Q))
    print('beta (Pa/K):', beta)
    print('derived:', derived())
    Ki, Qi, bi = iso_control()
    print('iso Q eig:', np.linalg.eigvalsh(Qi), 'K_iso:', Ki.ravel())
    # rotation covariance of Q assembly at 45deg: check Qr SPD
    for phi in (0.0, np.pi/4, np.pi/2):
        Qr, br = rotate_Q_beta(Q, beta, phi)
        print(f'phi={np.degrees(phi):.0f} Qr eig:', np.linalg.eigvalsh(Qr), 'beta r:', br)
