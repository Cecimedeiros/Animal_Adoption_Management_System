#sistema de gerenciamento da entrada de animais para adoção (perfil dos animais)
import json
import os
from time import sleep

caminho_arquivo= os.path.join(os.path.dirname(__file__), 'json.json')

def carregar_abrigo():
    if not os.path.exists(caminho_arquivo):
        with open (caminho_arquivo,'w') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, ident=3)
        with open (caminho_arquivo, 'r') as arquivojson_aberto:
           return json.load(arquivojson_aberto)

def cadastrar_abrigo (nome, endereco, tipo_animal, contato):
    abrigos= carregar_abrigo()
    abrigos.append({'nome': nome, 'endereco': endereco, 'tipo_animal': tipo_animal,'contato':contato})
    with open (caminho_arquivo, 'w') as arquivojson_aberto:
        json.dump (abrigos, arquivojson_aberto, ident=3, ensure_ascii=False)
    print ("O abrigo foi cadastrado!")

def listar_abrigo():
    abrigos= carregar_abrigo()
    if abrigo:
        for abrigo in abrigos:
            print (f"Nome: {abrigo['nome']}, \n Endereçoo: {abrigo['endereco']},\n Porte do animal: {abrigo['tipo_animal']}, Contato: {abrigo['contato']} ")
    else: 
        print ("Nenhum abrigo cadastrado! ")

def atualizar_abrigo (nome_antigo, novo_nome, novo_ende, novo_tipo_animal, novo_contato):
   
    abrigos= carregar_abrigo()
    for abrigo in abrigos:
        if abrigo['nome']== nome_antigo:
            abrigo['nome']==novo_nome
            abrigo['endereco']== novo_ende
            abrigo['tipo_animal']== novo_tipo_animal
            abrigo['contato']==novo_contato
            break
    with open (caminho_arquivo, 'w') as arquivojson_aberto: 
        json.dump(abrigos, arquivojson_aberto,indent=3, ensure_acii=False)
    print ("Informaçõe sobre o abrigo atualizadas!")

def excluir_abrigo (nome):
    abrigos=carregar_abrigo()
    for abrigo in abrigos:
        if abrigo['nome']==nome:
            abrigos.remove (abrigo)
        with open (caminho_arquivo, 'w') as caminho_arquivo:
            json.dumps(abrigos, caminho_arquivo, ident=3, ensure_ascii=False)
        print ("Dados do abrigo excluídos! ")

def buscar_abrigos(nome):
    abrigos=carregar_abrigo ()
    encontrado = False
    for abrigo in abrigos:
        if abrigo['nome'] == nome:
            print (f"Nome: {abrigo['nome']}, \n Endereçoo: {abrigo['endereco']},\n Porte do animal: {abrigo['tipo_animal']}, Contato: {abrigo['contato']} ")
            encontrado=True
        if not encontrado:
            print ("Nenhum usuário encontrado!")

def main (): 
    print (" <<-------- PLATAFORMA \"EM BUSCA DE UM LAR\" -------->>")
    print ("\n Olá, somos uma plataforma de gerenciamento de animais para adoção!" )
    op= int(input ("\n Aqui você consegue realizar as seguintes ações: \n 1 - Sou um abrigo \n 2 - Sou voluntário(a) da plataforma/Quero me tornar voluntário(a) \n 3 - Quero adotar um animal \n 4 - Sair da plataforma \n O que deseja fazer no momento? "))
  
    if op== 1: 
        opcao=input("O que você deseja fazer dentre as seguintes opções: 1- cadastrar o abrigo \n 2- Vizualizar informações do abrigo \n 3- Atualizar informações sobre o abrigo 4- Excluir informações sobre o abrigo \n 5- Listar os abrigos existentes \n 6-Voltar ao menu inicial ? ")
        match (opcao):
            case 1: 
                while True:
                    print ("------> SISTEMA DE GERENCIAMENTO DO CADASTRAMENTO DE ABRIGOS PARA ANIMAIS <------")
                    print ("\n Para cadastrar um novo abrigo é preciso que responda as seguintes perguntas: ")
                    nome=input("\n Informe o nome do abrigo a ser cadastrado: ")
                    endereco= input ("\n Informe a localização do abrigo (cidade e estado, apenas): ")
                    tipo_animal= input ("\nInforme o porte dos animais que esse abrigo é capaz de abrigar: ")
                    contato=input ("\n Informe o contato do abrigo: ")
                    cadastrar_abrigo(nome, endereco, tipo_animal,contato)
                    maisum= input ("Deseja cadastrar mais um abrigo?")
                    if maisum=="n":
                        break
            case 2: 
                while True:
                    nome=input("\n Informe o nome do abrigo a ser procurado: ")
                    buscar_abrigos()
                    maisum= input ("Deseja buscar mais um abrigo?")
                    if maisum=="n":
                        break
            case 3:
                while True:
                    nome_antigo= input ("Informe o nome a ser atualizado (o nome antigo): ")
                    novo_nome= input ("Informe o novo nome: ")
                    novo_ende= input ("Informe o novo endereço do abrigo: ")
                    novo_tipo_animal=input ("Informe o novo tipo de porte de animal que será abrigado pelo abrigo: ")
                    novo_contato= input ("Informe o novo contato do abrigo")
                    atualizar_abrigo(nome_antigo, novo_nome, novo_ende, novo_tipo_animal, novo_contato)
                    maisum= input ("Deseja atualizar mais um abrigo?")
                    if maisum=="n":
                        break
            case 4:
                while True:
                    nome= input ("Qual o nome do abrigo você deseja excluir?")
                    excluir_abrigo(nome)
                    maisum= input ("Deseja excluir mais um abrigo?")
                    if maisum=="n":
                        break
            case 5:
                listar_abrigo()
            case 6:
                print ("Voltando ao menu inicial...")
                sleep (4)
                main()  
            case _: 
                print ("Opção inválida! Tente novamente.")
    elif op==2:
        voluntario ()
    elif op==3: 
        questionario ()
    elif op==4:  
        print ("Saindo da plataforma. Até logo!")
        fim ()
    else: 
        print ("Opção inválida, tente novamente! ")
        main()

if __name__=="__main__":
    main ()
main ()

#ignorem daqui pra baixo