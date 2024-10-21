from database import Database

dados = ("Nescau Achocolatado", 11.50, "Alimento")

banco = Database()
banco.cadastrar_produto(dados)


# op = input("Cadastrar pessoa?: S/N: ").upper()
# while op != "N":
#     nome = input("Digite o nome: ")
#     cpf = input("Digite o cpf: ")
#     email = input("Digite o email: ")
#     profissao = input("Digite a profissao: ")

#     dados = (nome,cpf,email,profissao)

#     banco = Database()
#     banco.cadastrar_pessoa(dados)
#     op = input("Cadastrar outra pessoa?: S/N: ").upper()

# print("Programa finalizado com sucesso")