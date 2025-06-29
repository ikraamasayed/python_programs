import time 
class ON_Operation :
    
    def execute ( self):
        print( "Screen ON")
    
class OFF_Operation:
    def execute ( self):
        print(" Screen OFF ")

class Device :
    def Operation ( self,ide):
        ide.execute()

default_state = True  
lap1 = Device()

starttime = time.time()
duration = 10 
while time.time() - starttime< duration:
    if default_state:
        ide =  ON_Operation()
        default_state = False
    else :
        ide = OFF_Operation()
        default_state = True
    
    lap1.Operation(ide)
    time.sleep(2)
print( "time exceeds")
