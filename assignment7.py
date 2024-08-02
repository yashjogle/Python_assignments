import pandas as pd
import matplotlib.pyplot as plt
class DataCleaningError(Exception):
    pass
def clean_dataset(df):
    df = df.dropna(subset=['Confirmed', 'Deaths', 'Recovered'])
    df['Country'] = df['Country'].str.title()  
    required_columns = ['Country','Confirmed','Deaths','Recovered','Active','New cases','New deaths','New recovered', 'Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','Confirmed last week','1 week change','1 week % increase','WHO Region']
    if not all(col in df.columns for col in required_columns):
        raise DataCleaningError('Critical columns are missing')
    return df
def save_dataset(df, file_path):
    df.to_csv(file_path, index=False)
def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise DataCleaningError(f'Unable to load dataset:{e}')
def calculate_totals(df):
    total_confirmed = df['Confirmed'].sum()
    total_deaths = df['Deaths'].sum()
    total_recovered = df['Recovered'].sum()
    return total_confirmed, total_deaths, total_recovered
def find_extreme_cases(df):
    highest_cases=df.groupby('Country')['Confirmed'].sum().idxmax()
    lowest_cases=df.groupby('Country')['Confirmed'].sum().idxmin()
    return highest_cases,lowest_cases
def visualize_trends(df):
    total_cases_by_country=df.groupby('Country')['Confirmed'].sum()
    total_cases_by_country.plot(kind='bar', title='Total Confirmed Cases by Country')
    plt.show()
def main():
    input_file_path='C:\programming\yashjogle\yash_internship\clean_covid_data.csv'
    output_file_path='clean_covid_data.csv'
    try:
        df = load_dataset(input_file_path)
        cleaned_df=clean_dataset(df)
        save_dataset(cleaned_df, output_file_path)
    except DataCleaningError as e:
        print(f"Data cleaning error occurred:{e}")
        return
    total_confirmed, total_deaths, total_recovered = calculate_totals(cleaned_df)
    print(f'Total Confirmed Cases: {total_confirmed}')
    print(f'Total Deaths: {total_deaths}')
    print(f'Total Recovered: {total_recovered}')
    highest_cases, lowest_cases = find_extreme_cases(cleaned_df)
    print(f'Country with the highest number of cases:{highest_cases}')
    print(f'Country with the lowest number of cases:{lowest_cases}')
    visualize_trends(cleaned_df)
if __name__ == '_main_':
    main()