import os
import asyncio

DATA_PATH = "../data/biomedrel/"

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

#PBT - like random search - starts by training many neural networks in parallel with random hyperparameters. But instead of the networks training independently, it uses information from the rest 
#of the population to refine the hyperparameters and direct computational resources to models which show promise.
PTB_BRACKETS = {
    
    "-LRB-": "(",
    "-RRB-": ")",
    "-LCB-": "{",
    "-RCB-": "}",
    "-LSB-": "[",
    "-RSB-": "]",
}

def clean_and_parse(sent: str, nlp):
    tokens = sent.strip().split(" ")

    new = []
    for token in tokens:
        new_token = PTB_BRACKETS.get(token, None)
        if new_token is None:
            new.append(token)
        else:
            new.append(new_token)
    return nlp(" ".join(new))


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