from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

def take_screenshot(url: str) -> str:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Aguarde o carregamento da página

    # Adicione um timestamp ao nome do arquivo gerado
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    driver.save_screenshot(filename)
    driver.quit()

    return filename

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Tire um screenshot de um site.')
    parser.add_argument('url', help='A URL do site para tirar o screenshot')
    args = parser.parse_args()

    url = args.url
    filename = take_screenshot(url)

    print(f"Screenshot salvo como '{filename}' para a URL {url}")
