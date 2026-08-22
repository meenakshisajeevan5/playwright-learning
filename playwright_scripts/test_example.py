from playwright.sync_api import Page,expect
import pytest

@pytest.fixture
def open_heroku(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    yield page
    
def test_login(open_heroku):
    expect(open_heroku.get_by_role("button",name="Login")).to_be_visible()
    