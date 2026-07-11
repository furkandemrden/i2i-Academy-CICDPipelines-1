from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_domain_page_loads():
    """
    Launch a headless Chrome browser, navigate to https://example.com
    and verify that the page loads correctly by checking its title.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium 4.6+ automatically manages the correct chromedriver version.
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")
        assert "Example Domain" in driver.title
    finally:
        driver.quit()
