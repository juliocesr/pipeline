from Coleta import ColetaTodosDados
from Coleta import ProcessamentoDataLake
from Coleta import ConexaoMongoDB
from Coleta import ConexaoPostgresSQL

if __name__ == "__main__":
    ConexaoPostgresSQL.conecxaoPostgres()
    # ProcessamentoDataLake.processamento()
    # ColetaTodosDados.coletarDados()