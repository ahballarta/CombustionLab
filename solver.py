
from fuels import FUELS_DICTIONARY

def solver_Tad(thermo, reactants, products, T0=298):
    H_react = 0
    PCI_total = 0

    for sp, n in reactants.items():
        if sp in FUELS_DICTIONARY:
            PCI_total += n * FUELS_DICTIONARY[sp]["PCI"]
        else:
            H_react += n * thermo.get_enthalpy(sp, T0)

    target = H_react + PCI_total

    T_low = 300
    T_high = 6000

    for i in range(100):
        T_mid = (T_low + T_high) / 2
        H_mid = sum(n * thermo.get_enthalpy(sp, T_mid) for sp, n in products.items())
        
        print(f"Iter {i+1}: T_mid={T_mid:.2f} K, H_mid={H_mid:.2f}, target={target:.2f}, error={H_mid-target:.2f}")

        if H_mid < target:
            T_low = T_mid
        else:
            T_high = T_mid

        if (T_high - T_low) < 0.01:
            break

    return (T_low + T_high) / 2
