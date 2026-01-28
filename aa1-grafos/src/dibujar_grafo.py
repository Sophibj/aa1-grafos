# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "rutas_khan.csv"
OUT = Path(__file__).resolve().parents[1] / "img" / "grafo_khan.png"
LAYOUT = "manual"  # 'manual' | 'kamada_kawai' | 'spring'


def cargar_csv(ruta: Path) -> pd.DataFrame:
    df = pd.read_csv(ruta)  # pandas.read_csv
    df = df.rename(columns=str.lower)
    return df[["source", "target", "distance"]]


def construir_grafo(df: pd.DataFrame) -> nx.Graph:
    G = nx.Graph()
    for _, r in df.iterrows():
        G.add_edge(r["source"], r["target"], weight=float(r["distance"]))
    return G


def posiciones(G: nx.Graph, layout: str) -> dict:
    layout = layout.lower()
    if layout == "manual":
        # Coordenadas aproximadas para parecerse a la imagen original (x, y):
        return {
            # bloque noreste (Maine)
            "Boston": (10.0, 0.0),
            "Reading": (8.6, 0.45),
            "Weston": (7.9, 0.2),
            "Canton": (7.8, -0.55),
            "Providence": (7.0, -0.9),
            "Sturbridge": (6.4, 0.45),

            # eje central
            "Springfield": (5.2, 0.3),
            "Hartford": (4.6, 0.0),
            "New Haven": (4.1, -0.65),
            "New York": (3.4, -1.1),
            "Newburgh": (3.7, -0.4),
            "Albany": (3.2, 0.45),

            # norte (Vermont/New Hampshire)
            "White River Jct.": (5.0, 1.0),
            "St. Johnsbury": (5.3, 1.6),
            "Derby Line": (5.45, 2.1),
            "Concord": (5.9, 0.85),

            # noroeste
            "Highgate Springs": (4.25, 1.45),
            "Champlain": (3.3, 2.0),

            # este lejano
            "Bangor": (9.1, 1.0),
            "Houlton": (10.6, 1.0),
        }

    elif layout == "kamada_kawai":
        # Requiere SciPy. respetar longitudes relativas por peso.
        return nx.kamada_kawai_layout(G, weight="weight")
    elif layout == "spring":
        return nx.spring_layout(G, seed=7, weight="weight")
    else:
        raise ValueError("Layout no soportado.")


def dibujar(G: nx.Graph, pos: dict, salida: Path) -> None:
    plt.figure(figsize=(13, 6))

    # Aristas primero para que no tapen los nodos
    nx.draw_networkx_edges(G, pos, width=1.6, edge_color="#444")

    # Nodos
    nx.draw_networkx_nodes(G, pos, node_color="#98e6f5", node_size=1550, edgecolors="#333")

    # Etiquetas de nodos (pequeños ajustes para el “cluster” Boston–Reading–Weston–Canton–Providence)
    pos_lab = pos.copy()
    for n, (dx, dy) in {
        "Reading": (0.0, 0.10),
        "Weston": (0.0, -0.07),
        "Canton": (0.0, -0.08),
        "Providence": (0.0, -0.08),
        "Sturbridge": (0.0, 0.08),
    }.items():
        if n in pos_lab:
            x, y = pos_lab[n]
            pos_lab[n] = (x + dx, y + dy)

    nx.draw_networkx_labels(G, pos_lab, font_size=9, font_weight="bold")

    # Etiquetas de pesos
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.axis("off")
    salida.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(salida, dpi=200)
    print(f"Imagen creada en: {salida}")


def main():
    df = cargar_csv(DATA)
    G = construir_grafo(df)
    pos = posiciones(G, LAYOUT)
    dibujar(G, pos, OUT)


if __name__ == "__main__":
    main()