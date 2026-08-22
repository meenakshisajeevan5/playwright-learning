from playwright.sync_api import Page,expect
import pytest

@pytest.mark.parametrize("username,password,expected_url" ,[
    ("tomsmith","SuperSecretPassword!","https://the-internet.herokuapp.com/secure"),
    ("tomsmith","tomsmith","https://the-internet.herokuapp.com/login"),
    ("wronguser","SuperSecretPassword!","https://the-internet.herokuapp.com/login"),
])
def test_login(page : Page ,username,password,expected_url):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.get_by_role("button",name="Login").click()
    expect(page).to_have_url(expected_url)
