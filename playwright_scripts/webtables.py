from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/webtables")
    expect(page.get_by_role("cell", name="Cierra", exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name="cierra@example.com", exact=True)).to_be_visible()
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_role("dialog")).to_contain_text("Registration Form")
    page.wait_for_timeout(3000)
    browser.close()