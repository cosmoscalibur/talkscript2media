#storage

import os

def storange():

	Ruta = [r'tests/audio',r'tests/img',r'tests/text']


	for i in Ruta:

		if not os.path.exists(i): os.makedirs(i)


storange()
