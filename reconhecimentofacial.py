#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform

if platform.system() == "Windows":
   print("[!] - Desculpe! Este programa não está disponível para Windows.")
else:
   pass

try:
   import face_recognition as fr
except ImportError:
   print("[!] - Necessário a biblioteca: face_recognition.")
   print("[D] - Inicializando download..."+"\n")
   os.system("wget https://bootstrap.pypa.io/get-pip.py")
   os.system("sudo python get-pip.py")
   os.system("sudo pip3 install face_recognition")
   os.system("clear")

class FaceRecog:
    def __init__(self):
#       print("[+][+][+][+][+][+][+][+]")
#	print("[+]		    [+]")
#	print("[+]  Reconhecimento  [+]")
#	print("[+]      Facial	    [+]")
#	print("[+]  Teste Neymar Jr [+]")
#	print("[+]		    [+]")
#	print("[+] With Face Recogn.[+]")
#	print("[+][+][+][+][+][+][+][+]\n")

	neymar = fr.load_image_file("neymar.jpg")
	neymar_encode = fr.face_encodings(neymar)[0]

	neymar2 = fr.load_image_file("neymar2.jpg")
	neymar2_encode = fr.face_encodings(neymar2)[0]

	comparacao = fr.compare_faces([neymar_encode,neymar2_encode])

	if comparacao[0] == True:
	   print("[+] - É o Neymar Jr!")
	else:
	   print("[+] - Não é o Neymar Jr!")

if __name__ == "__main__":
    FaceRecog()
