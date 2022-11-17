import json
import requests
import sys
import socket
from datetime import datetime



class identificate:

    def get_ip(Self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    def get_location(Self):
        ip_address = Self.get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = json.dumps(response)
        location_data = json.loads(location_data)
        print(location_data)
        print(type(location_data))


#Variabili dichiarate
youare = identificate()
#infolistarray = identificate().get_location()
#infoliststring = reduce(lambda a, b :a+ "" +str(b), infolistarray)

def main():
    print(youare.get_location())
    target = youare.get_ip()


    port_start = int(input("Inizia dalla porta: "))
    port_finish = int(input("Fino alla porta: "))

    # Defining a target
    if len(sys.argv) == 2:

        # translate hostname to IPv4
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Invalid amount of Argument")
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:

        # will scan ports
        for port in range(port_start, port_finish):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicatoror i in location_data:

            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()
if __name__ == '__main__':
    main()