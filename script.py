from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from datetime import datetime
import argparse


def take_screenshot(url: str) -> str:
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    with webdriver.Firefox(options=firefox_options) as driver:
        driver.get(url)

        # Wait for the page to finish loading
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Add a timestamp to the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"

        # Save the screenshot and return the filename
        driver.save_screenshot(filename)
        return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Capture a screenshot of a website.')
    parser.add_argument('url', help='The URL of the website to capture')
    args = parser.parse_args()

    url = args.url
    filename = take_screenshot(url)

    print(f"Screenshot saved as '{filename}' for the URL {url}")
