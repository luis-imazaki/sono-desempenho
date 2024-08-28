from LinkedList import LinkedList
import csv



with open("teste2.csv", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if str(linha[0]) == "CIÊNCIA DA COMPUTAÇÃO - BACHARELADO" and str(linha[6]) == "2019/1":
            print(str(linha))
        