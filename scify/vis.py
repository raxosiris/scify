import visualise_spacy_tree
from IPython.display import Image, display
from typing import Union
from spacy.tokens import Doc, Span, Token
import spacy
from typing import Dict, Any

def build_hierplane_tree(tree: spacy.tokens.Span) -> Dict[str, Any]:
    """
    After some search, I found this conversion in Mark Neumann's https://github.com/DeNeutoy/spacy-vis/blob/master/displacy/app.py

    There is another Fn that can convert NLTK trees (ala AMR/LISPy) into the same JSON struct
    Returns
    -------
    A JSON dictionary render-able by Hierplane for the given tree.
    """
    if isinstance(tree, Doc):
        #print("hi!")
        raise ValueError("Input has to be a Span: A sentence, not the whole doc, (can be changed, but the function uses .root which doc doesn't have TODO")
    def node_constuctor(node: Token):
        children = []
        for child in node.children:
            children.append(node_constuctor(child))

        span = node.text
        # These character spans define what word is highlighted
        # by Hierplane. For intermediate nodes, the spans
        # are composed and the union of them is highlighted.
        char_span_start = tree[node.i: node.i + 1].start_char
        char_span_end = tree[node.i: node.i + 1].end_char

        # These are the icons which show up in the bottom right
        # corner of the node. We can add anything here,
        # but for brevity we'll just add NER and a few
        # other things.
        attributes = [node.pos_]

        if node.ent_iob_ == "B":
            attributes.append(node.ent_type_)

        if node.like_email:
            attributes.append("email")
        if node.like_url:
            attributes.append("url")

        hierplane_node = {
                "word": span,
                # The type of the node - all nodes with the same
                # type have a unified colour.
                "nodeType": node.dep_,
                # Attributes of the node, eg PERSON or "email".
                "attributes": attributes,
                # The link between  the node and it's parent.
                "link": node.dep_,
                # The span to highlight in the sentence.
                "spans": [{"start": char_span_start,
                           "end": char_span_end}]
        }
        if children:
            hierplane_node["children"] = children
        return hierplane_node

    hierplane_tree = {
            "text": str(tree),
            "root": node_constuctor(tree.root)
    }
    return hierplane_tree


def tree_vis(doc: Union[Doc, Span]):
    png = visualise_spacy_tree.create_png(doc)
    return display(Image(png))