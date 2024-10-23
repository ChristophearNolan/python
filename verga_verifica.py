class Articolo:
    def __init__(self,codice,fornitore,marca,prezzo,quantita):
        self.codice=codice
        self.fornitore=fornitore
        self.marca=marca
        self.prezzo=prezzo
        self.quantita=quantita
        

    def scheda_articolo(self):
        return(f"codice: {self.codice}\n fornitore: {self.fornitore}\n marca: {self.marca}\n prezzo: {self.prezzo}\n quantità: {self.quantita}")
    
    def modifica_scheda(self):
         #self.codice=input("inserisci il nuovo codice: ")
         self.fornitore=input("inserisci il nuovo fornitore: ")
         self.marca=input("inserisci la nuova marca: ")
         self.prezzo=input("inserisci il nuovo prezzo: ")
         self.quantita=input("inserisci la nuova quantità: ")
         return(f"fornitore: {self.fornitore}\n marca: {self.marca}\n prezzo: {self.prezzo}\n quantità: {self.quantita}")
    

    #orario 9.30
class Televisore(Articolo):
    def __init__(self,codice, fornitore,marca,prezzo,quantita,pollici,tipo): 
        super().__init__(codice, fornitore,marca,prezzo,quantita)
        self.pollici=pollici
        self.tipo=tipo
        

    def scheda_articolo(self):
         return super().scheda_articolo()+f"\npollici: {self.pollici}\n tipo: {self.tipo}"
    # orario 9.47


t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")

print(t1.scheda_articolo())
print("--------------------------")
t1.modifica_scheda()
print(t1.scheda_articolo())
print("--------------------------")


class Frigorifero(Articolo):
     
    def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
        super().__init__(codice,fornitore,marca,prezzo,quantita)
        self.dimensioni=dimensioni
        self.modello=modello

    def scheda_articolo(self):
         return super().scheda_articolo()+f"\ndimensioni: {self.dimensioni}\n modello: {self.modello}"

f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
print(f1.scheda_articolo())
print("--------------------------")

#orario 10.1


class Ordine():
    def __init__(self,codice,data, piva,indirizzo):
        self.codice=codice
        self.data=data
        self.piva=piva
        self.indirizzo=indirizzo
        self.lista_articoli=[]
    
    def aggiungi_articolo(self,articolo):
        if isinstance(articolo,Televisore):
            tipo_articolo="televisore"
            self.lista_articoli.append(articolo)
            print(f"articolo del tipo: {tipo_articolo} è stato aggiunto alla lista")

        elif isinstance(articolo,Frigorifero):
            tipo_articolo="frigorifero"
            self.lista_articoli.append(articolo)
            print(f"articolo del tipo {tipo_articolo} è stato aggiunto alla lista")

        else:
            print("tipo di articolo non valido")

    def rimuovi_articolo(self,articolo):
        if isinstance(articolo,Televisore):
            tipo_articolo="televisore"
            self.lista_articoli.remove(articolo)
            print(f"articolo del tipo: {tipo_articolo} è stato rimosso alla lista")
        
        elif isinstance(articolo,Frigorifero):
            tipo_articolo="frigorifero"
            self.lista_articoli.remove(articolo)
            print(f"articolo del tipo: {tipo_articolo} è stato rimosso alla lista")

        else: 
            print("articolo non presente nella lista")
    
    def importo_ordine(self):
        importoT=0
        importoF=0
        for articolo in self.lista_articoli:
            if isinstance(articolo,Televisore):
                importoT=int(articolo.quantita)*int(articolo.prezzo)
                print(f"numero articoli: {articolo.quantita}")
                print(f"importo televisori{importoT} ")

            elif isinstance (articolo,Frigorifero):
                importoF=int(articolo.quantita)*int(articolo.prezzo)
                print(f"numero articoli: {articolo.quantita}")
                print(f"importo frigoriferi{importoF} ")
            
            else:
                print("articolo non presente nella lista")


    def dettaglio_ordine(self):
        sommaT=0
        sommaF=0
        for articolo in self.lista_articoli:
            if isinstance(articolo,Televisore):
                sommaT+=int(articolo.prezzo)
            
            elif isinstance(articolo,Frigorifero):
                sommaF+=int(articolo.prezzo)

            else: 
                print("articolo non presente nella lista")

        print(f"somma importi televisori: {sommaT}")
        print(f"somma importi frigorifer: {sommaF}")
        print(f"somma totale degli importi dei televisori e dei frigoriferi: {sommaT+sommaF}")



        return([sommaT,sommaF,sommaT+sommaF])
    #10.40
        
t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t1)
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(t2)
ordine1.rimuovi_articolo(f2)

ordine1.importo_ordine()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")
print("--------------------------")


class Ordini():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.lista_ordine=[]

  def aggiungi_ordine(self,ordine):
      self.lista_ordine.append(ordine)
      print("ordine aggiunto con successo alla lista")
    

  def rimuovi_ordine(self,ordine):
    if ordine in self.lista_ordine:
        self.lista_ordine.remove(ordine)
        print("ordine rimosso dalla lista con successo")

  def totale_ordini(self):
    totT=0
    totF=0
    tot=0
    for ordine in self.lista_ordine:
        importi=ordine.dettaglio_ordine()
        totT=importi[0]
        totF=importi[1]
        tot=importi[2]

        print("--------------------------")
        print(f"\nImporto televisori= {importi[0]}")
        print(f"\nImporto frigoriferi= {importi[1]}")
        print(f"\nImporto Totale= {importi[2]}")

    return ([totT,totF,tot])
  

ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

#orario 11.03