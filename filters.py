from jinja2 import Markup

def embolden(string, keyword):
    """Jinja filter to make bold keyword in string with <strong> tags"""

    words_to_change = []

    # find keyword
    for word in string.split(): # returnsn list of jinja2.Markup objects
        if word.lower() == Markup(keyword.lower()):

            if word not in words_to_change:
                words_to_change.append(word)

    # add <strong> tags
    for word in words_to_change:
        string = string.replace(word, Markup(f"<strong>{word}</strong>"))
    
    return string