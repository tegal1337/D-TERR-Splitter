
# by d4v.id
from tqdm import tqdm
from colorama import Fore,Style
def ket_file(ket):
    words = 0
    with open(ket, "r") as kata_file:
        for line in kata_file:
            num_kata = line.split(";"or","or":"or" ")
            words += len(num_kata)

        return str(words)


def split_line():
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Enter Filename (ex: daftar.txt):")
    nama = str(input(">> "))
    nama_file = open(nama, "r")
    read_file = nama_file.read()
    print("\n\tFile: "+Fore.GREEN+"{}".format(nama)+Style.RESET_ALL)
    print("\tLines: "+Fore.GREEN+"{}".format(all_line(nama))+Style.RESET_ALL)
    lines = read_file.split()
    print(Fore.RED+"\t["+Style.RESET_ALL+"#"+Fore.RED+"]"+Style.RESET_ALL+" Splitter Lines "+Fore.RED+"(contoh:34000-end)"+Style.RESET_ALL)
    print(Fore.RED+"\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Enter Number To Split (ex: 55):")
    num = int(input("\t>> "))
    print("Processing: "+Fore.GREEN+"{} - {} list".format(int(all_line(nama)), num)+Style.RESET_ALL)
    print("Result: "+Fore.GREEN+"{} copyied".format(int(all_line(nama)) - num)+Style.RESET_ALL)
    
    if int(all_line(nama)) - num < 0:
        print(Fore.RED+"Failed Input"+Style.RESET_ALL)
        exit()

    num_line = lines[(num-1):]
    with open("hasil-line.txt","w") as nama_file:
        for all_in in tqdm(num_line):
            nama_file.write("{}\n".format(all_in))

        print(Fore.GREEN+" SUCCESS SAVE "+Style.RESET_ALL+"["+Fore.GREEN+"hasil-line.txt"+Style.RESET_ALL+"]")


def all_line(file_line):
    baris = 0
    with open(file_line, "r") as file:
        for line in file:
            baris += 1
            line = baris

        return str(line)


def typeSplit(sign):
    if sign == 1:
        split = ":"
    elif sign == 2:
        split = ","
    elif sign == 3:
        split = ";"
    elif sign == 4:
        split = "|"
    elif sign == 5:
        split = "#"
    else:
        print(Fore.RED+"Wrong input..")

    return str(split)


def name_file():
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Enter Filename (ex: daftar.txt):")
    nama = str(input(">> "))
    print("File: {}\nLine: {}\nWords: {}".format(nama, all_line(nama), ket_file(nama)))


def split_text():
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Enter Filename  (ex: daftar.txt) >")
    nama = str(input(">> "))
    print("\n\tWords: "+Fore.GREEN+"{}".format(ket_file(nama))+Style.RESET_ALL)
    nama_file = open(nama, "r")
    print(Fore.RED+"\t["+Style.RESET_ALL+"#"+Fore.RED+"]"+Style.RESET_ALL+" List Splitter(Pembagi) text "+Fore.RED+"(; : ,)"+Style.RESET_ALL)
    print(Fore.RED+"\t["+Style.RESET_ALL+"#"+Fore.RED+"]"+Style.RESET_ALL+" Ex: [ admin;pa213ss;sada@gmail.com ]") 
    
    print(Fore.RED+"\n\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Split Type\t1.) :     2.) ,      3.) ;     4.) |     5.) #")
    numType = int(input("\t>> "))

    print(Fore.RED+"\n\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Ex: [ admin;pa213ss;sada@gmail.com ]") 
    print(Fore.RED+"\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+  "     [   0  ;   1   ;       2       ] Choose number (ex: 0): ")
    num = int(input("\t>> "))
    
    inputType = typeSplit(numType)
    read_file = nama_file.readlines()
    with open("hasil-text.txt", "w") as nama_file:
        for line in tqdm(read_file):
            action = line.split(inputType)
            input_action = action
            nama_file.write("{}\n".format(input_action[num]))
        
        print(Fore.GREEN+" SUCCESS SAVE "+Style.RESET_ALL+"["+Fore.GREEN+"hasil-text.txt"+Style.RESET_ALL+"]")
         


##core##
print(Fore.GREEN+"\n//"+Style.RESET_ALL+Fore.RED+" D-TERR by d4v.id"+Style.RESET_ALL)
type_tools = ["File Checker", "Splitter Text(: , ; | #)", "Splitter Lines"]
print(Fore.GREEN+"//"+Style.RESET_ALL+Fore.RED+" Multiple For Splitter"+Style.RESET_ALL)
try:
    print(Fore.RED+"["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Choose Methode: ")
    print("\t(1) {}\t(2) {}\t(3). {}".format(type_tools[0], type_tools[1], type_tools[2]))
    put_number =int(input("\t>> "))
    if put_number == 1:
        name_file()
    elif put_number == 2:
        split_text()
    elif put_number == 3:
        split_line()

except ValueError:
    print(Fore.RED+"\nFailed Input.."+Style.RESET_ALL)
except FileNotFoundError:
    print(Fore.RED+"\nFile Notfound.."+Style.RESET_ALL)
except IndexError:
    print(Fore.RED+"\nFailed Input.."+Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.RED+"\nExiting..."+Style.RESET_ALL)

    
