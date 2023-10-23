import string
import codecs
import pandas as pd

def extract_words(data, split) -> list:
    """
    A function that split a string and return the word before the split variable
    Example: "we are the best friends and the friends are the best"
    if the split = "friends" we will get [best,the]
    """
    il = [i for i, x in enumerate(data.translate(str.maketrans("","")).split()) if x == split]
    res = [data.split()[x-1] for x in il]
    return res

ABECEDARIO_1 = list(string.ascii_lowercase)
ABECEDARIO_2 = list(string.ascii_lowercase)

df = pd.read_html('http://www.portaldalinguaportuguesa.org/advanced.php?action=browse&l1=a&l2=a',header=0)[7]
df = df.iloc[: , 3:]
data = df.columns[0]


for x in ABECEDARIO_1:
    for y in ABECEDARIO_2:
        df = pd.read_html(f'http://www.portaldalinguaportuguesa.org/advanced.php?action=browse&l1={x}&l2={y}',header=0)[7]
        df = df.iloc[: , 3:]
        data = df.columns[0]
        res = extract_words(data,'-')
        if len(res) != 0:
            with codecs.open(f"./WordList/{x}.txt", "a","utf-8") as w:
                w.write('\n'.join(res) + '\n')
            with  codecs.open("wordlist.txt","a","utf-8") as wa:
                wa.write('\n'.join(res) + '\n')
        else:
            print(f'http://www.portaldalinguaportuguesa.org/advanced.php?action=browse&l1={x}&l2={y}')