# Patrick Johnson         4/13/2020 #
# SWDV 630 3W 20/SP2         Week 5 #
#####################################
# Singleton Design Pattern Example

class ConnectionSingleton:
    __instance = None
    
    def __new__(cls):
        if cls.__instance == None:
            print("Connecting (Should only happen once)")
            cls.__instance = super(ConnectionSingleton, cls).__new__(cls)
        return cls.__instance

def main():
    connection1 = ConnectionSingleton()
    connection2 = ConnectionSingleton()
    
    print(connection1 == connection2, connection1 is connection2)
    
    # Note the shared memory address
    print(connection1)
    print(connection2)
    
    # Instances can be treated like Python class objects
    connection1.test = "Something"
    print(connection2.test)
    print(ConnectionSingleton().test)
    
if __name__=="__main__":
    main()
        