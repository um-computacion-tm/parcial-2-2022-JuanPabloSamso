class Compress:
    def __init__(self):
        pass

    def compress(self,text):
        texto = text
        words = texto.split(" ")
        dic = {}
        number = [dic.setdefault(word, len(dic)+1) for word in words]
        return number, dic

    def uncompress(self,number, dic):
        words = []
        for l in number:
            for j,k in dic.items():
                if k == number[l]-1:
                    words.append(j)
        texto = " ".join(words)
        return texto 