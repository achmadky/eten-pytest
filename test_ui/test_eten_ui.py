# tests_ui/test_eten_ui.py

from selenium import webdriver

def test_home_page_load():
    driver = webdriver.Chrome()  # You can use other browsers too
    driver.get("https://eten-ui.vercel.app/")
    # assert "Eten" in driver.title
    driver.quit()
