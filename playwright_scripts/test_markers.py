from playwright.sync_api import Page,expect
import pytest

@pytest.mark.smoke
def test_login_smoke(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.regression
def test_login_regression(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("problem_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
@pytest.mark.skip(reason="feature not built yet")
def test_payment(page :Page):
    pass