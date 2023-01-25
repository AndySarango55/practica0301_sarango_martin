import cProfile
import csv

nif_dict = {"0":"T","1":"R","2":"W","3":"A","4":"G","5":"M","6":"Y","7":"F","8":"P","9":"D","10":"X","11":"B","12":"N",
                 "13":"J","14":"Z","15":"S","16":"Q","17":"V","18":"H","19":"L","20":"C","21":"K","22":"E",}


def check_username(nombre, apellidos):
    return nombre.title(), apellidos.title()

def check_nif(nif_usuario):

    if nif_usuario == "DNI":
        return nif_usuario
    else:
        dni = str(nif_usuario)
        num = dni[0:8]
        check = int(num) % 23
        good_num = nif_dict[str(check)]
    return num + good_num

def check_user(documento):
    with open(documento, encoding="utf-8") as csvfile:
        lista = []
        correccion = []
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for datos in reader:
            lista.append(datos)
            nombre = check_username(datos[0])
            dni = check_nif(datos[1])
            correccion.append([nombre, dni])
    with open("salida.csv", "w", encoding="utf-8", newline=" ") as csvfil:
        writer = csv.writer(csvfil, delimiter=",",dialect=csv.excel)
        for che in correccion:
            writer.writerow(che)

cProfile.run("check_user('1000.csv')")





