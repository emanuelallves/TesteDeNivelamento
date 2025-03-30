import pandas as pd
import glob
import os

def process_file(file_path, output_dir):
    df = pd.read_csv(file_path, delimiter = ';')

    df['VL_SALDO_INICIAL'] = df["VL_SALDO_INICIAL"].str.replace(",", ".").astype(float)
    df['VL_SALDO_FINAL'] = df["VL_SALDO_FINAL"].str.replace(",", ".").astype(float)

    df['DATA'] = pd.to_datetime(df['DATA'], dayfirst = True, errors = 'coerce').dt.strftime('%Y-%m-%d')

    os.makedirs(output_dir, exist_ok = True)
    file_name = f'processed_{os.path.basename(file_path)[-10:]}'

    output_path = os.path.join(output_dir, file_name)

    df.to_csv(output_path, index = False, sep = ';', encoding = 'utf-8')

def process_files_in_directory(input_dir, output_dir):

    files = glob.glob(os.path.join(input_dir, '*.csv'))

    for file in files:
        process_file(file, output_dir)

if __name__ == '__main__':

    input_directory = "./Tasks/banco_de_dados/files/arquivos_demonstracoes_contabeis"
    output_directory = './Tasks/banco_de_dados/files/processed_data'

    process_files_in_directory(input_directory, output_directory)