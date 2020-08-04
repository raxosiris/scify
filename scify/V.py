import visualise_spacy_tree
from IPython.display import Image, display, IFrame, HTML
from spacy.tokens import Doc, Span, Token
import spacy
from typing import Dict, Any, Union, List
import json
import os
from spacy import displacy

class V:
    """
    Static Methods for Visualizing Docs, Spans and Sentences
    """

    def __init__(self) -> None:
        return
    
    @staticmethod
    def tree(doc: Union[Doc, Span]):
        png = visualise_spacy_tree.create_png(doc)
        return display(Image(png))

    @staticmethod
    def hierplane(sent, temp_file="temp.html"):
        """Interactive visualization of the Sentence dependency hierarchy. Hierplane is a AllenAI Component"""
        print("heelo")
        #nbs_path = "../nbs/" + temp_file
        tree = dict(build_hierplane_tree(sent))
        tree_json = json.dumps(tree, sort_keys=True)
        html = """
        <!DOCTYPE html><html>
    <head>
        <title>Hierplane!</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.css">
        <script src="https://unpkg.com/hierplane@0.2.1/dist/static/hierplane.min.js"></script>
        </head>
    <body>
        <script>
        
        hierplane.renderTree(JSON.parse(JSON.stringify({tree_json})));
        </script>
    </body>
    </html>""".format(tree_json=tree_json) 

        #because working with files is hard and Iframe only takes paths
        with open(temp_file, "w") as h:
            h.write(html)
        #at the server
        #with open("../temp_file_vis.json", "w+") as f:
        #  f.write(json.dumps(tree,sort_keys=True))
        #print("Connecting to localhost for vis_server (you have to run one first)....because jupyter and HTML is buggy")
        #return HTML(html)


        #print(os.path.abspath(os.getcwd()), "path")
        return IFrame(src=temp_file, width='100%', height='500px')
    
    @staticmethod
    def visualise_doc(doc:Doc, compact=False):
        displacy.render(doc, style="dep", options={"distance": 120, "compact":compact}, jupyter=True)
        displacy.render(doc, style="ent", options={"distance": 120}, jupyter=True)
    
    @staticmethod
    def visualise_subtrees(doc:Doc, subtrees: List[int]):
        """Only visualize the dependencies in the subtrees
        Adapted from code of Mark Neumann
        """
        words = [{"text": t.text, "tag": t.pos_} for t in doc]

        if not isinstance(subtrees[0], list):
            subtrees = [subtrees]

        for subtree in subtrees:
            arcs = []

            tree_indices = set(subtree)
            for index in subtree:

                token = doc[index]
                head = token.head
                if token.head.i == token.i or token.head.i not in tree_indices:
                    continue

                else:
                    if token.i < head.i:
                        arcs.append(
                            {
                                "start": token.i,
                                "end": head.i,
                                "label": token.dep_,
                                "dir": "left",
                            }
                        )
                    else:
                        arcs.append(
                            {
                                "start": head.i,
                                "end": token.i,
                                "label": token.dep_,
                                "dir": "right",
                            }
                        )
            print("Subtree: ", subtree)
            displacy.render(
                {"words": words, "arcs": arcs},
                style="dep",
                options={"distance": 120},
                manual=True,
                jupyter=True
            )

def build_hierplane_tree(tree: Span) -> Dict[str, Any]:
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
  