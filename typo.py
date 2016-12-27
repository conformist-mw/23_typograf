import re
# Chars
nbsp = '\u00A0'

patterns = [
    # handle quotes
    (r'([\'"])(.*?)(\1)', r'«\2»'),
    # replace dash within short words with hyphen
    (r'\b(\w{3,5})\s?[-—]\s?(\w{2})\b', r'\1-\2'),
    # replace hyphen with dash
    (r'\s-\s', r' — '),
    # remove win-like newlines
    (r'\r\n', r'\n'),
    # replace extra newlines
    (r'\n{2,}', r'\n'),
    # remove tabs
    (r'\t', r' '),
    # remove extra spaces
    (r'[ ]{2,}', r' '),
    # words followed by numbers
    (r'(\d+[.,]?\d+)\s?([€$\w]+)', r'\1{}\2'.format(nbsp)),
    # handle phone numbers
    (r'\b[\+\(]?(\d)[-\s+\(]?(\d{2,3})[-\s+\)]?\s?'
        r'(\d{2,3})[-\s]?(\d{1,3})[-\s]?(\d+)\b', r'\1(\2)\3–\4–\5'),
    # numbers followed by words
    (r'[^0-9]([а-яА-Яa-zA-Z.]+)\s?(\d+)', r' \1{}\2'.format(nbsp)),
    # short words followed by nbsp
    (r'\b([\w]{1,2}\s+)\b', r'\1{}'.format(nbsp)),
]


def typo(text):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text
