#Doc.set_extension('my_ents', default=None)

#add to pipeline (for multiple docs...merging)
def move_ents_to_attr(doc:Doc, attr_name:str)->Doc:
    if doc._.my_ents is None:
        doc._.my_ents = []
    doc._.my_ents.extend(doc.ents)
    doc.ents = []
    return doc


TRIGGERS = {
    "causal": [], #biocause paper ~10 phrases
}

def discourse_section(abstract)->str: #conclusion, intro, etc.
    return

def pattern_from_shortest_dep_path():
    5

#candidates: show_negex_entities
def has_trigger_spans(triggers = TRIGGERS["causality"])->bool:
    """pre-parsing filter to focus on good candidates"""
    return "TODO"
