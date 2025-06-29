import os 
# os.remove("G:/My Drive/python_program/diary.txt")

with open (r"G:/My Drive/python_program/diary.txt","a+") as h:
    lal = h.read()
    if h.tell() !=0 :
        h.seek(0)
        h.write( "Ikku ")
        h.truncate()
        h.seek(0)
        lal = h.read()
        print(lal)
    
    h.seek(0)
    h.write("Ikrama")
    h.truncate()
    h.seek(0)
    lal =h.read()
    print(lal)

with open (r"G:/My Drive/python_program/diary.txt","+a") as i:
    if i.tell ()!=0:
        i.write(" Sayed")
        i.write("\nNikhat Parveen")
        i.seek(0)
    pila=i.read()
    print(pila)
