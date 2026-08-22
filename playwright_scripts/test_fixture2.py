from playwright.sync_api import Page,expect
import pytest

@pytest.fixture
def open_textbook(page: Page):
    page.goto("https://demoqa.com/text-box")
    yield page
def test_fill_name(open_textbook):
    open_textbook.get_by_placeholder("Full Name").fill("Meenakshi")
    open_textbook.get_by_role("button",name="Submit").click()
    expect(open_textbook.locator("#name")).to_contain_text("Meenakshi")
def test_fill_email(open_textbook):
    open_textbook.get_by_placeholder("name@example.com").fill("test@example.com")
    open_textbook.get_by_role("button",name="Submit").click()
    expect(open_textbook.locator("#email")).to_contain_text("test@example.com")