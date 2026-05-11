# Python para MLOps — Fundamentos Practicos

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0099B5?style=flat-square&logo=pytest&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![LinkedIn](https://img.shields.io/badge/LinkedIn%20Learning-0A66C2?style=flat-square&logo=linkedin&logoColor=white)

Practica de Python aplicada a MLOps, basada en el curso de LinkedIn Learning **[Complete Guide to Python Fundamentals for MLOps](https://www.linkedin.com/learning/complete-guide-to-python-fundamentals-for-mlops)**.

Construido como parte del Master en Big Data, Data Engineering & AI — ESESA, Malaga 2025-2026.

---

## Contenido

### Fundamentos de Python

| Notebook / Archivo | Tema |
|------------------|------|
| `01_variables.ipynb` | Variables, tipos de datos, operaciones basicas |
| `02_lists.ipynb` | Listas: creacion, slicing, manipulacion |
| `03_Adding_extracting_data.ipynb` | Agregar y extraer datos de estructuras |
| `03_dictionaries.ipynb` | Diccionarios: keys, values, get, update |
| `04_Tuples_and_sets.ipynb` | Tuplas y sets: inmutabilidad y operaciones de conjuntos |
| `04_Working_with_functions.ipynb` | Funciones: argumentos, returns, scope |
| `05_building_clasees_and_methods.ipynb` | Programacion orientada a objetos: clases y metodos |
| `06_Python_functions_and_classes.ipynb` | Funciones avanzadas y clases en profundidad |

### Testing con pytest

| Archivo | Tema |
|---------|------|
| `07_Testing.ipynb` | Introduccion a testing con pytest |
| `08_test_functions.py` | Tests unitarios para funciones |
| `08_test_classes.py` | Tests unitarios para clases |
| `08_test_utils.py` | Tests para utilerias |

### Datos con Pandas

| Notebook | Tema |
|---------|------|
| `10_Introduction_to_pandas.ipynb` | Introduccion a pandas para analisis de datos |

### Codigo de produccion

```
program/
|-- __init__.py
|-- items.py           # Modulo de ejemplo con clases de negocio
utils.py                # Funciones utilitarias
script.py               # Script principal ejecutable
examples/               # Ejemplos complementarios
plain-asserts/          # Tests con asserts planos (sin pytest)
```

---

## Stack tecnologico

| Tecnologia | Uso |
|-----------|-----|
| Python 3.8+ | Lenguaje base |
| NumPy | Calculo numerico y arrays |
| pandas | Manipulacion y analisis de datos tabulares |
| pytest | Framework de testing unitario |
| Jupyter | Notebooks para experimentacion |

---

## Como ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/xfalconix/python_mlops_course.git
cd python_mlops_course

# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Ejecutar notebooks
jupyter notebook

# Ejecutar tests
pytest -v
```

---

## Que demuestra este repo

- Dominio solido de **Python fundamentals** (POO, funciones, estructuras de datos)
- Habilidad de escribir **tests unitarios** con pytest
- Capacidad de estructurar un **proyecto de Python** con modulos y paquetes
- Familiaridad con **pandas y NumPy** para procesamiento de datos

Estos fundamentos son el cimiento de cualquier pipeline MLOps: scripts de ingestion, feature engineering, training loops y serving scripts se escriben en Python.

---

## Autor

Carlos Falconi — Master en Big Data, Data Engineering & AI — ESESA, Malaga 2025-2026
