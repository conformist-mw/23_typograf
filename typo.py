import re
# Chars
ndash = '–'
nbsp = '\u00A0'


def replace_quotes(text):
    return re.sub(r'([\'"])(.*?)(\1)', r'«\2»', text)


def replace_hyphen(text):
    text = re.sub(r'\b(\w{3,5})\s?[-—]\s?(\w{2})\b', r'\1-\2', text)
    text = re.sub(r'\s-\s', r' — ', text)
    return text


def handle_phones(text):
    phone = re.compile(
        r'[\+\(]?(\d)[-\s+\(]?(\d{2,3})[-\s+\)]?\s?'
        r'(\d{2,3})[-\s]?(\d{1,3})[-\s]?(\d+)')
    return phone.sub(r'\1(\2)\3{0}\4{0}\5'.format(ndash), text)


def remove_extra_spaces(text):
    text = re.sub(r'\r\n', r'\n', text)
    text = re.sub(r'\n{2,}', r'\n', text)
    text = re.sub(r'[ \t]{2,}', r' ', text)
    return text


def number_with_words(text):
    text = re.sub(r'(\d+[.,]?\d+)\s?([€$\w]+)', r'\1{}\2'.format(nbsp), text)
    text = re.sub(r'[^0-9]([а-яА-Я.]+)\s?(\d+)', r' \1{}\2'.format(nbsp), text)
    return text


def small_units_handle(text):
    text = re.sub(r'\b([\w]{1,2}\s+)\b', r'\1{}'.format(nbsp), text)
    return text


def typo(text):
    text = replace_hyphen(text)
    text = replace_quotes(text)
    text = handle_phones(text)
    text = remove_extra_spaces(text)
    text = number_with_words(text)
    text = small_units_handle(text)
    return text
