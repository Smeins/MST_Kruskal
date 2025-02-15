#  Minimum Spanning Tree (MST) - Kruskal & Prim Algorithmen

Dieses Repository enthält eine Implementierung und Visualisierung des **Minimum Spanning Tree (MST)** mit dem **Kruskal Algorithmus**. Außerdem wird der **Prim’s Algorithmus** angeschnitten, jedoch nicht visualisiert. Zusätzlich wird der MST sowohl in **2D als auch in 3D** visualisiert. 

---

##  Was ist ein Minimum Spanning Tree (MST)?
Ein **Minimum Spanning Tree (MST)** ist ein Teilgraph eines gewichteten, zusammenhängenden und ungerichteten Graphen, der:
- Alle Knoten des Graphen verbindet.
- Die minimale Summe der Kantengewichte aufweist.
- **Keinen Zyklus** enthält.

---

##  Kruskal’s Algorithmus (Greedy-Ansatz)
**Idee:**
- Wähle die **leichteste Kante**, die keinen **Zyklus** erzeugt.
- Füge sie dem MST hinzu.
- Wiederhole, bis **n-1 Kanten** im Baum sind.

🔹 **Datenstruktur:** **Union-Find (Disjoint Set Union, DSU)**

🔹 **Laufzeit:** \( O(E \log E) \) (weil die Kanten zuerst sortiert werden)

###  Beispiel:
```plaintext
Knoten:  {0, 1, 2, 3}
Kanten mit Gewichten:
    (0 - 1, 1)
    (0 - 2, 4)
    (1 - 2, 2)
    (1 - 3, 6)
    (2 - 3, 3)
```
Ergebnis (MST): **(0-1), (1-2), (2-3)** mit Gesamtgewicht **6**

---

##  Prim’s Algorithmus (Greedy-Ansatz)
**Idee:**
- Beginne bei einem beliebigen Knoten.
- Wähle die **leichteste angrenzende Kante**.
- Wiederhole, bis alle Knoten verbunden sind.

🔹 **Datenstruktur:** **Priority Queue (Heap)**

🔹 **Laufzeit:** \( O(E + V \log V) \)

---

##  Visualisierung in 2D & 3D
###  2D-Visualisierung mit `networkx`
 Zeigt den Originalgraphen & MST
```python
import networkx as nx
import matplotlib.pyplot as plt

```

###  3D-Visualisierung mit `mpl_toolkits.mplot3d`
 Zufällige 3D-Positionen für Knoten, MST in **rot** hervorgehoben.
```python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
```

---

##  Installation
### 1️ Abhängigkeiten installieren:
```bash
pip install networkx matplotlib numpy
```


---

##  Kruskal vs. Prim
| **Eigenschaft**  | **Kruskal** | **Prim** |
|------------------|------------|---------|
| **Ansatz**      | Greedy (Kanten-Auswahl) | Greedy (Knoten-Wachstum) |
| **Beste für**   | Spärliche Graphen | Dichte Graphen |
| **Laufzeit**    | \( O(E \log E) \) | \( O(E + V \log V) \) |

---

##  Anwendung
| **Einsatzgebiet** | **Algorithmus** |
|------------------|----------------|
| Straßennetzoptimierung | Kruskal |
| Computernetzwerke (STP-Protokoll) | Prim |
| Machine Learning (Clusteranalyse) | Kruskal |

---
## Anwendungsbilder 3D
### Nutzung der 3D-Modellierung mit einem n = 20
![MST_3D_n20](https://github.com/user-attachments/assets/4da10fc9-0a36-47e6-b4dc-f5e03e64ef1c)
### Nutzung der 3D-Modellierung mit einem n = 5
![MST_3D_n5](https://github.com/user-attachments/assets/f0f395b9-985d-4d46-acbf-d10f36854638)
## Anwendungsbilder 2D
### Nutzung der 2D-Modellierung mit einem n = 20
![MST_2D_n20](https://github.com/user-attachments/assets/b3513ac5-59aa-48e8-84d4-9f43ea5075c9)
### Nutzung der 2D-Modellierung mit einem n = 5
![MST_2D_n5](https://github.com/user-attachments/assets/3247dc5b-c3f6-465e-bfb6-471fb22af591)

