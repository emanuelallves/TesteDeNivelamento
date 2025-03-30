import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

cookies = {
    'Encrypted-Local-Storage-Key': '1nobFmfQmy8G6KoEDNznEGk8vqml0qUASNS8tME1BHU',
    'XSRF-TOKEN': '51082e85-564e-4ff7-8ab8-49aacb6fb65a',
    'lgpd-cookie-v2': '{"v":7,"g":[{"id":"cookies-estritamente-necessarios","on":true},{"id":"cookies-de-desempenho","on":true},{"id":"cookies-de-terceiros","on":true}]}',
    '_ga': 'GA1.1.1290568805.1743115444',
    '_ga_WGZPDK4DH1': 'GS1.1.1743115444.1.1.1743116360.60.0.0',
    '_ga_LPHJ6M7WB1': 'GS1.1.1743115444.1.1.1743116360.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'Encrypted-Local-Storage-Key=1nobFmfQmy8G6KoEDNznEGk8vqml0qUASNS8tME1BHU; XSRF-TOKEN=51082e85-564e-4ff7-8ab8-49aacb6fb65a; lgpd-cookie-v2={"v":7,"g":[{"id":"cookies-estritamente-necessarios","on":true},{"id":"cookies-de-desempenho","on":true},{"id":"cookies-de-terceiros","on":true}]}; _ga=GA1.1.1290568805.1743115444; _ga_WGZPDK4DH1=GS1.1.1743115444.1.1.1743116360.60.0.0; _ga_LPHJ6M7WB1=GS1.1.1743115444.1.1.1743116360.0.0.0',
    'Referer': 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0 (Edition std-2)',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Opera GX";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

pdf_files = './Tasks/web_scraping/PDFs'
os.makedirs(pdf_files, exist_ok = True)

def search_page(url):

    resp = requests.get(url,
                        cookies=cookies,
                        headers=headers)
        
    if resp.status_code != 200:
        print('Error')
        return None

    return resp.text

def extract_pdf_links(html):

    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []

    for link in soup.find_all('a'):
        href = link['href']

        if 'Anexo' in href and href.endswith('.pdf'):
            pdf_links.append(urljoin(url, href))

    if not pdf_links:
        print('No PDFs found')
    
    return pdf_links

def download_pdf(pdf_url):
    pdf_name = pdf_url.split('/')[-1]
    pdf_path = os.path.join(pdf_files, pdf_name)

    pdf_resp = requests.get(pdf_url, headers = headers)

    if pdf_resp.status_code == 200:
        with open(pdf_path, 'wb') as file:
            file.write(pdf_resp.content)
        
        print(f'Downloaded {pdf_name}')
    else:
        print(f'Error downloading {pdf_name}')

def compress_files():
    zip_path = './Tasks/web_scraping/anexos.zip'

    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for file in os.listdir(pdf_files):
            zip_file.write(os.path.join(pdf_files, file), file)
        
        print('Compressed files')

if __name__ == '__main__':
    
    html = search_page(url)
    if not html:
        exit()
    
    pdf_links = extract_pdf_links(html)
    if not pdf_links:
        exit()

    for pdf_url in pdf_links:
        download_pdf(pdf_url)
    
    compress_files()
