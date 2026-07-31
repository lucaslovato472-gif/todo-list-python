import json
import os

ARQUIVO = "minhas_tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        file = open(ARQUIVO, "r", encoding="utf-8")
        tarefas = json.load(file)
        file.close()
        return tarefas
    return []

def salvar_tarefas(tarefas):
    file = open(ARQUIVO, "w", encoding="utf-8")
    json.dump(tarefas, file, ensure_ascii=False, indent=4)
    file.close()

def mostrar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nVocê não tem nenhuma tarefa cadastrada.")
    else:
        print("\n--- SUAS TAREFAS ---")
        for i in range(len(tarefas)):
            status = "✓" if tarefas[i]["concluida"] else " "
            print(f"{i + 1}. [{status}] {tarefas[i]['titulo']}")

def adicionar_tarefa(tarefas):
    nova_tarefa = input("\nO que você precisa fazer? ")

    # Corrigido .script() para .strip()
    if nova_tarefa.strip() != "":
        item = {
            "titulo": nova_tarefa,
            "concluida": False
        }
        tarefas.append(item)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!")
    else:
        print("Você não digitou nada!")

def concluir_tarefa(tarefas): 
    mostrar_tarefas(tarefas)
    if len(tarefas) > 0:
        numero = input("\nDigite o número da tarefa que você concluiu: ")

        if numero.isdigit():
            indice = int(numero) - 1
            if indice >= 0 and indice < len(tarefas):
                tarefas[indice]["concluida"] = True
                salvar_tarefas(tarefas)
                print("Boa! Tarefa concluída.")
            else:
                print("Esse número de tarefa não existe.")
        else:
            print("Por favor, digite apenas números.")

def deletar_tarefas(tarefas):
    mostrar_tarefas(tarefas)
    if len(tarefas) > 0:
        numero = input("\nDigite o número da tarefa para apagar: ")

        if numero.isdigit():
            indice = int(numero) - 1
            if indice >= 0 and indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print(f"Tarefa '{tarefa_removida['titulo']}' apagada!")
            else:
                print("Esse número de tarefa não existe.")
        else:
            print("Por favor, digite apenas números.")


lista_de_tarefas = carregar_tarefas()

opcao = ""
while opcao != "5":
    print("\n-----------------------")
    print("  MEU BANCO DE TAREFAS")
    print("-----------------------")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar como feita")
    print("4. Excluir tarefa")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        mostrar_tarefas(lista_de_tarefas)
    elif opcao == "2":
        adicionar_tarefa(lista_de_tarefas)
    elif opcao == "3":
        concluir_tarefa(lista_de_tarefas)
    elif opcao == "4":
        deletar_tarefas(lista_de_tarefas)
    elif opcao == "5":
        print("Até a próxima!")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")