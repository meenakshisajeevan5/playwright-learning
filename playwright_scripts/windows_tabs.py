from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/windows")
    page.get_by_role("link", name="Click Here").click()
    page.wait_for_timeout(2000)
    all_pages = context.pages
    new_page = all_pages[1]
    new_page.wait_for_load_state()
    new_page.bring_to_front()
    expect(new_page.get_by_role("heading", name="New Window")).to_be_visible()
    print("Original tab title:", page.title())
    print("New tab title:", new_page.title())
    browser.close()