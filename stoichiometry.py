from fuels import FUELS_DICTIONARY
def combustion_reaction(fuel_name, air_excess=0.0):
    fuel = FUELS_DICTIONARY[fuel_name]
    C_atoms = fuel["C"]
    H_atoms = fuel["H"]
    O_atoms = fuel["O"]

    O2_stoich = C_atoms + H_atoms/4 - O_atoms/2
    O2 = O2_stoich * (1 + air_excess)

    N2 = O2 * 3.76

    reactants = {
        fuel_name: 1,
        "O2": O2,
        "N2": N2
    }

    products = {
        "CO2": C_atoms,
        "H2O": H_atoms/2,
        "N2": N2
    }

    return reactants, products