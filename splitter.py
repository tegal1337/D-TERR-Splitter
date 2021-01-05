
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
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Masukkan Nama File (ex: daftar.txt):")
    nama = str(input(">> "))
    nama_file = open(nama, "r")
    read_file = nama_file.read()
    print("\n\tLines: "+Fore.GREEN+"{} {} baris list".format(nama, all_line(nama))+Style.RESET_ALL)
    lines = read_file.split()
    print(Fore.RED+"\t["+Style.RESET_ALL+"#"+Fore.RED+"]"+Style.RESET_ALL+" Splitter(Pembagi) Baris "+Fore.RED+"(contoh:34000-selesai)"+Style.RESET_ALL)
    print(Fore.RED+"\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Masukkan angka awal baris/line yang ingin di split (ex: 55):")
    num = int(input("\t>> "))
    print("Proses: "+Fore.GREEN+"{} - {} list".format(int(all_line(nama)), num)+Style.RESET_ALL)
    print("Hasil: "+Fore.GREEN+"{} list di copy".format(int(all_line(nama)) - num)+Style.RESET_ALL)
    if int(all_line(nama)) - num < 0:
        print(Fore.RED+"GAGAL data melebihi batas dan tidak ada dalam file"+Style.RESET_ALL)
        exit()

    num_line = lines[(num-1):]
    with open("hasil-line.txt","w") as nama_file:
        for all_in in tqdm(num_line):
            nama_file.write("{}\n".format(all_in))

        print(Fore.GREEN+" SUCCESS SAVE "+Style.RESET_ALL+"tersimpan di folder ini ["+Fore.GREEN+"hasil-line.txt"+Style.RESET_ALL+"]")

def all_line(file_line):
    baris = 0
    with open(file_line, "r") as file:
        for line in file:
            baris += 1
            line = baris

        return str(line)

def name_file():
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Masukkan Nama File (ex: daftar.txt):")
    nama = str(input(">> "))
    print("File: {}\nList: {} baris\nWords: {} kata".format(nama, all_line(nama), ket_file(nama)))

def split_text():
    print(Fore.RED+"\n["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Masukkan Nama File (ex: daftar.txt) >")
    nama = str(input(">> "))
    print("\n\tWords: "+Fore.GREEN+"{} kata di list".format(ket_file(nama))+Style.RESET_ALL)
    nama_file = open(nama, "r")
    print(Fore.RED+"\t["+Style.RESET_ALL+"#"+Fore.RED+"]"+Style.RESET_ALL+" List Splitter(Pembagi) text "+Fore.RED+"(; : ,)"+Style.RESET_ALL)
    print(Fore.RED+"\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Contoh: [admin;pa213ss;sada@gmail.com]") 
    print(Fore.RED+"\t["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+"         [  0  ;   1   ;       2      ]  Ingin di split (ex: 2): ")
    num = int(input("\t>> "))
    read_file = nama_file.readlines()
    with open("hasil-text.txt", "w") as nama_file:
        for line in tqdm(read_file):
            action = line.split(";"or","or":")
            input_action = action
            nama_file.write("{}".format(input_action[num]))
        
        print(Fore.GREEN+" SUCCESS SAVE "+Style.RESET_ALL+"tersimpan di folder ini ["+Fore.GREEN+"hasil-text.txt"+Style.RESET_ALL+"]")
         
# core
print(Fore.GREEN+"\n//"+Style.RESET_ALL+Fore.RED+" D-TERR by d4v.id"+Style.RESET_ALL)
type_tools = ["File Checker", "Splitter Text(: , ;)", "Splitter Line/Baris"]
print(Fore.GREEN+"//"+Style.RESET_ALL+Fore.RED+" Multiple For Splitter"+Style.RESET_ALL)
try:
    print(Fore.RED+"["+Style.RESET_ALL+"?"+Fore.RED+"]"+Style.RESET_ALL+" Metode yang mau di eksekusi: ")
    print("\t(1) {}\t(2) {}\t(3). {}".format(type_tools[0], type_tools[1], type_tools[2]))
    put_number =int(input("\t>> "))
    if put_number == 1:
        name_file()
    elif put_number == 2:
        split_text()
    elif put_number == 3:
        split_line()

except ValueError:
    print(Fore.RED+"GAGAL data yang ada masukkan salah / tidak ada."+Style.RESET_ALL)
except FileNotFoundError:
    print(Fore.RED+"GAGAL file tidak ditemukan(Not Found)"+Style.RESET_ALL)
except IndexError:
    print(Fore.RED+"GAGAL data melebihi batas / tidak ada dalam file"+Style.RESET_ALL)

    
