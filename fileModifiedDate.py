import os
import time
import stat

try:
	modTimesinceEpoc = os.path.getmtime("abc.py")
	modificationTime = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(modTimesinceEpoc))
	print("Son değiştirilme  : ", modificationTime )
except Exception as e:
	print("Dosya bulunamadı")
else:
	pass
finally:
	pass




