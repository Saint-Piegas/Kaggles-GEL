import os
from zipfile import ZipFile

#É IMPORTANTE QUE VC TENHA FEITO O PASSO A PASSO DAS CONFIGURAÇÕES DAS VARIAVEIS DE AMBIENTE DO KAGGLE
from kaggle.api.kaggle_api_extended import KaggleApi

COMPETITION = "spaceship-titanic"
DONWLOAD_PATH = "./SpaceshipTitanic/Data"

def BaixaDados(competition, download_path):
    api = KaggleApi()
    api.authenticate()  # Autenticar usando o arquivo kaggle.json
    api.competition_download_files(competition, path=download_path)
    
    # Extrair o arquivo ZIP baixado
    zip_file_path = os.path.join(download_path, f"{competition}.zip")
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    os.remove(zip_file_path)
    print(f"Dados da competição {competition} baixados e extraídos em {download_path}")
    
if __name__ == "__main__":
    BaixaDados(COMPETITION, DONWLOAD_PATH)