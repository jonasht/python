# This code from https://github.com/FreeOpcUa
from opcua import Client
import time
import sys
sys.path.insert(0, "..")

if __name__ == "__main__":
    client = Client("opc.tcp://localhost:4840")
    try:
        # connecting!
        client.connect()
        # Client has a few methods to get proxy to UA nodes that should always be in address space
        root = client.get_root_node()
        myData1 = root.get_child(["0:Objects", "2:MyObject", "2:MyData1"])
        myDataDatetime = root.get_child(["0:Objects", "2:MyObject", "2:MyDataDatetime"])
        obj = root.get_child(["0:Objects", "2:MyObject"])
        print("myobj is: ", obj)
        print("myData1 is: ", myData1)
        print("myDataDatetime is: ", myDataDatetime)
        while True:
            print("myData1 = %4.1f" %client.get_node("ns=2;i=2").get_value())
            print("myDataDatetime = ", client.get_node("ns=2;i=3").get_value().strftime("%Y-%m-%d 	%H:%M:%S"))
            time.sleep(2)            
    finally:
        client.disconnect()