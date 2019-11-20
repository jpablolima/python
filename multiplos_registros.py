import sqlite3

dados = [("Pablo", "1234-5678"),
          ("Goku", "9999-8887"),
          ("Vegeta", "7894-5632")]
conexao = sqlite3.connect("agenda.db")
cursor=conexao.cursor()
cursor.executemany('''
        insert into agenda (nome, telefone)
        values(?,?)
        ''', dados)
conexao.commit()
cursor.close()
conexao.close()