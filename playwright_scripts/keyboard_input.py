from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").click()
    page.keyboard.type("tomsmith")
    page.keyboard.press("Tab")
    page.keyboard.type("SuperSecretPassword!")
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    browser.close()