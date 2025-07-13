f = open("C://Users//jassi//Documents//Python//py for ml//funny.txt","r")
f_out = open("C://Users//jassi//Documents//Python//py for ml//funny_wc.txt","w")
for line in f:
    tokens = line.split(' ')
    f_out.write(" wordcount:"+str(len(tokens))+line)

f.close()
f_out.close() 