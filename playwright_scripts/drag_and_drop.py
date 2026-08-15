from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    box_a=page.locator("#column-a")
    box_b=page.locator("#column-b")
    box_a.drag_to(box_b)
    expect(page.locator("#column-a header")).to_have_text("B")
    expect(page.locator("#column-b header")).to_have_text("A")
    page.wait_for_timeout(3000)
    browser.close()
    
    #drag_this.drag_to(drop_here) syntax for drag and drop
    # header is used because Child element — header is the specific child tag inside #column-a where the actual text "A" or "B" lives. 🙂
    