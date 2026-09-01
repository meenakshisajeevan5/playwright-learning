from playwright.sync_api import Page, expect

def test_products_visible(logged_in_page):
    expect(logged_in_page.locator(".inventory_list")).to_be_visible()

def test_cart_visible(logged_in_page):
    expect(logged_in_page.locator(".shopping_cart_link")).to_be_visible()