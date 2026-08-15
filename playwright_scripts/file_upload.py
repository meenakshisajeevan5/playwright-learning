from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("input[type='file']").first.set_input_files("C:/path/to/your/file.txt")
    page.get_by_role("button", name="Upload").click()
    expect(page.locator("#uploaded-files")).to_be_visible()
    page.wait_for_timeout(3000)
    browser.close()