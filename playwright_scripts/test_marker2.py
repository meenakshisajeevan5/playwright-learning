from playwright.sync_api import Page,expect
import pytest

@pytest.mark.smoke
def test_login_page_visible(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page.get_by_role("heading",name="Login Page"))
@pytest.mark.regression
def test_successful_login(page :Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
@pytest.mark.regression
def test_failed_login(page : Page):
     page.goto("https://the-internet.herokuapp.com/login")
     page.locator("#username").fill("tomsmith")
     page.locator("#password").fill("wrongpassword")
     page.get_by_role("button",name="Login").click()
     expect(page).to_have_url("https://the-internet.herokuapp.com/login")
@pytest.mark.skip
def test_logout(page :Page):
    pass