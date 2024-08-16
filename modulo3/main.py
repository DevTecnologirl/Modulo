import os
if os.path.exists("folderExemplo"):
  os.remove("folderExemplo")
else:
  print("A pasta nao existe")