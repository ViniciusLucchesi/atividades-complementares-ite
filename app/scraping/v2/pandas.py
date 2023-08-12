import re
import pandas as pd
import numpy as np
from datetime import datetime


# Used by the route: /api/v2/activities
def get_activities(group: int = None) -> list[dict[str, str | int]]:
    df = get_html_table()
    df = format_and_filter_date(df)
    df = create_local_and_city_columns(df)
    df = remove_substrings_from_event_column(df)

    # Extract group and hours
    df['group'] = df['observation'].apply(extract_group)
    df['hours'] = df['observation'].apply(extract_hours)
    
    df.drop('theme', axis=1, inplace=True)
    df.drop('observation', axis=1, inplace=True)

    # Filtering groups by user
    if group is not None:
        df = df[df['group'] == group]
    
    df = df.drop_duplicates(subset=df.columns.difference(['city']))
    df = df.sort_values(by=['hours'], ascending=False)

    return df.to_dict(orient='records')


# Used by some DataFrame columns
def extract_group(text: str) -> str:
    match = re.search(r'Grupo (\d+):', text)
    if match:
        group_number = int(match.group(1))
    else:
        group_number = 0
    return group_number

def extract_hours(text: str) -> str:
    match = re.search(r'Grupo (\d+): (\d+)', text)
    if match:
        hours_number = int(match.group(2))
    else:
        hours_number = 0
    return hours_number


# Used to extract/transform data from DataFrame
def get_html_table() -> pd.DataFrame:
    df = pd.read_html('https://portal.ite.edu.br/atividadescomplementares/atividadesdisponiveis')[0]
    df.columns = ['date', 'theme', 'event', 'professor', 'observation', 'time', 'local']
    return df.reset_index(drop=True)

def format_and_filter_date(df: pd.DataFrame) -> pd.DataFrame:  
    today = datetime.now().date()

    # Concatenating date and time + formatting date
    df['date'] = df['date'].astype(str) + ' ' + df['time'].astype(str)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y %H:%M')
    
    # Generate a new column to remove all activities that has the date before today + formatting date
    df['before_today'] = df['date'].dt.date < today
    df = df[df['before_today'] == False]
    df['date'] = df['date'].dt.strftime('%d/%m/%Y %H:%M')

    # Remove unnecessary columns
    df.drop('before_today', axis=1, inplace=True)
    df.drop('time', axis=1, inplace=True)

    return df

def create_local_and_city_columns(df: pd.DataFrame) -> pd.DataFrame:    
    df['city'] = np.where(
            df['local'].str.contains(' - '), # If contains '-'
            np.where(
                df['local'].str.split('-').str[1].str.strip().str.lower() == 'zoom',
                'Bauru/Botucatu',
                df['local'].str.split('-').str[0].str.strip(), # Extracted city
            ),
            'Bauru' # Default city
        )
    df['local'] = np.where(
            df['local'].str.contains(' - '), 
            df['local'].str.split('-').str[1].str.strip(), 
            df['local']
        )
    return df

def remove_substrings_from_event_column(df: pd.DataFrame) -> pd.DataFrame:
    df['event'] = df['event'].str.replace(pat='( (-|–) (bauru|botucatu)/(online|presencial))', repl='', regex=True, case=False) 
    return df

