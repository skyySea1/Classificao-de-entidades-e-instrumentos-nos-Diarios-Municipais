import requests
from bs4 import BeautifulSoup
import os

# URL do site onde os PDFs estão listados
url = "https://example.com/pagina-com-pdfs"

# Fazer a requisição e obter o HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Criar pasta para salvar os PDFs
os.makedirs("pdfs", exist_ok=True)

# Encontrar e baixar todos os PDFs
for link in soup.find_all("a", href=True):
    if link["href"].endswith(".pdf"):
        pdf_url = link["href"]
        if not pdf_url.startswith("http"):
            pdf_url = url + pdf_url  # Corrigir links relativos

        pdf_response = requests.get(pdf_url)
        pdf_name = os.path.join("pdfs", pdf_url.split("/")[-1])

        with open(pdf_name, "wb") as f:
            f.write(pdf_response.content)

        print(f"Baixado: {pdf_name}")