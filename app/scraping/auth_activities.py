import httpx
import pandas as pd


# Used by the route: /api/v2/activities/auth
def get_activities_link(payload: dict[str, str]) -> list[dict[str, str|int]] | list[dict[str, str]]:
    html_content = get_html_content(payload)
    df = extract_table_from_content(html_content)

    if isinstance(df, list):
        return df

    df = format_and_filter_dataframe(df)
    return df.to_dict(orient='records')


# Used to extract/transform data from DataFrame
def get_html_content(payload: dict[str, str]) -> str:
    client = httpx.Client()

    reqLogin = "https://portal.ite.edu.br//atividadescomplementares/Login"
    reqUrl = "https://portal.ite.edu.br//atividadescomplementares/Index"

    headersList = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0" 
    }

    _ = client.post(reqLogin, data=payload, headers=headersList)
    data = client.get(reqUrl)

    return data.text

def extract_table_from_content(html_content: str) -> pd.DataFrame | list[dict[str, str]]:
    try:
        df = pd.read_html(html_content, extract_links="body")[0]
        df.columns = ['activity', 'group', 'event', 'event_url', 'year', 'remaining_vacancies']
        return df.reset_index(drop=True)
    except:
        return [{"error": "Matricula ou senha incorretos"}]

def format_and_filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Droping
    df.drop(columns=['activity', 'year'], inplace=True)
    
    # Formating
    df['group'] = df['group'].apply(extract_first_value).apply(format_group_from_str_to_int)
    df['event'] = df['event'].apply(extract_first_value)
    df['event_url'] = df['event_url'].apply(extract_first_value).apply(format_link)
    df['remaining_vacancies'] = df['remaining_vacancies'].apply(extract_first_value).astype(int)
    
    # Filtering
    df = df[df['remaining_vacancies'] > 0]

    return df


# Used by some DataFrame columns
def format_link(link: str) -> str:
    if link is not None:
        formated_link = link[2::].replace(' ', '%20')
        return f"https://portal.ite.edu.br/atividadescomplementares/{formated_link}"
    return "N/A"

def extract_first_value(column: tuple[str, str]) -> str:
    if column[1] is None:
        return column[0]
    else:
        return column[1]

def format_group_from_str_to_int(text: str) -> int:
    match text:
        case "Extensão":
            return 3
        case "Pesquisa":
            return 2
        case "Ensino":
            return 1




if __name__ == "__main__":
    payload = {
        "matricula": "010620005",
        "password": "7946852"
    }

    df = get_activities_link(payload)
    print(df)