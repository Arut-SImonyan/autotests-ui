from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator('//*[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//*[@id=":r1:"]')
    username_input.fill("username")

    password_input = page.locator('//*[@id=":r2:"]')
    password_input.fill("password")

    registration_button = page.locator('//*[@id="registration-page-registration-button"]')
    registration_button.click()

    dashboard = page.locator('//*[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard).to_be_visible()
    expect(dashboard).to_have_text("Dashboard")
