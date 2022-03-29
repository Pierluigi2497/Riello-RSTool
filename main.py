# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def createVisualGraph(Graph):
    if len(Graph) < 15:
        return
    #Tolgo i primi 10
    Graph = Graph[10:]
    #Finchè non finisco il grafico, stampo i valori
    x = []
    y = []
    while(Graph):
        value = Graph[:4]
        #print(value)
        x.append(int.from_bytes(bytes.fromhex(value[0]),"big"))
        ora = str(x[-1])
        y.append(int.from_bytes(bytes.fromhex(value[1] + value[2]),"big"))
        valore = str(y[-1]/100)
        print("Il " + ora + " è " + valore)
        Graph = Graph[4:]

def getData(index):
    o = []
    client.send(get_something[index])
    Graph = client.recv(1024)
    Graph = Graph.hex()
    while(Graph):
        o.append(Graph[:2])
        Graph = Graph[2:]
    return o


def showTemperature(Graph):
    if len(Graph) < 11:
        return
    #Tolgo i primi 10
    Graph = Graph[10:]
    print("Temperatura: " + str(int.from_bytes(bytes.fromhex(Graph[0]),"big")))

def showPower(Graph):
    if len(Graph) < 13:
        return
    #Tolgo i primi 11
    Graph = Graph[11:]
    power = int.from_bytes(bytes.fromhex(Graph[0] + Graph[1]),"big")
    power = power / 10000
    print("Potenza attuale: " + str(power))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import socket
    import sys
    import time


    if len(sys.argv) < 3:
        print("Inserire 3 argomenti: [ID] [IP] [PORT] ")

    host = sys.argv[2]
    port = int(sys.argv[3])
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    #Prende il grafico
    #get_graph = b"\x00\x00\x00\x00\x00\x06\x01\x03\xc0\x00\x00\x30"
    get_something = []
    get_something.append(b"\x00\x00\x00\x00\x00\x06\x01\x03\xc0\x00\x00\x30")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x1e\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x1d\x00\x01")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x3d\x00\x01")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x05\x00\x01")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x37\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x39\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x10\x00\x0c")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x01\x00\x0f")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x3b\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x25\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x21\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x1c\x00\x01")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x23\x00\x02")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x10\x20\x00\x01")
    get_something.append(b"\x00\x00\00\x00\x00\x06\x01\x03\x30\x80\x00\x01")
    

#4 Total Energy?????????
#5 ACTUAL POWER
#8 IDK,too long    Potrebbe esserci "Energia Oggi"
#9 Potenza di picco
#11 Energia totale
#12 Temperature

    while(1):
        q = "Y"
        if(q == "Y"):
            Graph = getData(0)
            if sys.argv[1] != '0':
                print(getData(sys.argv[1]))
            else:
                createVisualGraph(getData(0))
                showPower(getData(5))
                showTemperature(getData(12))
            time.sleep(10)
        else:
            exit(0)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
