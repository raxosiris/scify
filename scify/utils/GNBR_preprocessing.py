import os
import asyncio
from typing import Dict, List, Union

DATA_PATH = "../data/biomedrel/"

PTB_BRACKETS = {
    
    "-LRB-": "(",
    "-RRB-": ")",
    "-LCB-": "{",
    "-RCB-": "}",
    "-LSB-": "[",
    "-RSB-": "]",
}

class GNBR():
    @staticmethod
    def get_data_and_distributions(DIR_PATH=DATA_PATH):
        with open(DIR_PATH + "part-i-chemical-gene-path-theme-distributions.txt", "r") as f:
            l = f.readlines() #bad and inefficient....
            headers = l[1].strip().split("\t")[1:]
            #headers = next(f).strip().split("\t")[1:] --this did return [] most of the time
            print(headers, 'headers', """
            chemical-gene
    (A+) agonism, activation
    (A-) antagonism, blocking
    (B) binding, ligand (esp. receptors)
    (E+) increases expression/production
    (E-) decreases expression/production
    (E) affects expression/production (neutral)
    (N) inhibits
            """)
            distributions = {}
            #incredibly dumb way of doing this because the fileread IO is buggy or just bad
            for line in l[2:]:
                line = line.strip().split("\t")
            
                distributions[line[0]] = {name: float(value) for name, value in zip(headers, line[1:])}
            
            with open(DIR_PATH + "part-ii-dependency-paths-chemical-gene-sorted-with-themes.txt", "r") as data:
                data_headers = ["pmid", "sent", "ent1", "ent1_offset", "ent2", "ent2_offset",
                                "ent1_raw", "ent2_raw", "ent1_canonical", "ent2_canonical", 
                                "ent1_type", "ent2_type", "dep", "sent"]

                lines = [{k:v for k,v in zip(data_headers, line.strip().split("\t"))} for line in data]
            
        return lines, distributions
    @staticmethod
    def clean_and_parse(sent: str, nlp, PTB_BRACKETS=PTB_BRACKETS):
        """ -LRB- something -RRB- ===> (something) """
        tokens = sent.strip().split(" ")

        new = []
        for token in tokens:
            new_token = PTB_BRACKETS.get(token, None)
            if new_token is None:
                new.append(token)
            else:
                new.append(new_token)
        return nlp(" ".join(new))

    def unambigous_support(support: Dict)->bool:
        """Is the support mixed for many themes or pretty focused?"""
        return max(support)/sum(support) > 0.8
    @property
    def THEMES():
        return """
                Chemical-gene 	
                    A+ 	Agonism, activation 	                        3a 	6+ 
                    A− 	Antagonism, blocking 	 	                    6– 
                    B 	Binding, ligand (esp. receptors) 	 	        14–16 
                    E+ 	Increases expression/production 	 	        8+, 9+ 
                    E− 	Decreases expression/production 	 	        8–, 9–, 10 
                    E 	Affects expression/production (neutral) 	 	8, 9, 11a 
                    N 	Inhibits 	 	                                3 
                Gene-chemical 	
                    O 	Transport, channels 	                        3a 	19, 21 
                    K 	Metabolism, pharmacokinetics 	 	            11c 
                    Z 	Enzyme activity 	 	                        20 
                Chemical-disease 	
                    T 	Treatment/therapy (incl. investigatory) 	    3b 	8g, 8h, 9 
                    C 	Inhibits cell growth (esp. cancers) 	 	    2, 3 
                    Sa 	Side effect/adverse event 	 	                6, 15, 16 
                    Pr 	Prevents, suppresses 	 	                    1, 9, 21, 24, 28 
                    Pa 	Alleviates, reduces 	 	                    26, 30 
                    J 	Role in pathogenesis 	 	                    20 
                Disease-chemical 	
                    Mp 	Biomarkers (progression) 	                    3b 	18, 19 
                Gene-disease 	
                    U 	Causal mutations 	                            3c 	14 
                    Ud 	Mutations affect disease course 	 	        13 
                    D 	Drug targets 	 	                            10, 12 
                    J 	Role in pathogenesis 	 	                    2h, 4, 6, 8, 9 
                    Te 	Possible therapeutic effect 	 	            2j, 3 
                    Y 	Polymorphisms alter risk 	 	                22, 26, 27 
                    G 	Promotes progression 	 	                    29 

                Disease-gene 	Md 	Biomarkers (diagnostic) 	        3c 	5, 7 
                    X 	Overexpression in disease 	 	                15, 17, 30 
                    L 	Improper regulation linked to disease 	 	    18, 19, 21

                Gene–gene 	B 	Binding, ligand (esp. receptors) 	    3d 	10 
                    W 	Enhances response 	 	                        13 
                    V+ 	Activates, stimulates 	 	                    14, 16 
                    E+ 	Increases expression/production 	 	        21, 22 
                    E 	Affects expression/production (neutral) 	 	7, 17 
                    I 	Signaling pathway 	 	                        24 
                    H 	Same protein or complex 	 	                25 
                    Rg 	Regulation 	 	                                28, 30 
                    Q 	Production by cell population 	 	            1, 2, 6
                """

    @staticmethod
    def parse_dep_path(dep_string: str):

        rules = [rule.split("|") for rule in dep_string.split(" ")]

        for triple in rules:

            if triple[0] in PTB_BRACKETS:
                triple[0] = PTB_BRACKETS[triple[0]]

            if triple[2] in PTB_BRACKETS:
                triple[2] = PTB_BRACKETS[triple[2]]

            if triple[1] == "nsubj:xsubj":
                triple[1] = "nsubj"

            if triple[1] == "nsubjpass:xsubj":
                triple[1] = "nsubjpass"
        return rules
#PBT - like random search - starts by training many neural networks in parallel with random hyperparameters. But instead of the networks training independently, it uses information from the rest 
#of the population to refine the hyperparameters and direct computational resources to models which show promise.


