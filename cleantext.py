import re
import string

def clean_text(text):
    text = re.sub('<.*?>', '', text)

    text = re.sub(r'\[\[[^]]*\]\]', '', text) # Get rid of [[ ]]
    text = re.sub(r'\[[^]]*\]', '', text)   #   Or [ ]

    text = re.sub(r'\{\{[^}]*\}\}', '', text)
    text = re.sub(r'\{[^}]*\}', '', text)

    text = re.sub(r'\(\([^)]*\)\)', '', text)
    text = re.sub(r'\([^)]*\)', '', text)

    text = re.sub(r'\=\=([^\=]*)\=\=', '', text)#   == ==
    text = re.sub(r'\<!--[^>]*\-->', '', text)# <!-- -->
    text = re.sub(r'(?m)^\*.*\n?', '', text)# *
    text = re.sub(r'(?m)^\=.*\n?', '', text)# =
    text = re.sub(r'(?m)^#.*\n?', '', text) # Lines with #
    text = re.sub(r'(?m)^\|.*\n?', '', text) # Lines with or symbol
    text = re.sub(r'(?m)^\s\|.*\n?', '', text)  # Lines with or symbol after whitespace



    text = re.sub(r'(?m)^from:.*\n?', '', text) #Lines starting with from:
    text = re.sub(r'(?m)^Resim:.*\n?', '', text)
    text = re.sub(r'(?m)^Dosya:.*\n?', '', text)
    text = re.sub(r'(?m)^!.*\n?', '', text)
    text = re.sub(r'(?m)^::.*\n?', '', text)
    text = re.sub(r'(?m)^;.*\n?', '', text)

    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()


    #text = ''.join(ch for ch in text if ch not in exclude)
    return text
