# Verifica se o arquivo existe para depois remover

import os
if os.path.exists("arquivo.txt"):
  os.remove("arquivo.txt")
else:
  print("O arquivo nao existe")