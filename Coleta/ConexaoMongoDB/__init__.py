import pymongo
from pymongo import MongoClient
from Coleta import ColetaTodosDados

client = MongoClient('localhost', 27017)
database = client["dataLake"]
collection = database["dataLake_APInasa"]


def salvarDadosMongoDB():
    salvarDados = collection.insert_one(ColetaTodosDados.coletarDados())
    if salvarDados.acknowledged:
        print("Dados salvos com sucesso!")
    else:
        print("Erro ao salvar dados")


def trazerDados():
    print(collection.count_documents({}))
    if collection.count_documents({}) > 0:
        for dados in collection.find():
            print(dados)
