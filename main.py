# main.py

import os
import shutil
from datetime import datetime

# Caminho base da pasta onde ficarão os documentos
BASE_DIR = "C:\\Users\\adzo-\\sistema-gerenciamento-biblioteca\\documentos"

# Função para listar documentos organizados por tipo e ano de modificação
def listar_documentos():
    print("\nDocumentos encontrados:\n")
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            tipo = file.split('.')[-1].upper()
            ano_modificacao = datetime.fromtimestamp(os.path.getmtime(file_path)).year
            print(f"Arquivo: {file} | Tipo: {tipo} | Ano: {ano_modificacao}")

# Função para adicionar um documento (copia de um caminho informado para a pasta BASE_DIR)
def adicionar_documento(caminho_origem):
    if os.path.isfile(caminho_origem):
        shutil.copy(caminho_origem, BASE_DIR)
        print("Documento adicionado com sucesso.")
    else:
        print("Erro: Caminho inválido ou arquivo não encontrado.")

# Função para renomear um documento
def renomear_documento(nome_atual, novo_nome):
    caminho_atual = os.path.join(BASE_DIR, nome_atual)
    caminho_novo = os.path.join(BASE_DIR, novo_nome)
    if os.path.isfile(caminho_atual):
        os.rename(caminho_atual, caminho_novo)
        print("Documento renomeado com sucesso.")
    else:
        print("Erro: Documento não encontrado.")

# Função para remover um documento
def remover_documento(nome_documento):
    caminho = os.path.join(BASE_DIR, nome_documento)
    if os.path.isfile(caminho):
        os.remove(caminho)
        print("Documento removido com sucesso.")
    else:
        print("Erro: Documento não encontrado.")

# Interface de linha de comando (CLI)
def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Biblioteca Digital ===")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Renomear documento")
        print("4. Remover documento")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_documentos()
        elif opcao == '2':
            caminho = input("Informe o caminho completo do arquivo a ser adicionado: ")
            adicionar_documento(caminho)
        elif opcao == '3':
            nome_atual = input("Informe o nome atual do documento: ")
            novo_nome = input("Informe o novo nome do documento: ")
            renomear_documento(nome_atual, novo_nome)
        elif opcao == '4':
            nome_documento = input("Informe o nome do documento a ser removido: ")
            remover_documento(nome_documento)
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
