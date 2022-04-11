import mysql.connector
from zmq import CURVE

conexao = mysql.connector.connect( host='localhost', user='root', password='2251',database='bd_precos')
cursor = conexao.cursor()

#=====================================================================
def CREATE(produto, valor):
    comando = f'INSERT INTO tb_precos(PRODUTO, VALOR) VALUES("{produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()
def READ():
    comando = 'SELECT * FROM tb_precos'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
def UPDATE():
    opcao = int(input('[1]-Produto [2]-Preço  [3]-ID  [9]-Sair?'))
    if opcao ==1:
        antigo = input('Qual produto deseja alterar? ')
        nome = input('Qual novo nome deseja? ')
        comando = f'UPDATE tb_precos SET PRODUTO = "{nome}" WHERE PRODUTO = "{antigo}"'
        cursor.execute(comando)
        conexao.commit()
    elif opcao == 2:
        antigo = input('Qual produto deseja alterar? ')
        valor = float(input('Qual valor deseja?'))
        comando = f'UPDATE tb_precos SET VALOR = {valor} WHERE PRODUTO = "{antigo}"'
        cursor.execute(comando)
        conexao.commit()
    elif opcao == 3:
        antigo = input('Qual ID deseja alterar? ')
        valor = float(input('Qual valor deseja?'))
        comando = f'UPDATE tb_precos SET ID = {valor} WHERE ID = "{antigo}"'
        cursor.execute(comando)
        conexao.commit()

    elif opcao == 9:
        print('Saiu !')
    else:
        print('Opçao Invalida')
def DELETE():
    antigo = input('Qual produto deseja deletar? ')
    comando = f'DELETE FROM tb_precos WHERE PRODUTO = "{antigo}"'
    cursor.execute(comando)
    conexao.commit()
#========================================================================
#CREATE("",)
#READ()
#UPDATE()
#DELETE()
cursor.close()
conexao.close()