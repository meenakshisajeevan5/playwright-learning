from playwright.sync_api import Page, expect

def test_login(login_page):
    expect(login_page.get_by_role("button",name="Login")).to_be_visible()
def test_assert(logged_in_heroku):
    expect(logged_in_heroku).to_have_url("https://the-internet.herokuapp.com/secure")
def test_visible(logged_in_heroku):
    expect(logged_in_heroku.get_by_role("heading",name="Secure Area",exact=True)).to_be_visible()

# Test 1: uses login_page fixture
# Assert the Login button is visible on the login page

# Test 2: uses logged_in_heroku fixture
# Assert URL is "https://the-internet.herokuapp.com/secure"

# Test 3: uses logged_in_heroku fixture
# Assert heading "Secure Area" is visible n