''' PROCESSI TOTALMENTE IGNARI

 in questo caso i processi sono ignari della presenza di altri processi  e operano indipendente senza alzuna comunicazione diretta o scambio di informazioni
  un esempio può essere il parallelismo di dati:
  con un immagine divisa in pixel, ogni processo elabora i dati in un determinato set di pixel senza preoccuparsi di altri processi '''


''' il multiprocessing è una libreria per la creazione, la comunicazione e la sincornizzazione
tra processi nella programmazione parallela e concorrente'''

from multiprocessing import Process
''' process è una classe che serve per creare processi eseguendo una funzione
(o metodo ) specificando come target'''

def process_function (data):
    result= data * 2
    print(result)

if __name__=="__main__":
    data_list=[1, 2, 3, 4]
    processes=[]

    for data in data_list:
        p=Process(target=process_function,args=(data,))
        '''la virgola istituisce la dichiarazione di null'''
        processes.append(p)
        p.start()
        ''' avvia l'esecuzione del processo separato '''

    for p in processes:
        p.join()
        ''' blocca il processo principale fino a quando il processo separato non termina'''


    
