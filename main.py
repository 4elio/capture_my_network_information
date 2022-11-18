# Il programma è stato scritto implementando i codici trovati su https://www.geeksforgeeks.org/


import json
import requests
import sys
import socket
from datetime import datetime

# Classe identificate è il primo oggetto che viene esceguito dal programma .
# Al suo interno sono definite le funzioni get_ip (il cui output restituisce l'indirizzo ip publico della macchina) e
# viene chiamata dalla funzione get_location al fine di generare le informazioni recuperate da https://ipapi.co

class identificate:

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    def get_location(self):
        ip_address = self.get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        
        #Conversione da array in stringa
        
        location_data = json.dumps(response)
       # location_data = json.loads(location_data) # Decommentare se si vuole convertire in Dict
        print(location_data) 
        print(type(location_data))

#Variabile che punta alla classe identificate al fine di poterla chiamare nella classe scannerport. 

youare = identificate()


# Classe scannerport è il secondo oggetto che viene eseguito dal programma .
# Questa classe interagisce con l'utente al fine di definire l'inizio e la fine della scansione porte con le variabili port_start e port_finish.

class scannerport:
    def portcheck(self):
        
        #Variabili
        target = youare.get_ip()
        port_start = int(input("Inizia dalla porta: "))
        port_finish = int(input("Fino alla porta: "))
       
#Utilizzata funzione try per gestire le eccezioni    
        try:

            # Ciclo for per scansione
            
            for port in range(port_start, port_finish):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)

                # Funzione che restituisce il print del output nel caso trovi una porta aperta

                result = s.connect_ex((target, port))
                if result == 0:
                    print("Port {} is open".format(port))
                s.close()
#Eccezioni
        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()    

def main():
    youare.get_location() # Chiamata la funzione get_location 
    scannerport().portcheck() #Chiamata la funzione portcheck 
    quit() 

if __name__ == '__main__':
    main()
