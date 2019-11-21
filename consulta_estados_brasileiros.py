import sqlite3 
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
print("%3s %-20s %12s" % ("Id", "Estado", "População"))
print("="*37)
for estado in conexao.execute("select * from estados order by nome"):
  print("%3d %-20s %12d" %
    (estado["id"],
    estado["nome"],
    estado["populacao"]))
conexao.close