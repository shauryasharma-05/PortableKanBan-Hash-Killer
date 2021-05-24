#PortableKanban 4.3.6578.38136 - Encrypted Password Retrieval
#Python3 -m pip install des
#or
#pip install des

import json
import base64
from des import * #python3 -m pip install des, pip install des
import sys

def decode(hash):
	hash = base64.b64decode(hash.encode('utf-8'))
	key = DesKey(b"7ly6UznJ")
	return key.decrypt(hash,initial=b"XuVUm5fR",padding=True).decode('utf-8')

print(decode('XXXXXXXXXXXXXXXXXXXXXX'))

#change this to your encrypted key

