import json
import os
import time
from sec_crud import carregar_animal

caminho_arquivo = os.path.join(os.path.dirname(__file__), 'adotantes.json')

def carregar_adotantes():
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w',  encoding='utf-8') as arquivojson_aberto:
            json.dump([], arquivojson_aberto, indent=3)

    dados = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivojson_aberto:
        if not isinstance(dados, list):
            return []
        return json.load(arquivojson_aberto)

def cadastrar_adotante(nome, idade, bairro, contato, preferencia_porte, preferencia_especie):
    adotantes = carregar_adotantes()
    adotantes.append({
        'nome': nome,
        'idade': idade,
        'bairro': bairro,
        'contato': contato,
        'preferencia_porte': preferencia_porte,
        'preferencia_especie':preferencia_especie
    })
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
        json.dump(adotantes, arquivojson_aberto, indent=3, ensure_ascii=False)
    print("Adotante cadastrado com sucesso!")

def listar_adotantes():
    adotantes = carregar_adotantes()
    if adotantes:
        for adotante in adotantes:
            nome = adotante.get('nome', 'Nome não disponível')
            idade = adotante.get('idade', 'Idade não disponível')
            bairro = adotante.get('bairro', 'Bairro não disponível')
            contato = adotante.get('contato', 'Contato não disponível')
            preferencia_animal = adotante.get('preferencia_animal', 'Preferência não disponível')
            print(f"\n Nome: {nome}, \n Idade: {idade}, \n bairro: {bairro}, \n Contato: {contato}, \n Preferência de animal: {preferencia_animal}")
    else:
        print("Nenhum adotante cadastrado!")

def buscar_adotante(nome):
    adotantes = carregar_adotantes()
    encontrado = False
    for adotante in adotantes:
        if adotante['nome'] == nome:
            print(f"Nome: {adotante['nome']}, Idade: {adotante['idade']}, bairro: {adotante['bairro']}, Contato: {adotante['contato']}, Preferência de animal: {adotante['preferencia_animal']}")
            encontrado = True
            break
    if not encontrado:
        print("Nenhum adotante encontrado com esse nome.")

def atualizar_adotante(nome_velho, nome_novo, end_novo_adotante, porte_novo_escolhido,novo_contato_adotante):
    adotantes = carregar_adotantes()
    for adotante in adotantes:
        if adotante['nome'] == nome_velho:
            adotante['nome']= nome_novo
            adotante['endereço']= end_novo_adotante
            adotante['porte']= porte_novo_escolhido
            adotante['contato']= novo_contato_adotante
            break
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
            json.dump(adotantes, arquivojson_aberto, indent=3, ensure_ascii=False)
    print("Adotante atualizado com sucesso!")            

def excluir_adotante(nome):
    adotantes = carregar_adotantes()
    adotantes_filtrados = [adotante for adotante in adotantes if adotante['nome'] != nome]
    
    if len(adotantes_filtrados) < len(adotantes):
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivojson_aberto:
            json.dump(adotantes_filtrados, arquivojson_aberto, indent=3, ensure_ascii=False)
        print("Adotante excluído com sucesso!")
    else:
        print("Adotante não encontrado para exclusão.")

def verificar_preferencia_adotante(adotantes, animais):
    nome_adotante = input("Informe o nome do adotante para verificar as preferências: ").strip().lower()
    adotante_encontrado = None
    for adotante in adotantes:
        if adotante['nome'].strip().lower() == nome_adotante:
            adotante_encontrado = adotante
            break    
    if not adotante_encontrado:
        print("Adotante não encontrado.")
        return  
    print(f"Verificando preferências de adoção para {adotante_encontrado['nome']}...")
    
    preferencia_porte = adotante_encontrado['preferencia_porte']
    preferencia_especie = adotante_encontrado['preferencia_especie']
    
    for animal in animais:
        # Garantir que o porte do animal também seja uma string para a comparação
        porte_animal = animal.get('porte' , '').strip()
        especie_animal = animal.get('especie' , '').strip()
        
        # Comparar as preferências do adotante com as características do animal 
        if preferencia_porte == porte_animal or preferencia_especie == especie_animal:
            print(f"O animal {animal['nome']} atende às suas preferências!")
        


def main3():
    while True:
        op = int(input("\nEscolha uma das ações:\n1 - Cadastrar adotante\n2 - Listar adotantes\n3 - Buscar adotante\n4 - Excluir adotante \n5 - Atualizar adotante\n6 - Match \n7- Voltar para o menu inicial \nO que deseja fazer? "))

        match op:
            case 1:
                while True:
                    print("---- CADASTRO DE ADOTANTE ----")
                    nome = input("Informe o nome do adotante: ")
                    idade = input("Informe a idade do adotante: ")
                    
                    print("\nBairros disponíveis em Recife:")
                    bairros = ["Boa Viagem", "Casa Forte", "Graças", "Jaqueira", "Torre", "Várzea"]
                    for i, bairro in enumerate(bairros, 1):
                        print(f"{i}. {bairro}")
                    bairro_escolhido = int(input("Escolha o número do bairro desejada: "))
                    if bairro_escolhido <= 1 or bairro_escolhido > len(bairros):
                        bairro = bairros[bairro_escolhido - 1]
                    
                    contato = input("Informe o contato do adotante: ")

                    print("\nPreferências de animais:")
                    preferencias_porte = ["1", "2", "3"]
                    preferencias_especie = ["1", "2", "3"]

                    while True:
                        for i, preferencia in enumerate(preferencias_porte, 1):
                            print(f"{i}. {preferencia}")

                        try:
                            preferencia_escolhida_porte = int(input("Escolha o número da preferência desejada \n 1 - Pequeno porte \n 2 Médio porte \n 3 - Grande porte : "))
                            
                            if 1 <= preferencia_escolhida_porte <= 3:
                                preferencia_porte = preferencias_porte[preferencia_escolhida_porte - 1]
                                break 
                            else:
                                print('Escolha uma opção do menu.')
                                
                        except ValueError:
                            print('Entrada inválida. Por favor, insira um número.')
                    while True:
                        for i, especie in enumerate(preferencias_especie, 1):
                            print(f"{i}. {especie}")

                        try:
                            preferencia_escolhida_especie = int(input("Escolha o número da preferência de espécie: \n1 - Cachorro \n2 - Gato \n3 - Outro : "))
                            
                            if 1 <= preferencia_escolhida_especie <= 3:
                                preferencia_especie = preferencias_especie[preferencia_escolhida_especie - 1]
                                break 
                            else:
                                print('Escolha uma opção do menu.')
                        except ValueError:
                            print('Entrada inválida. Por favor, insira um número.')

                    
                    cadastrar_adotante(nome, idade, bairro, contato, preferencia_especie, preferencia_porte )

                    maisum = input("Deseja cadastrar mais um adotante? (s/n): ").strip().lower()
                    if maisum == 'n':
                        break
            case 2:
                    listar_adotantes()

            case 3:
                    nome = input("Informe o nome do adotante para buscar: ")
                    buscar_adotante(nome)

            case 4:
                    nome = input("Informe o nome do adotante para excluir: ")
                    excluir_adotante(nome)

            case 5:
                    
                    print ("\n -->>  ATUALIZAÇÃO DE DADOS DOS ADOTANTE <<--")
                    nome_velho= input ("Informe o nome do adotante que deseja atualizar: ")
                    if nome_velho ==nome_velho:
                        nome_novo= input ("Informe o novo nome: ")
                        print("\n1 - Boa Viagem", "\n2 - Casa Forte", "\n3 - Graças", "\n4 - Jaqueira", "\n5 - Torre", "\n6 - Várzea")
                        end_novo_adotante= input ("Informe o novo bairro do adotante: ")
                        print("\n1 - Grande Porte" "\n2 - Médio Porte" "\n3 - Pequeno Porte")
                        porte_novo_escolhido=input ("Informe qual o porte desejado: ")
                        novo_contato_adotante= input ("Informe o novo contato do adotante: ")
                        atualizar_adotante(nome_velho, nome_novo, end_novo_adotante, porte_novo_escolhido, novo_contato_adotante)
                        while True:
                            maisum= input ("Deseja atualizar mais um adotane? (s/n)").lower()
                            if maisum == 's' or maisum == 'sim':
                                time.sleep(3)
                                break

                            elif maisum or 'n' or 'não' or 'nao':
                                 print("Atualização encerrada...")
                                 time.sleep(3)
                                 break
                            
                            else:
                                print('\n Escolha uma opção disponível no menu!')                     
            case 6:
                
                adotantes = carregar_adotantes()  # Carrega os adotantes
                animais = carregar_animal()  # Carrega os animais
                verificar_preferencia_adotante(adotantes, animais) 

            case 7:       
                    print(" Voltando para o menu inicial...")
                    time.sleep(3)
                    break

            case _:
                    print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main3()