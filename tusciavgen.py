import markovify 
import csv
with open("tusciaweb.csv", "r",encoding="utf-8",newline="") as f:
    corpus=f.read()
tusciamodel=markovify.NewlineText(corpus)
with open("tusciav.txt","w",encoding="utf-8") as out:

    for i in range(1000):
        out.write(tusciamodel.make_sentence()+"\n")
        

