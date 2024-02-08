''' PROCESSI DIRETTAMENTE A CONOSCENZA
i processi sono consapevoli l'uno dell'altro e comunicano direttamente '''

import os# modulo che fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import Process,current_process,Pipe

def process_id():
     print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(conn):
     process_id()
     print("elabora il dato ricevuto ed invio risultato")
     data_received = conn.recv()
     result= data_received*2
     conn.send(result)
     conn.close()

if __name__=="__main__":
     process_id()
     print(" creo una connesione e un processo figlio")
     parent_conn, child_conn = Pipe()
     data= 5
     p= Process(target=process_function, args=(child_conn,))
     p.start()
     parent_conn.send(data)
     result= parent_conn.recv()
     p.join()
     process_id()
     print("stampo il risultato ricevuto")
     print(result)
     
