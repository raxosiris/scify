import visualise_spacy_tree
from IPython.display import Image, display
from typing import Union
from spacy.tokens import Doc, Span

def tree_vis(doc: Union[Doc, Span]):
    png = visualise_spacy_tree.create_png(doc)
    return display(Image(png))