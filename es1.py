#togliere la parte non disponibile per dsa
pluvio= (
    ("milano", [("gennaio", 15),("febbraio", 12),("marzo",17),("aprile",10),("maggio",0),("giugno",5),("luglio",0),("agosto",17)]),
        ("roma", [("gennaio", 11),("febbraio", 0),("marzo",7),("aprile",15),("maggio",4),("giugno",5),("luglio",6),("agosto",13)])
        )

città=input("inserisce il nome di un capoluogo: ")
def tempo(città,pluvio):
    for nome,*dati in pluvio:
       
        somma=0
        cont=0
        max=0
        min=999
        meseMax=0
        meseMin=0
        if(città==nome):
            for mese in dati:
                for val in mese:
                    cont+=1
                    somma+=val[1]
                    if(val[1]<min):
                        min=val[1]
                        meseMin=mese[cont]
                    if(val[1]>max):
                        max=val[1]
                        meseMax=mese[cont]
                return(somma/cont,min,max,meseMin,meseMax)
tupla2=tempo(città,pluvio)
print("media precepitazione "+ città+" è di: "+str(tupla2[0]))
print("precepitazioni maggiore di "+ città+" è di : "+str(tupla2[2])+" nel mese: "+str(tupla2[4]))
print("precepitazioni minore di "+ città+" è di: "+str(tupla2[1])+" nel mese : "+str(tupla2[3]))


 

