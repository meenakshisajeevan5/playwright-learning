from playwright.sync_api import Page,expect
import pytest

@pytest.mark.parametrize("username, expected_url", [
    ("standard_user" ,    "https://www.saucedemo.com/inventory.html"),
    ("problem_user" ,      "https://www.saucedemo.com/inventory.html"),
    ("performance_glitch_user",  "https://www.saucedemo.com/inventory.html"),
])
def test_login(page: Page, username, expected_url):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()
    expect(page).to_have_url(expected_url)