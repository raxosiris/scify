from operator import eq, ge, le

PARAMS = {
    
    "LEN_TRESH": 15,
    "SUBTREE_LEN_TRESH": 6,
    
}

SPACY_DEPS = {'ROOT', 'acl', 'acl:relcl','advcl','advmod','amod','appos','aux','auxpass','case','cc','cc:preconj','ccomp',
              'compound','compound:prt','conj','cop','csubj','csubjpass','dep','det','det:predet','dobj','expl','iobj','list',
              'mark','mwe','neg','nmod','nmod:npmod','nmod:poss','nmod:tmod','nsubj','nsubjpass','nummod','parataxis','punct','xcomp'}

labels = { #[get_label_candidates_from_entity(ent) for ent in corp[8].ents if len(ent._.annotated)]
'AMINO_ACID',
 'ANATOMICAL_SYSTEM',
 'CANCER',
 'CELL',
 'CELLULAR_COMPONENT',
 'CELL_LINE',
 'CELL_TYPE',
 'CHEBI',
 'CHEMICAL',
 'CL',
 'DEVELOPING_ANATOMICAL_STRUCTURE',
 'DISEASE',
 'DNA',
 'GENE_OR_GENE_PRODUCT',
 'GGP',
 'GO',
 'IMMATERIAL_ANATOMICAL_ENTITY',
 'MULTI-TISSUE_STRUCTURE',
 'ORGAN',
 'ORGANISM',
 'ORGANISM_SUBDIVISION',
 'ORGANISM_SUBSTANCE',
 'PATHOLOGICAL_FORMATION',
 'PROTEIN',
 'RNA',
 'SIMPLE_CHEMICAL',
 'SO',
 'TAXON',
 'TISSUE'
}
texts = [
    
]