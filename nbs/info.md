
# Info on Datasets and Linguistic Terms


## GNBR: GLOBAL NETWORK OF BIOMEDICAL RELATIONS

Example from distribution file. It has the dependency paths as keys and their support for a specific theme as value. The support is continous, not just a relation like "inhibit" or "upregulate". It is calculated by correlating a new sentence to a cluster of dependency paths.

```python
#it's very big but looks like this
distributions_kv_example = {"kinases|compound|START_ENTITY participate|nsubj|kinases participate|nmod|END_ENTITY": {'A+': 2.0,
  'A+.ind': 0.0,
  'A-': 0.0,
  'A-.ind': 0.0,
  'B': 0.0,
  'B.ind': 0.0,
  'E+': 0.0,
  'E+.ind': 0.0,
  'E-': 0.0,
  'E-.ind': 0.0,
  'E': 0.0,
  'E.ind': 0.0,
  'N': 0.0,
  'N.ind': 0.0,
  'O': 2.0,
  'O.ind': 0.0,
  'K': 0.0,
  'K.ind': 0.0,
  'Z': 0.0,
  'Z.ind': 0.0}}
```

`Support Legend from Paper:`

"""
Table 3.
Simplified relationship themes derived from the clusters shown in Figure 3a–d

Type	Symbol	Theme	Relevant figure	Supporting cluster(s)
Chemical-gene 
    A+ 	Agonism, activation 	3a 	6+ 
 	A− 	Antagonism, blocking 	 	6– 
 	B 	Binding, ligand (esp. receptors) 	 	14–16 
 	E+ 	Increases expression/production 	 	8+, 9+ 
 	E− 	Decreases expression/production 	 	8–, 9–, 10 
 	E 	Affects expression/production (neutral) 	 	8, 9, 11a 
 	N 	Inhibits 	 	3 
Gene-chemical 	O 	Transport, channels 	3a 	19, 21 
 	K 	Metabolism, pharmacokinetics 	 	11c 
 	Z 	Enzyme activity 	 	20 
Chemical-disease 	T 	Treatment/therapy (incl. investigatory) 	3b 	8g, 8h, 9 
 	C 	Inhibits cell growth (esp. cancers) 	 	2, 3 
 	Sa 	Side effect/adverse event 	 	6, 15, 16 
 	Pr 	Prevents, suppresses 	 	1, 9, 21, 24, 28 
 	Pa 	Alleviates, reduces 	 	26, 30 
 	J 	Role in pathogenesis 	 	20 
Disease-chemical 	Mp 	Biomarkers (progression) 	3b 	18, 19 
gene-disease 	U 	Causal mutations 	3c 	14 
 	Ud 	Mutations affect disease course 	 	13 
 	D 	Drug targets 	 	10, 12 
 	J 	Role in pathogenesis 	 	2h, 4, 6, 8, 9 
 	Te 	Possible therapeutic effect 	 	2j, 3 
 	Y 	Polymorphisms alter risk 	 	22, 26, 27 
 	G 	Promotes progression 	 	29 
Disease-gene 	Md 	Biomarkers (diagnostic) 	3c 	5, 7 
 	X 	Overexpression in disease 	 	15, 17, 30 
 	L 	Improper regulation linked to disease 	 	18, 19, 21 
Gene–gene 	B 	Binding, ligand (esp. receptors) 	3d 	10 
 	W 	Enhances response 	 	13 
 	V+ 	Activates, stimulates 	 	14, 16 
 	E+ 	Increases expression/production 	 	21, 22 
 	E 	Affects expression/production (neutral) 	 	7, 17 
 	I 	Signaling pathway 	 	24 
 	H 	Same protein or complex 	 	25 
 	Rg 	Regulation 	 	28, 30 
 	Q 	Production by cell population 	 	1, 2, 6 
"""


