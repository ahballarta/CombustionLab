# CombustionLab

**CombustionLab** is a Python-based combustion calculation tool designed to estimate the adiabatic flame temperature of simple fuels using stoichiometric combustion, excess air and tabulated thermodynamic data.

The project was created as a learning and engineering tool to connect combustion theory with a computational implementation in Python.

## Version

Current version: **V1 (Initial Release - Work in Progress)**

This is an early-stage version. The project is under active development and may change significantly in future releases.

## Features
- Defines basic fuel properties for methane, propane, and hydrogen
- Calculates stoichiometric combustion reactions- Allows excess air and ambient temperature input (via code configuration)
- Reads thermodynamic enthalpy data from an Excel database
- Estimates adiabatic flame temperature using an iterative numerical solver
- Modular code structure separating combustion, thermodynamics, and data handling

## Project Structure
```
textCombustionLab/
│
├── main.py
├── fuels.py
├── stoichiometry.py
├── thermo_properties.py
├── solver.py
│
└── data/
    └── enthalpy_data.xlsx
```

## License

This project is released under the MIT License for educational and engineering use.

## Author

Developed by **André Ballarta Elguera**.

