import re
import io
import httpx
import pandas as pd
from tqdm import tqdm
from PyPDF2 import PdfReader
from dotenv import load_dotenv



class ScraperInscriptions:
    def __init__(self, payload: dict[str, str]) -> None:
        load_dotenv()
        self.payload = payload
    

    def activities(self) -> list[dict[str, str]]:
        html_content = self.get_html_content()
        df_formated = self.extract_table_from_content(html_content)
        return df_formated.to_dict(orient='records')

    def get_inscriptions(self) -> list[dict[str, str]]:
        html_content = self.get_html_content()
        df_formated = self.extract_table_from_content(html_content)

        df_list = []
        for i in tqdm(range(len(df_formated)), desc="Processando PDF"):
            pdf_object = self.get_pdf_content(df_formated['protocolo'][i])
            pdf_text_content = pdf_object.pages[0].extract_text()

            pdf_dict = self.convert_text_to_dict(pdf_text_content)
            df = self.convert_dict_to_dataframe(pdf_dict)
            df['atividade'] = df_formated['atividade'][i]
            df_list.append(df)
        
        df = pd.concat(df_list).sort_values(by=['data'], ascending=True)
        return df.to_dict(orient='records')
        

    # Converting functions
    def convert_text_to_dict(self, text: str) -> dict:
        data = {}
        for line in text.split("\n"):
            key_match = re.search(r"^(.*?):", line)
            value_match = re.search(r":\s*(.*)$", line)
            if key_match and value_match:
                data[key_match.group(1).strip()] = value_match.group(1).strip()
        
        data.setdefault('Link', None)
        data.setdefault('Senha Link', None)
        # if 'Link' not in data:
        #     data['Link'] = None
        # if 'Senha Link' not in data:
        #     data['Senha Link'] = None

        return data

    def convert_dict_to_dataframe(self, pdf_dict: dict) -> pd.DataFrame:
        df = pd.DataFrame.from_dict([pdf_dict])
        df = df.loc[:, ['Evento', 'Palestrante', 'Local', 'Data', 'Horário', 'Créditos', 'Grupo', 'Link', 'Senha Link']]
        df.columns = ['evento', 'palestrante', 'local', 'data', 'horário', 'créditos', 'grupo', 'link', 'senha']
        df['grupo'] = df['grupo'].apply(lambda x: {'Extensão': 3, 'Pesquisa': 2, 'Ensino': 1}[x])
        df['créditos'] = df['créditos'].astype(int)
        return df


    # Scraping functions
    def get_html_content(self) -> str:
        client = httpx.Client()

        reqLogin = "https://portal.ite.edu.br/atividadescomplementares/Login"
        reqUrl = "https://portal.ite.edu.br/atividadescomplementares/EventosInscrito"

        headersList = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0" 
        }

        _ = client.post(reqLogin, data=self.payload, headers=headersList)
        data = client.get(reqUrl)
        return data.text

    def get_pdf_content(self, url: str) -> PdfReader | str:
        client = httpx.Client()

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
        }
        reqLogin = "https://portal.ite.edu.br/atividadescomplementares/Login"
        _ = client.post(reqLogin, data=self.payload, headers=headers)
        response = client.get(url=url, headers=headers, timeout=120)    
        on_fly_mem_obj = io.BytesIO(response.content)
        try:
            pdf_file = PdfReader(on_fly_mem_obj)
            return pdf_file
        except Exception as e:
            print(f"Error: {e}")
            return "N/A"


    # Extracting/Transforming data from DataFrame
    def extract_table_from_content(self, html_content: str) -> pd.DataFrame | list[dict[str, str]]:
        try:
            df = pd.read_html(html_content, extract_links='body')[0]
            df.columns = ['atividade', 'grupo', 'item', 'evento', 'vagas', 'inscrições', 'créditos', 'início das inscrições', 'fim das inscrições', 'invest.', 'comp. faltas', 'protocolo', 'remover inscrição']
            
            # News
            df.drop(columns=['grupo', 'item', 'evento', 'vagas', 'inscrições', 'créditos', 'início das inscrições', 'fim das inscrições', 'invest.', 'comp. faltas', 'remover inscrição'], inplace=True)
            df['protocolo'] = df['protocolo'].apply(lambda x: x[0] if x[1] is None else x[1]).apply(lambda x: f'https://portal.ite.edu.br/atividadescomplementares/{str(x[2:]).replace(" ", "%20") if x is not None else "N/A"}').str.strip()
            df['atividade'] = df['atividade'].apply(lambda x: x[0] if x[1] is None else x[1]).apply(lambda x: str(x).replace(' ', '_')).str.strip()

            return df
        except Exception as e:
            print(e)
            return [{"error": "Matricula ou senha incorretos"}]
