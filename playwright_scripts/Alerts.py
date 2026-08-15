from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Click for JS Confirm").click()
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")
    page.once("dialog", lambda dialog: dialog.accept("Meenakshi"))
    page.get_by_role("button", name="Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: Meenakshi")
    page.wait_for_timeout(3000)
    browser.close()