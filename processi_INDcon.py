''' PROCESSI INDIRETTAMENTE A CONOSCENZA UNO DELL'ALTRO
i processi potrebbere non conoscere gli altri in modo diretto, ma possono interagire
attraverso uno scambio indiretto di informazioni'''

'''1) Queue= classe che rappresenta una coda condivisa tra processi
    utilizzato per la comunicazione tra processi, consentendo lo scambio di dati in modo sicuro
   
   2)put(item)= aggiunge un elemento alla coda
   3)get()= Rimuove e restituisce un elemento alla coda.
   4) empty()= Restituisce True se la coda è vuota, altrimenti restistuisce false
   5) full()=   Restituisce True se la coda è piena, altrimenti restistuisce false 
   6) qsize()= restituisce il numero di elementi presenti nella coda
   7) close()= chiude la coda
   
   8)current_process: funzione che restituisce un oggetto Process che rappresenta il processo in esecuzione'''

from asyncio import Queue
import os# modulo che fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import Process,current_process,Pipe

def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(data, result_queue):
    process_id()
    print("elabora: ",data)
    result= data*2
    result_queue.put(result)

if __name__=="__main__":
    data_list=[1,2,3,4]
    result_queue= Queue()
    processes= []

    for data in data_list:
        p= Process(target=process_function, args=(data,result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Il main stampa i risultati")
    while not result_queue.empty():
        result= result_queue.get()
        print(result)
