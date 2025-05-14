# Pedro Marrocos - CRUD de Vagas (empresas criam/editam/excluem/listam vagas)

# Lista simulada de vagas só para teste (mais tarde será substituída por dados reais)
vagas = [
    {"titulo": "Desenvolvedor Backend", "empresa": "Empresa X", "local": "São Paulo"},
    {"titulo": "Designer UX", "empresa": "Estúdio Criativo", "local": "Rio de Janeiro"} #json
]

def listar_vagas():
    if not vagas:
        print("Nenhuma vaga cadastrada.")
    else:
        print("=== Lista de Vagas ===")
        for i, vaga in enumerate(vagas, 1):
            print(f"{i}. {vaga['titulo']} - {vaga['empresa']} ({vaga['local']})")

# Menu temporário de teste, enquanto não tem o JSON
def menu():
    while True:
        print("\n1. Listar vagas")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_vagas()
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
