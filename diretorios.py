'''  import os
 os.getcwd() 
 os.chdir('a')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('.\c')
print(os.getcwd())
  '''

 # Criação de Diretorios

''' import os
os.mkdir('d')
os.mkdir('e')
os.mkdir('f')
print(os.getcwd())
os.chdir('d')
print(os.getcwd())
os.chdir('../e')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('f')
print(os.getcwd())
 '''
''' import os
os.makedirs('avo/pai/filho')
os.makedirs('avo/mae/filha') '''

import os
os.mkdir('vingadores')
os.rename('vingadores', 'liga da justiça')