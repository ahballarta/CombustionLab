# CombustionLab (README en Español)

**CombustionLab** es una herramienta de cálculo de combustión basada en Python diseñada para estimar la temperatura de llama adiabática de combustibles simples mediante combustión estequiométrica, exceso de aire y datos termodinámicos tabulados.

El proyecto fue creado como una herramienta de aprendizaje e ingeniería para conectar la teoría de combustión con una implementación computacional en Python.

---

## Versión

Versión actual: **V1 (Lanzamiento inicial - En desarrollo)**

Esta es una versión inicial. El proyecto está en desarrollo activo y puede cambiar significativamente en futuras versiones.

---

## Características

- Define propiedades básicas de combustibles como metano, propano e hidrógeno  
- Calcula reacciones de combustión estequiométrica  
- Permite definir exceso de aire y temperatura ambiente (configurado en el código)  
- Lee datos termodinámicos desde un archivo Excel  
- Estima la temperatura adiabática mediante un método iterativo numérico  
- Estructura modular separando combustión, termodinámica y manejo de datos  

---

## Estructura del proyecto

```
CombustionLab/
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

---

## Cómo funciona

1. Se selecciona un combustible del listado disponible  
2. Se define el exceso de aire y la temperatura ambiente en el código  
3. Se calculan reactivos y productos de combustión  
4. Se cargan datos de entalpía desde Excel  
5. Se resuelve la temperatura adiabática de forma iterativa  

---

## Uso

Ejecutar el programa:

```bash
python main.py
```

Ejemplo de input:

```text
Fuel: CH4
Air excess (0.10 = 10%): 0.10
Ambient temperature [K]: 298
```

Ejemplo de output:

```text
REACTANTS
CH4: 1.0000
O2: 2.2000
N2: 8.2720

PRODUCTS
CO2: 1.0000
H2O: 2.0000
N2: 8.2720

Adiabatic Flame Temperature = XXXX.XX K
```
---

## Fundamento de ingeniería

Para un combustible genérico CxHyOz:

Requerimiento de oxígeno:

```text
O2,stoich = x + y/4 - z/2
```

Productos principales:

```text
CO2, H2O, N2
```

Supuestos del modelo:
- Combustión completa  
- Sin disociación química  
- Sin pérdidas de calor  

---

## Fuentes de combustibles disponibles

El proyecto incluye:

| Combustible | Nombre | Fórmula |
|---|---|---|
| CH4 | Metano | CH₄ |
| C3H8 | Propano | C₃H₈ |
| H2 | Hidrógeno | H₂ |

---

## Requisitos

Instalar dependencias:

```bash
pip install pandas numpy openpyxl
```

---

## Limitaciones actuales

- No incluye efectos de disociación  
- Base de combustibles limitada  
- No tiene interfaz de usuario  
- Modelo simplificado de combustión  
- No reporta oxígeno remanente explícitamente  

---

## Futuras mejoras

- Añadir más combustibles  
- Análisis de gases de combustión  
- Interfaz tipo CLI (V2)  
- Validación de entradas  
- Herramientas de visualización  

---

## Licencia

Este proyecto está publicado bajo licencia MIT para uso educativo e ingenieril.

---

## Autor

Desarrollado por **André Ballarta Elguera**.

# CombustionLab (README in English)

**CombustionLab** is a Python-based combustion calculation tool designed to estimate the adiabatic flame temperature of simple fuels using stoichiometric combustion, excess air and tabulated thermodynamic data.

The project was created as a learning and engineering tool to connect combustion theory with a computational implementation in Python.

## Version

Current version: **V1 (Initial Release - Work in Progress)**

This is an early-stage version. The project is under active development and may change significantly in future releases.

## Features
- Defines basic fuel properties for methane, propane, and hydrogen
- Calculates stoichiometric combustion reactions
- Allows excess air and ambient temperature input (via code configuration)
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

## How It Works

The program follows these main steps:

1. The user selects a fuel from the available fuel database.
2. The user enters the excess air value and ambient temperature.
3. The program calculates the combustion reactants and products.
4. Thermodynamic enthalpy data is loaded from `enthalpy_data.xlsx`.
5. The adiabatic flame temperature is estimated through an iterative bisection method.

## Usage
Run the program:

```bash
python main.py
```

Example input:

```text
Fuel: CH4
Air excess (0.10 = 10%): 0.10
Ambient temperature [K]: 298
```

Example output:

```text
REACTANTS
CH4: 1.0000
O2: 2.2000
N2: 8.2720

PRODUCTS
CO2: 1.0000
H2O: 2.0000
N2: 8.2720

Adiabatic Flame Temperature = XXXX.XX K
```

## Engineering Background

For a generic fuel with the form CxHyOz, the stoichiometric oxygen requirement is calculated as:

```text
O2,stoich = x + y/4 - z/2
```

The combustion reaction assumes complete combustion, producing mainly:

```text
CO2, H2O and N2
```

Energy balance is solved iteratively assuming:
- Complete combustion
- No dissociation
- No heat losses

## Available Fuels

The current version includes:

| Fuel | Name | Formula |
|---|---|---|
| CH4 | Methane | CH₄ |
| C3H8 | Propane | C₃H₈ |
| H2 | Hydrogen | H₂ |

## Libraries Requirements

Install the required Python libraries:

```bash
pip install pandas numpy openpyxl
```

## Current Limitations

- No chemical dissociation effects
- Limited fuel database
- No user interface (inputs are defined in code)
- Simplified combustion model
- No exhaust gas reporting for oxygen excess

## Future Improvements

- Add additional fuels
- Add flue gas composition analysis
- Add CLI interface (V2 feature)
- Add validation and error handling
- Add visualization tools

## License

This project is released under the MIT License for educational and engineering use.

## Author

Developed by **André Ballarta Elguera**.

