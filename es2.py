#richiesta 5 da non fare
tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )


def media_globale(tupla_vendite):
  prezzo_media=0
  cont=0
  for vendita in tupla_vendite:
    (reparto,categoria),(prodotto,(metodo,importo))=vendita
    print(reparto,categoria)
    for prodotto,*metodo in vendita:
        for metodo,importo in prodotto:
            prezzo_media+=importo
            cont+=1
    # for prodotto,prezzo in tipo:
    #     prezzo_media+=prezzo
    #     cont+=1
  return prezzo_media/cont#prezzo_media/cont


def venditaMax(tupla,nome):
    venditaMassimo=0
    prod=""
    for reparto,*tipo in tupla_vendite:
            for prodotto,prezzo in tipo:
               if(venditaMassimo<prezzo):
                    vendita=prezzo
                    prod=prodotto
    return (venditaMassimo,prod)

def venditaMin(tupla_vendite):
    prezzoMinTot=0
    for reparto,*altro in tupla_vendite:
        for giorno,prezzo in altro:
            if(prezzoMinTot>prezzo):
                prezzoMinTot=prezzo
                
    return prezzoMinTot



print("media globale :",media_globale(tupla_vendite))

