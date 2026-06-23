from fuels import FUELS_DICTIONARY
from stoichiometry import combustion_reaction
from thermo_properties import ThermoData
from solver import solver_Tad

# Data file path for enthalpy data
ENTHALPY_DATABASE = "data/enthalpy_data.xlsx"

print("\nAVAILABLE FUELS:\n")
for fuel in FUELS_DICTIONARY:
    print(fuel)

input_fuel = input("\nFuel: ").strip()

air_excess = float(input("Air excess (0.10 = 10%): "))

Tamb = float(input("Ambient temperature [K]: "))

reactants, products = (combustion_reaction(input_fuel, air_excess))

print("\nREACTANTS")

for sp, n in reactants.items():
    print(
        f"{sp}: {n:.4f}"
    )

print("\nPRODUCTS")

for sp, n in products.items():
    print(
        f"{sp}: {n:.4f}"
    )

thermo = ThermoData(ENTHALPY_DATABASE)

Tad = solver_Tad(thermo, reactants, products, T0=Tamb)

print(f"\nAdiabatic Flame Temperature = {Tad:.2f} K")