import json
import requests
from pprint import pprint



def pesquisa():
    searh = input("Digite: ").upper()
    with open('linguagens.json',  encoding='utf8') as f:
        data = json.load(f)
        print(data.get(searh))


def rodarPrograma():
    verf = 1
    while verf > 0:
        print("Opção 1- Pesquisar uma linguagem e irá retornar onde estudar\nOpção 2- Opção Caso seja iniciante na Area\nOpção 3-  Parar programa")
        switchcase = int(input("Digite opção desejada: "))
        match switchcase:
            case 1:
                pesquisa()
            case 2:
                iniciante()


def iniciante():
    print("Parabens você escolheu a opção iniciante, seja muito bem nessa area de tecnologia!\n")
    print("Quando se é iniciante recomendamos sempre estudar a logica de programação\n")
    print("Nesse caso vamos recomendar um curso pra você sobre logica e algoritimos\n")
    with open('linguagens.json', encoding='utf8') as f:
        data = json.load(f)
        print(data.get('logica_programacao'))
        

    
