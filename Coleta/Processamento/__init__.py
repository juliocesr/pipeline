import pandas as pd
from Coleta import ColetaTodosDados


def processamento():
    dadosBrutos = ColetaTodosDados.coletarDados()
    dados_processados = []
    for data, obj in dadosBrutos["near_earth_objects"].items():
        for objeto in obj:
            dados_processados.append(objeto)
            dados_processados.append({
                "Nome": objeto["name"],
                "Data": objeto["close_approach_data"][0]["close_approach_date"],
                "Distância (KM)": float(objeto["close_approach_data"][0]["miss_distance"]["kilometers"]),
                "Velocidade (KM/h)": float(objeto["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]),
                "Diâmetro (km)": f"{objeto['estimated_diameter']['kilometers']['estimated_diameter_min']:.2f} - "
                                 f"{objeto['estimated_diameter']['kilometers']['estimated_diameter_max']:.2f}",
                "Perigoso": "Sim" if objeto["is_potentially_hazardous_asteroid"] else "Não"
            })
    df = pd.DataFrame(dados_processados)
    df.to_csv("DadosProcessados.csv", index=False)
