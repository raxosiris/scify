#Doc.set_extension('my_ents', default=None)

#add to pipeline (for multiple docs...merging)
def move_ents_to_attr(doc:Doc, attr_name:str)->Doc:
    if doc._.my_ents is None:
        doc._.my_ents = []
    doc._.my_ents.extend(doc.ents)
    doc.ents = []
    return doc