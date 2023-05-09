def negate_literal(literal):
    """Return the negation of a propositional literal."""
    if literal.startswith('~'):
        return literal[1:]
    else:
        return '~' + literal


def resolve(s1, s2):
    """Apply the resolution rule to two propositional logic sentences."""
    for literal in s1:
        if negate_literal(literal) in s2:
            s3 = list(set(s1) | set(s2)) # joining s1 and s2
            s3 = [l for l in s3 if l != literal and l != negate_literal(literal)] # deleting from s3 literal l
            return s3
    return None


def simplify(sentence):
    """Simplify a propositional logic sentence by removing redundant literals."""
    for i in range(len(sentence)):
        if negate_literal(sentence[i]) in sentence[:i]:
            return ['TRUE'] # True
    return list(set(sentence))


def to_remove(resolvent, old_sentences):
    """Removes weaker sentences from KB."""
    for i in range(len(old_sentences)):
        if set(old_sentences[i]).issubset(set(resolvent)): # if new derived sentence is weaker than already existed sentence
            return True
    return False


def derive_new_sentences(kb):
    """Derive all possible sentences that can be inferred from a knowledge base."""
    all_sentences = [s for s in kb]
    parent_indexes = [[] for _ in range(len(kb))]
    i = 0
    while i in range(len(all_sentences)):
        for j in range(0, len(all_sentences)):
            resolvent = resolve(all_sentences[i], all_sentences[j])
            if resolvent is not None:
                resolvent = simplify(resolvent)
                if resolvent != ['TRUE'] and resolvent not in all_sentences and to_remove(resolvent, all_sentences) == False:
                    all_sentences.append(resolvent)
                    parent_indexes.append([i, j])
        i += 1
    return all_sentences, parent_indexes