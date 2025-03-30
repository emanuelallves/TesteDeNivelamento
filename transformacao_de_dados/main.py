import pdfplumber
import pandas as pd
import zipfile

pdf_path = './Tasks/web_scraping/PDFs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
csv_path = './Tasks/transformacao_de_dados/data.csv'
zip_path = './Tasks/transformacao_de_dados/Teste_data.zip'

substitutions = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}

def extract_tables_from_pdf(pdf_path):
    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()

            if table:
                df = pd.DataFrame(table[1:], columns = table[0])
                tables.append(df)
    
    return tables

def save_data(tables, csv_path, substitutions):
    df_final = pd.concat(tables, ignore_index = True)
    df_final.rename(columns = substitutions, inplace = True)
    df_final.to_csv(csv_path, index = True, encoding = 'utf-8')

    return df_final

def create_zip_file(zip_path, csv_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        zip_file.write(csv_path)

if __name__ == '__main__':
    
    tables = extract_tables_from_pdf(pdf_path)
    save_data(tables, csv_path, substitutions)
    create_zip_file(zip_path, csv_path)