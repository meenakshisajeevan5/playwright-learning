from playwright.sync_api import Page,expect
import pytest

@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()
    yield page
    
def test_products_visible(logged_in_page: Page):
    expect(logged_in_page.locator(".inventory_list")).to_be_visible()
    
def test_cart_visible(logged_in_page: Page):
    expect(logged_in_page.locator(".shopping_cart_link")).to_be_visible()
    