import mysql.connector

class Database():
    def __init__(self,banco = "cadastro"):
        self.banco = banco


    def connect(self):
        self.conn = mysql.connector.connect(host='localhost', database='empresa', user='root', password='')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("conectado com sucesso")
        else:
            print("algo deu erro")


    def desconnect(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada")

        
    def cadastrar_pessoa(self,dados):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO pessoa (nome,cpf,email,profissao) values (%s,%s,%s,%s)', dados)

            self.conn.commit()
            print("cadastrado com sucesso")
            self.desconnect()

        except Exception as err:
            print(f"algo deu errado, {err}")


    def cadastrar_produto(self,dados):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO produto (nome_produto,valor,categoria) values (%s,%s,%s)', dados)

            self.conn.commit()
            print("Produto cadastrado com sucesso")
            self.desconnect()

        except Exception as err:
            print(f"algo deu errado, {err}")


if __name__ == "__main__":
    conexao = Database()
    conexao.cadastrar_pessoa()  