import sqlite3
dados =[["São Paulo",44396484],["Minas Gerais",20869101],
["Rio de Janeiro",16550024],["Bahia Bahia",16550024],
["Rio Grande do Sul",15203934],["Paraná",11247972],
["Pernambuco",11163018],["Ceará",9345173],
["Pará",8904459],["Maranhão",8175113],
["Santa Catarina",6904241],["Goiás",6819190],
["Paraíba",6610681],["Amazonas",3972202],
["Espírito Santo",3938336],["Rio Grande do Norte",3929911],
["Alagoas",3442175],["Mato Grosso",3340932],
["Piauí",3270973],["Distrito Federal",3204028],
["Mato Grosso do Sul",2914830],["Sergipe",2651235],
["Rondônia",2242937],["Tocantins",1768204],
["Acre",1515126],["Amapá",803513],
["Roraima",505665]]

conexao = sqlite3.connect("brasil.db")
conexao.row_factory=sqlite3.Row
cursor = conexao.cursor()
cursor.execute(""" create table estados(
               id integer primary key autoincrement, 
               nome text, 
               populacao integer  
)""")
cursor.executemany(" insert into estados(nome, populacao) values(?,?)", dados)
conexao.commit()
cursor.close()
conexao.close()


























