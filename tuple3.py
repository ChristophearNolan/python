prezzo_prodotti=(("mela","lunedi",1.0),
                 ("mela","martedi",1.2),
                 ("mela","mercoledi",1.1),
                 ("banana","lunedi",0.8),
                 ("banana","martedi",0.9),
                 ("banana","mercoledi",0.7))
g=input("inserisci un giorno ")
p=input("insersci un prodotto ")
def prezzo_medio(g,p,prezzo_prodotti):
    x=0
    somma=0
    
    for prodotti,giorni,prezzi in prezzo_prodotti:
        if(giorni==g and prodotti==p):
            x+=1
            somma+=prezzi
    if(x>0):
            media=somma/x
            return media
    else:
        return("prodotto non presente")
        

print("il prezzo medio del prodotto",p," nel giorno di",g," è di "+str(prezzo_medio(g,p,prezzo_prodotti)))





