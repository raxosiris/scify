def add_node_old(parent: str, pattern: List, parent_to_children: defaultdict):
    """ Refactored now"""
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
        return add_node_old(child, pattern_copy, parent_to_children)
    


def construct_pattern_old(dependency_triples: List[List[str]]):
    """
    Idea: add patterns to a matcher designed to find a subtree in a spacy dependency tree.
    Rules are strictly of the form "Parent --rel--> Child". To build this up, we add rules
    in DFS order, so that the parent nodes have already been added to the dict for each child
    we encounter.

    # Parameters
    dependency_triples: List[List[str]]
        A list of [parent, relation, child] triples, which together
        form a tree that we would like to match on.

    # Returns
    pattern:
        A json structure defining the match for the given tree, which
        can be passed to the spacy DependencyMatcher.

    """
    # Step 1: Build up a dictionary mapping parents to their children
    # in the dependency subtree. Whilst we do this, we check that there is
    # a single node which has only outgoing edges.
    root, parent_to_children = check_for_non_trees(dependency_triples)
    if root is None:
      return None
    pattern = [{"SPEC": {"NODE_NAME": root}, "PATTERN": {"ORTH": root}}]
    return add_node_old(root, pattern, parent_to_children)
