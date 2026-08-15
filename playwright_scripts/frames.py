from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/frames")
    frame = page.frame_locator("#frame1")
    expect(frame.get_by_role("heading", name="This is a sample page")).to_be_visible()
    page.wait_for_timeout(3000)
    browser.close()