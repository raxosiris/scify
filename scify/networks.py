from itertools import combinations, permutations
from functools import reduce
from typing import List, Tuple, Union
from spacy.tokens import Token, Doc, Span
import networkx as nx

# Load spacy's dependency tree into a networkx graph
def get_edges(doc: Union[Doc, List[Span]]):
    """Use get_edges_unique if you want object +id"""
    edges = []

    for token in doc:
        for child in token.children:
            edges.append((token, child))
    return edges

def get_edges_unique(doc: Union[Doc, List[Span]]):
    """"""
    edges = []

    for token in doc:
        for child in token.children:
            #if you want text instead of actual object!
            #edges.append(('{0}-{1}'.format(token.text, token.i),
            #'{0}-{1}'.format(child.text, child.i)))

            edges.append(((token, token.i), (child, child.i)))
    return edges

def get_verb(tokens: List[Token]):
    for token in tokens:
        if token.pos_ == "VERB":
            return token
    
#TODO either make a dict or read context off of tokens later
def triples_from_pairs(pairs: List[Tuple[Doc, Doc]], G, doc:Doc, relation_fn=get_verb):
    """takes two entities and finds a relation between them (relation_fn) looking at the 
    shortest path. Edit: Too simple. Instead of assuming it's the verb, lookup in the dependency patterns (GNBR)"""
    triples = []      
    for pair in pairs:
        i1, i2 = pair
        source, target = doc[i1], doc[i2]        
        SDP = nx.shortest_path(G, source, target) #previous issue: we pass networkx the tokens, but when we give .ents ... we have spans and it doesn't recognize
        relation = relation_fn(SDP)
        if (relation):
            triples = triples + [(relation, source, target)]
    return triples




def is_redundant(value, store): 
    mirror = (value[1], value[0])
    is_same = value[1] is value[0]
    return (is_same  or (value in store) or (mirror in store))


def pair_down(all_pairs):
    token_str = [(str(t[0]), str(t[1])) for t in all_pairs] #easier to compare str than tokens
    dist = []
    for value in token_str:
        #print(dist, value)
        if is_redundant(value, dist):
            value = False
        dist = dist + [value]

    return [pair for idx, pair in enumerate(all_pairs) if dist[idx] != False]