import pandas as pd
import os

def process_file(file_path, output_dir):
    df = pd.read_csv(file_path, delimiter = ';')

    df['Data_Registro_ANS'] = pd.to_datetime(df['Data_Registro_ANS'],
                                             format = '%Y-%m-%d',
                                             errors = 'coerce').dt.strftime('%Y-%m-%d')
    df['DDD'] = df['DDD'].fillna(0).astype(int)

    os.makedirs(output_dir, exist_ok = True)
    file_name = f'processed_{os.path.basename(file_path)[-19:]}'

    output_path = os.path.join(output_dir, file_name)

    df.to_csv(output_path, index = False, sep = ';', encoding = 'utf-8')

if __name__ == '__main__':

    input_file = './Tasks/banco_de_dados/files/Relatorio_cadop.csv'
    output_directory = './Tasks/banco_de_dados/files/processed_data'

    process_file(input_file, output_directory)