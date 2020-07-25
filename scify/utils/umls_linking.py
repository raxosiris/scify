#!/usr/bin/env python
def link_to_UMLS(text: str, nlp, UMLS_linker):
    doc = nlp(text)
    entities = [entity for entity in doc.ents]
    entities_final = []
    if len(entities):
        umls_entries = [entity._.umls_ents[0] for entity in entities if len(entity._.umls_ents)]
        if len(umls_entries):
            linked_ents = [linker.umls.cui_to_entity[entity[0]] for entity in umls_entries]
            entities_final = [[entity.canonical_name, entity.definition] for entity in linked_ents]
    return entities_final



