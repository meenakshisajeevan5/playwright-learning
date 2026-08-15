from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = page.get_by_role("button", name="Add Element")
    add_button.click()
    add_button.click()
    add_button.click()
    delete_buttons = page.get_by_role("button", name="Delete")
    expect(delete_buttons).to_have_count(3)
    page.wait_for_timeout(3000)
    browser.close()