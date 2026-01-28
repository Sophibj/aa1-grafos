# AA1 · Unidad 1 · Manipulación de datos y herramientas para IA

**Repositorio académico** que modela y dibuja un *grafo ponderado* a partir de la Figura 1 (mapa de carreteras) de Khan Academy. El conjunto de datos se almacena en CSV y la visualización se genera con **pandas**, **NetworkX** y **Matplotlib**.

## Estructura
```
aa1-grafos/
├─ data/              # CSV con aristas y distancias
│  └─ rutas_khan.csv
├─ src/               # Código fuente
│  └─ dibujar_grafo.py
├─ img/               # Salidas (PNG)
├─ requirements.txt   # Dependencias
└─ .gitignore
```

## Cómo ejecutar
```bash
# 1) Crear y activar entorno virtual (opcional pero recomendado)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Generar la imagen del grafo
python src/dibujar_grafo.py
# → img/grafo_khan.png
```

## Descripción técnica
El dataset `data/rutas_khan.csv` contiene pares de ciudades (origen/destino) y la distancia en millas como peso de la arista. El script `src/dibujar_grafo.py` carga el CSV en un `DataFrame`, construye un grafo **no dirigido** y posiciona los nodos con el layout **Kamada–Kawai**, que busca preservar distancias relativas según los pesos. La imagen resultante incluye etiquetas de nodos y de pesos sobre cada arista.

## Resultados
La visualización resultante (`img/grafo_khan.png`) reproduce de forma legible la estructura del grafo mostrada en la figura original, con nombres de ciudades y distancias claramente visibles.

## Referencias (APA )
- Khan Academy. (s. f.). *Describing graphs*. En Computer science – Algorithms. https://www.khanacademy.org/computing/computer-science/algorithms/algorithms/graph-representation/a/describing-graphs
- NetworkX Developers. (s. f.). *kamada_kawai_layout — NetworkX documentation*. https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.kamada_kawai_layout.html
- NetworkX Developers. (s. f.). *Weighted Graph (gallery example)*. https://networkx.org/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
- pandas. (s. f.). *pandas.read_csv — pandas documentation*. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- Matplotlib. (s. f.). *matplotlib.pyplot — Matplotlib documentation*. https://matplotlib.org/stable/api/pyplot_summary.html
