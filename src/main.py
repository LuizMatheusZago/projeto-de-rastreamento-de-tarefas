def ler(mensagem):
    return " ".join(input(mensagem).split())


def exibir_menu():
    print("\n===== HELPDESK SIMPLES =====")
    print("1. Cadastrar novo chamado")
    print("2. Visualizar chamados cadastrados")
    print("3. Sair da aplicação")


def cadastrar_chamado(chamados):
    print("\n--- Novo Chamado ---")

    titulo = ler("Título do problema: ")
    while titulo == "":
        print("❌ O título não pode ser vazio.")
        titulo = ler("Título do problema: ")

    descricao = ler("Descrição detalhada: ")

    prioridade = ler("Prioridade (Alta, Média ou Baixa): ").capitalize()
    while prioridade not in ("Alta", "Média", "Media", "Baixa"):
        print("❌ Prioridade inválida! Use Alta, Média ou Baixa.")
        prioridade = ler("Prioridade (Alta, Média ou Baixa): ").capitalize()
    if prioridade == "Media":
        prioridade = "Média"

    data_limite = ler("Data limite para resolver (ex: 20/12/2026): ")

    chamados.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    })
    print("✔ Chamado cadastrado com sucesso!")


def listar_chamados(chamados):
    print("\n--- Chamados Cadastrados ---")

    if not chamados:
        print("Nenhum chamado cadastrado no momento.")
        return

    for i, chamado in enumerate(chamados, start=1):
        print(f"\nChamado {i}")
        print(f"  Título:      {chamado['titulo']}")
        print(f"  Descrição:   {chamado['descricao'] or 'N/A'}")
        print(f"  Prioridade:  {chamado['prioridade']}")
        print(f"  Data limite: {chamado['data_limite'] or 'N/A'}")
        print(f"  Status:      {chamado['status']}")


def main():
    chamados = []

    while True:
        exibir_menu()
        opcao = ler("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_chamado(chamados)
        elif opcao == "2":
            listar_chamados(chamados)
        elif opcao == "3":
            print("Saindo da aplicação. Até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nAplicação encerrada. Até logo!")
