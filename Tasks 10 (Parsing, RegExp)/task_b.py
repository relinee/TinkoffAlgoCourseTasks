import re


def simplify(text):
    # Удаление артиклей
    text = re.sub(r'\b[aA]\b|\b[aA]n\b|\b[tT]he\b', r'', text)
    # Замена буквы 'c'
    tmp = 0
    while tmp != len(text):
        tmp = len(text)
        text = re.sub(r'(C)i', 'Si', text)
        text = re.sub(r'(C)e', 'Se', text)
        text = re.sub(r'(c)i', 'si', text)
        text = re.sub(r'(c)e', 'se', text)
        text = re.sub(r'(C)k', 'K', text)
        text = re.sub(r'(c)k', 'k', text)
        text = re.sub(r'c', 'k', text)
        text = re.sub(r'C', 'K', text)
    # Удаление удвоенных букв
    tmp = 0
    while tmp != len(text):
        tmp = len(text)
        text = re.sub(r'Ee', 'I', text)
        text = re.sub(r'ee', 'i', text)
        text = re.sub(r'Oo', 'U', text)
        text = re.sub(r'oo', 'u', text)
        text = re.sub(r'(?i)(\w)\1', r'\1', text)
    # Опускание буквы 'e' в конце слова
    text = re.sub(r'\b(\w+)(e)\b', r'\1', text)
    text = text.replace("  ", " ")
    return text


text = input()

print(simplify(text))

