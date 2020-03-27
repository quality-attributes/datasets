import json

with open('../req_ner.json') as json_file:
    data = json.load(json_file)

unnecessary_tags = [
    "NATIONALITY",
    "NUMBER",
    "ORGANIZATION",
    "COUNTRY",
    "TIME",
    "STATE_OR_PROVINCE"
]

text = []

for i in range(len(data)):
    req_text = data[i]['text']
    if data[i]['labels']:
        for tag in data[i]['labels']:
            if tag[2] in unnecessary_tags:
                substitute = ''
                for i in range(len(req_text[tag[0]:tag[1]])):
                    substitute = substitute + ' '
                req_text = req_text.replace(req_text[tag[0]:tag[1]], substitute)
    text.append(' '.join(req_text.split()))



with open('../normalized.txt', 'w') as f:
    for line in text:
        f.write(line + '\n')


with open('../req_masked.json') as json_file:
    data = json.load(json_file)

text = []
sys_words = []
usr_words = []

for i in range(len(data)):
    req_text = data[i]['text']
    if data[i]['labels']:
        sys_words = []
        usr_words = []
        for tag in data[i]['labels']:
            if tag[2] == 'SYSTEM':
                sys_words.append(req_text[tag[0]:tag[1]])
            if tag[2] == 'USER':
                usr_words.append(req_text[tag[0]:tag[1]])
        for word in sys_words:
            req_text = req_text.replace(word, 'system')
        for word in usr_words:
            req_text = req_text.replace(word, 'user')
    text.append(' '.join(req_text.split()))

with open('../normalized.txt', 'w') as f:
    for line in text:
        f.write(line + '\n')
