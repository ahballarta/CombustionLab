import pandas as pd
import numpy as np

class ThermoData:
    def __init__(self, file_path):
        # file_path to be defined in main.py for manteinability purposes
        self.dataframe = pd.read_excel(file_path,header=3)

    def get_enthalpy(self,species, T):
        return np.interp(T,self.dataframe["T"],self.dataframe[species])
    
print("\nThermodynamic data loaded successfully.")

#thermo_debug = ThermoData("data/enthalpy_data.xlsx")

#prueba = thermo_debug.get_enthalpy("CO2", 1000)
#print(prueba)
