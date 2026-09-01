from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    yield page
@pytest.fixture
def login_page(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    yield page
@pytest.fixture
def logged_in_heroku(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    yield page