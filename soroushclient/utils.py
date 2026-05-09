from soroushclient.helpers import add_surrogate, del_surrogate


def get_inner_text(text, entities):
    """
    Gets the inner text that's surrounded by the given entities.
    For instance: text = 'hey!', entity = MessageEntityBold(2, 2) -> 'y!'.

    :param text:     the original text.
    :param entities: the entity or entities that must be matched.
    :return: a single result or a list of the text surrounded by the entities.
    """
    text = add_surrogate(text)
    result = []
    for e in entities:
        start = e.offset
        end = e.offset + e.length
        result.append(del_surrogate(text[start:end]))

    return result
