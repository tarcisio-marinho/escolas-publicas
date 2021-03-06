import time
from mining import *

def search(info, tipo, data, numero=10):

    if(tipo == "data"):
        if(info not in data):
            print("Data inexistente")
            return
            
    elif(tipo == "bairro"):
        if(info not in data):
            print("Bairro inexistente")
            return

    elif(tipo == "veiculo"):
        if(info not in data):
            print("Veiculo inexistente")
            return
    
    elif(tipo == "feridos"):
        if(info not in data):
            print("Quantidade de feridos inexistente")
            return

    lista = data[info]
    i = 0
    for acidente in lista:
        print("data: {}\nDescrição: {}\nVeiculo: {}\nComplemento: {}\nOcorrencia: {}\nBairro: {}\nHora:{}\nendereco: {}\nMaps:{}\n"
                .format(acidente["data"], acidente["descricao"], acidente["veiculo"], acidente["complemento"], acidente["ocorrencia"], acidente["bairro"], 
                acidente["hora"], acidente["endereco"], acidente["link"]))

        i+=1
        if(i == numero):
            break


def menu(dados):

    bairro, data, feridos, veiculo = get_data(dados)

    while True:
        try:
            pesquisa = input("Pesquisar por: ")
        except KeyboardInterrupt:
            exit(0)

        if(pesquisa == "bairro"):
            for local in bairro:
                print(local)

            escolha = input("Escolha o bairro: ")
            search(escolha, "bairro", bairro)

        elif(pesquisa == "data"):
            for dia in data:
                print(dia)

            escolha = input("Escolha a data: ")
            search(escolha, "data", data)

        elif(pesquisa == "feridos"):
            for quantidade in feridos:
                print(quantidade)

            escolha = input("Escolha a quantidade de feridos: ")
            try:
                escolha = int(escolha)
            except ValueError:
                print("Digite apenas números")
                continue

            search(escolha, "feridos", feridos)

        elif(pesquisa == "veiculo"):
            for automovel in veiculo:
                print(automovel)
            
            escolha = input("Escolha o veiculo: ")
            search(escolha, "veiculo", veiculo)
        
        else:
            print("Pesquisa incorreta.")


def read_file(): 

    path = "data/acidentes-2016.csv"

    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()
    
    return dados

if __name__ == "__main__":
    dados = read_file()
    menu(dados)
