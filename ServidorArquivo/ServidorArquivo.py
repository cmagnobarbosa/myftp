# -*- coding: utf-8 -*-
from xmlrpc.server import SimpleXMLRPCServer
import sys
import os

#usado para deletar, cuidado ao utilizar
import shutil

class ServidorArquivo(object):
    """docstring for ServidorArquivo."""
    def __init__(self):
        #o caminho final será self.caminho+nome_usuario+"/"
        self.caminho="home/"

    def setCaminho(self,nome_usuario):
        """define o caminho da home a partir do nome do usuário"""
        self.caminho+=nome_usuario+"/"
    def gera_caminho(self,lista):
        return "/".join(lista)

    def ls(self,home):
        """lista os arquivos no diretorio"""
        print("Ls",home)
        arquivos=os.listdir(home)
        return arquivos

    def cd(self,caminho):
        """caminha pela home"""
        if(".." in caminho):
            path=caminho.split("/")
            print("len",len(path))
            if(len(path)==2):
                print("erro")
                return False,None
            path.pop()
            if(len(path)>2):
                path.pop()
            return True,self.gera_caminho(path)+"/"

        elif(os.path.exists(caminho)):
            print("caminho",caminho)
            return True,caminho+"/"
        else:
            return False
    def mkdir(self,nome):
        """cria um diretorio"""
        print("mkdir")
        try:
            os.mkdir(nome)
            return True
        except Exception as e:
            return False
    def delete(self,nome):
        try:
            os.remove(nome)
            return True
        except Exception as e:
            return False
    def rmdir(self,nome):
        """apaga um diretorio"""
        print("rmdir-- usando shutil")
        try:
            shutil.rmtree(nome)
            return True
        except Exception as e:
            return False

    def get(self,caminho):
        """abre e retorna um arquivo"""
        try:
            arquivo=open(caminho,"rb")
            file=arquivo.read()
            arquivo.close()
            return True,file
        except Exception as e:
            return False,None


    def getCaminho(self):
        """retorna o caminho da home"""
        return self.caminho

    def comandos_validos(self):
        pass


#porta onde o mesmo está sendo executado
porta=8001
#Chama de procedimendo remoto RPC
server= SimpleXMLRPCServer(("localhost",porta))
print("Servidor de arquivo executando na porta",porta)
#registra a instância do Servidor de senha para RPC
#Todos os métodos da classe se tornam acessiveis.
server.register_instance(ServidorArquivo())
#deixa o servidor de senha em loop
server.serve_forever()

# teste= ServidorArquivo()
# teste.setCaminho("zeus")
# teste.getCaminho()
# teste.ls()
# #teste.ls()
