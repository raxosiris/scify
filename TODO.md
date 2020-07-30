# TODO
[x] fix entity shift in char offset

[x] merge entities yeah

[x] put utils in .py files. I hate those long Jupyter notebooks with their uncomposable trash python code all over the place 

[ ] Fix error in merge_file thing

[ ] serialize and deserialize utils

[ ] can use multiple labels (since all are in entity._.kb_ents {bc5, jnlpa...}

[ ] Add more annotations as extension create product(UMLS, MESH, ontologies) X (models) annotated file from pubmed abstracts to not always load everything from scratch

[ ] slowly create multi-model NER annotated datasets to easy sample and do experiments on

[ ] look at source code for kindred, scipacy, role_pattern_nlp and adapt utils

[ ] EDA on corpus level stats and word-trees

[ ] Performance of merge_docs is horrid and not really by concept sensitivity (overwrite ranking)

[ ] Understand how to have a REBL, REPL or DATA VIEW in Python....
#TODO
#token -> char overlap in merge_docs
#document level matching %
#sentence level matching %
#performance?

#get_shortest_path between ents
#find pattern matches
#dependency pattern + pattern matcher on GNBR --> relation extraction precision?
TODO
1) isEntity in Sentence?
2) Shortest Path -> SP
3) compare with theme in GNBR

## Advanced (Later)

#try
  #as_doc() on a Span object (https://spacy.io/api/span#as_doc):

[ ] Implement custom spacy pipelines and knowledge linking/ knowledge bases https://stackoverflow.com/questions/51412095/spacy-save-custom-pipeline
