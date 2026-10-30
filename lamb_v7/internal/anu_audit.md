# Paper C (Anu): sign and unit audit

## 1. Piezoelectric pair

`-e E` in the stress, `+e eps` in `D_i`. Same tensor, opposite signs, energy `-eE eps`. Dimensions: `eE` in
Pa, `e eps` in C/m2.

## 2. Piezomagnetic pair

`-h H` in the stress, `+h eps` in `B_i`. Same tensor, opposite signs, for the same reason. Dimensions: `h`
in N/(A m), so `hH` = (N/Am)(A/m) = N/m2 = Pa, and `h eps` = N/(A m) = T. Both correct.

## 3. Magnetoelectric pair, the delicate one

    D_i = ... + alpha_ik H_k ,        B_i = ... + alpha_ik E_k

Reciprocity needs the same coefficient in both, with the energy term `-alpha_ik E_i H_k`. Written this way
the two appearances must carry the same sign; a minus in one and a plus in the other would make the energy
path-dependent. Dimensions: `alpha H` = (s/m)(A/m) = C/m2, a displacement; `alpha E` = (s/m)(V/m) =
V s/m2 = Wb/m2 = T, an induction. Both correct, and this is the neatest confirmation that the unit of alpha
is s/m.

Two traps. First, in a laminate alpha is a product property, so it is not a material constant and must not
be fitted as one. Second, papers differ in the sign convention for `H`, because some define it from a scalar
potential with the opposite sign. The scholar must fix the convention once in the notation table and keep
it. In ours `H_i = -psi_,i` and both entries are plus.

## 4. Pyroelectric and electrocaloric

`+p theta` in `D_i`; `+T0 p dE/dt` in the heat bracket. Same constant, factor T0, bracket carries the
negative of the source. Dimensions C/m2 and W/m3.

## 5. Pyromagnetic and magnetocaloric

`+m theta` in `B_i`; `+T0 m dH/dt` in the heat bracket. Dimensions: `m theta` = (N/AmK)(K) = T;
`T0 m dH/dt` = K (N/(A m K))(A/(m s)) = N/(m2 s) = W/m3. Correct.

## 6. Thermal stress and the MGT operator

`-beta theta` in the stress; `+T0 beta d eps/dt` in the bracket. Pa and W/m3.
`(1 + tau_q d/dt)` dimensionless on W/m3.

## 7. Electric and magnetic Gauss laws

`D_i,i = 0` and `B_i,i = 0`, in C/m3 and T/m. With no free charge and no free current these are the right
right-hand sides. If a free charge density is added later the electric law changes and the magnetic one does
not; that asymmetry deserves a sentence.

## 8. Effective constants from two routes

Neither route preserves every constant exactly. The rule of mixtures is exact for a layered stack along the
layering direction and wrong in the plane; Mori-Tanaka is better for inclusions and worse for continuous
layers. The audit here is not about signs but about honesty: both route values must be shown, and their
difference must be compared with the size of the thermal contribution before any claim is made. This is the
week-nine decision in the plan.

## 9. Unit audit, every term

Stress: `-e E`, `-h H`, `-beta theta`, all Pa. Electric displacement: `e eps`, `eps E`, `alpha H`, `p theta`,
all C/m2. Magnetic induction: `h eps`, `alpha E`, `mu H` = (N/A2)(A/m) = N/(A m) = T, and `m theta` = T.
Heat equation: every bracket entry W/m3 and the conduction term W/m3. Momentum with the size effect: N/m3 on
both sides.
