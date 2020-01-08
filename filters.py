from jinja2 import Markup
import re

def embolden(string, keyword):
    """Jinja filter to make bold keyword in string with <strong> tags"""

    # print(type(string))
    # words_to_change = []

    # # find keyword
    # for word in string.split(): # returns list of jinja2.Markup objects
    #     if word.lower() == Markup(keyword.lower()):

    #         if word not in words_to_change:
    #             words_to_change.append(word)

    # # print(string.split()[:20])
    # #print(string)
    # # add <strong> tags
    # for word in words_to_change:
    #     string = string.replace(word, Markup(f'<strong style="background-color: yellow;"><u>{word}</u></strong>'))
    
    matches = re.findall(f'(?i){keyword}', string, flags=re.I)
    string = re.sub(f'(?i){keyword}', Markup(f'<span style="background-color: yellow;">{keyword}</span>'), string)

    return Markup(string)


def format_hs(hscode: str) -> str:
    """input: 10 digit string representing HS code\nreturns string of length 13 with 3 dots added to HS code for better readability"""
    out = hscode[:4]

    if not hscode.isdigit():
        return hscode

    if len(hscode) == 4:
        return f"{hscode[:2]}.{hscode[2:]}"

    if len(hscode) == 6:
        return f"{hscode[:4]}.{hscode[4:]}"

    if len(hscode) == 8:
        return f"{hscode[:4]}.{hscode[4:6]}.{hscode[6:]}"

    if len(hscode) == 10:
        return f"{hscode[:4]}.{hscode[4:6]}.{hscode[6:8]}.{hscode[8:]}"
    return ""