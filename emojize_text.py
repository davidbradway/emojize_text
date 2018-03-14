import emoji
import re

def emojize_text(string: str) ->str:
    # put colons around all the words
    colons: str = re.sub(r'(\w*)', r':\1:', string)
    # put in emoji
    s: str = emoji.emojize(string=colons, use_aliases=True)
    # take out colons
    nocolons: str = re.sub(r':(\w*):', r'\1', s)
    return nocolons

if __name__ == '__main__':
    long: str = ' '.join(['hot chicken, four dollar toast, Deep v pop-up, squid, gluten-free,',
       'narwhal food truck. cloud bread. man bun, coloring book, cold-pressed church-key',
       'cardigan put a bird on it, 8-bit wolf, craft beer. Single-origin coffee.'])

    nocolons: str = emojize_text(long)
    print(nocolons)
    print(emoji.demojize(nocolons)) # for Python 3.x
