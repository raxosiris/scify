from typing import List
from collections import defaultdict


def check_for_non_trees(dependency_triples: List[List[str]]):
    """
    A utility function which checks:

    1. The dependency triples you pass in are not self referential
    2. The triples you pass in form a single tree, with one root.
    3. There are no loops in the triples you pass in.

    # Parameters
    dependency_triples: List[List[str]]
        A list of [parent, relation, child] triples, which together
        form a tree that we would like to match on.

    # Returns
    root: str
        The root of the subtree
    parent_to_children: Dict[str, List[Tuple[str, str]]]
        A dictionary mapping parents to a list of their children,
        where the child is represented as a (relation, child) tuple.
    """

    parent_to_children = defaultdict(list)
    seen = set()
    has_incoming_edges = set()
    for (parent, rel, child) in dependency_triples:
        seen.add(parent)
        seen.add(child)
        has_incoming_edges.add(child)
        if parent == child:
            return None, None
        parent_to_children[parent].append((rel, child))

    # Only accept strictly connected trees with a single root.
    roots = seen.difference(has_incoming_edges)
    if len(roots) != 1:
        return None, None

    root = roots.pop()
    seen = {root}

    # Step 2: check that the tree doesn't have a loop:
    def contains_loop(node):
        has_loop = False
        for (_, child) in parent_to_children[node]:
            if child in seen:
                return True
            else:
                seen.add(child)
                has_loop = contains_loop(child)
            if has_loop:
                break

        return has_loop

    if contains_loop(root):
        return None, None

    return root, parent_to_children


def add_node(parent: str, pattern: List, parent_to_children: defaultdict):
    pattern_copy = pattern.copy()
    info = parent_to_children[parent]
    if (len(info) ==  0):
        return pattern_copy
    for (rel, child) in info:
        # First, we add the specification that we are looking for
        # an edge which connects the child to the parent.
        node = {
            "SPEC": {
                "NODE_NAME": child,
                "NBOR_RELOP": ">",
                "NBOR_NAME": parent
                }
        }
        # We want to match the relation exactly.
        token_pattern = {"DEP": rel}

        # Because we're working specifically with relation extraction
        # in mind, we'll use START_ENTITY and END_ENTITY as dummy
        # placeholders in our list of triples to indicate that we want
        # to match a word which is contained within an entity (or the
        # entity itself if you have added the merge_entities pipe
        # to your pipeline before running the matcher).
        if child not in {"START_ENTITY", "END_ENTITY"}:
            token_pattern["ORTH"] = child
        else:
            token_pattern["ENT_TYPE"] = {"NOT_IN": [""]}

        node["PATTERN"] = token_pattern

        pattern_copy.append(node)
        return add_node(child, pattern_copy, parent_to_children)


root, parent_to_children = check_for_non_trees(examples)
pattern = [{"SPEC": {"NODE_NAME": root}, "PATTERN": {"ORTH": root}}]

if root is None:
    print("root is none")     



new_pattern = add_node(root, pattern, parent_to_children)
t = 5