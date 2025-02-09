from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os

# Configurar o WebDriver
driver = webdriver.Chrome()
driver.get("https://example.com/pagina-com-pdfs")

# Criar pasta para salvar os PDFs
os.makedirs("pdfs", exist_ok=True)

# Esperar carregar e pegar links de PDF
pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")

for link in pdf_links:
    pdf_url = link.get_attribute("href")
    pdf_name = os.path.join("pdfs", pdf_url.split("/")[-1])

    pdf_response = requests.get(pdf_url)
    with open(pdf_name, "wb") as f:
        f.write(pdf_response.content)

    print(f"Baixado: {pdf_name}")

driver.quit()
