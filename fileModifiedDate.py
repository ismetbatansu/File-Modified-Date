import os
import time
import stat


modTimesinceEpoc = os.path.getmtime("text.txt")
modificationTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTimesinceEpoc))
print("Son değiştirilme  : ", modificationTime )



