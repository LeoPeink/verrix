import subprocess
import os
import time
import hashlib

#FINAL VERSION
#check directories in /raw, create them in /unsorted if they don't exist
#ask what directory to render, then if retrying, then if shutdown at the end
#for each file, extracts the date from one filename and renames the file with the date and the hash, then renders it

def main_menu():
    print("Benvenuto in Verrix 4.0!\nQuesto script serve ad eliminare i silenzi dalle lezioni di UniTS per renderle più fruibili. Inoltre le encoda in modo che siano più leggere.")
    while(1):
        retry = 2
        while(retry != 0 and retry != 1):
            print("Vuoi rifare i file già fatti? 1 - sì, 0 - no")
            retry = int(input(""))
        shutdown = 2
        while(shutdown != 0 and shutdown != 1):
            print("Vuoi spegnere il pc al termine? 1 - sì, 0 - no")
            shutdown = int(input(""))
        print("Che cosa vogliamo renderizzare oggi?")
        print ("0 - Tutti i file [default]")
        materie = enumerate(os.listdir("raw/"), start=1)
        length = 0
        for i, nome in materie:
            print(f"{i} - {nome}")
            length += 1
        scelta = int(input(""))
        materie = enumerate(os.listdir("raw/"), start=1)
        if(scelta == 0):
            for i, nome in materie:
                verrix(nome, retry)
            break
        elif (scelta < 0 or scelta <= length):
            #print(list(materie))
            verrix(list(materie)[scelta-1][1], retry)
            break
        else:
            print("Input non valido.")
        '''
        if(scelta < 0 or scelta < len(os.listdir("raw/"))):
            verrix(list(enumerate(os.listdir("raw/")))[scelta][1], retry)
            break
        elif(scelta == 0):
            for i, nome in enumerate(os.listdir("raw/")[:-1]):
                verrix(list(enumerate(os.listdir("raw/")))[i][1], retry)
            break
        '''
    return


def  verrix(path, retry):                       #prende in input la cartella di lavoro e una bool: true se deve riprovare a renderizzare, false se deve renderare solo file nuovi
    in_path = "raw/" + path
    out_path = "unsorted/" + path
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    for item in os.listdir(in_path):
        if(item[0] == "#" and item[1] == "_" and retry == 0):
            continue
        elif(item[0] == "#" and item[1] == "_" and retry == 1):
            newitem = item
        else:
            newitem = "#_" + item
            os.rename(in_path + "/" + item , in_path + "/" + newitem)
        id = time.time()
        newfilename = item
        for i in range(len(str(item))):         #trova l'index con la data e assembla il nome del file renderizzato con l'hash
            if(item[i] == "2" and item [i+1] == "0" and item [i+2] == "2" and (item [i+3] == "3" or item [i+3] == "0" or item [i+3] == "2" or item [i+3] == "4")): 
                idx_anno = i
                if(item[i+4] == "-"):
                    newfilename = item[idx_anno] + item[idx_anno+1] + item[idx_anno+2] + item[idx_anno+3] + "-" + item[idx_anno+5] + item[idx_anno+6] + "-" + item[idx_anno+8] + item[idx_anno+9] + "_"+hashlib.md5((str(id).encode('utf-8'))).hexdigest()[-5:]  + ".mkv"
                else:
                    newfilename = item[idx_anno] + item[idx_anno+1] + item[idx_anno+2] + item[idx_anno+3] + "-" + item[idx_anno+4] + item[idx_anno+5] + "-" + item[idx_anno+6] + item[idx_anno+7] + "_"+hashlib.md5((str(id).encode('utf-8'))).hexdigest()[-5:]  + ".mkv"
        if item.endswith("mp4"):
            newfilename = newfilename[:-4] + ".mp4"
        print(f"{os.path.join(in_path, newitem)} -> {os.path.join(out_path, newfilename)}")
        #   subprocess.call(f"unsilence \"{os.path.join(in_path, newitem)}\" -ss 25 -y \"{os.path.join(out_path, newfilename)}\" ", shell=True)
        #subprocess.call(f"unsilence \"{os.path.join(in_path, newitem)}\" \"{os.path.join(out_path, newfilename)}\" -ss 25 -y  -t 16", shell=True)
    return


#main script:
main_menu()