from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.locator('//*[@id=":r0:"]')
        email_input.fill("user.name@gmail.com")

        username_input = page.locator('//*[@id=":r1:"]')
        username_input.fill("username")

        password_input = page.locator('//*[@id=":r2:"]')
        password_input.fill("password")

        registration_button = page.get_by_test_id("registration-page-registration-button")
        registration_button.click()

        context.storage_state(path="state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        courses_list_empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_list_empty_icon).to_be_visible()

        courses_list_empty_text = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(courses_list_empty_text).to_be_visible()
        expect(courses_list_empty_text).to_have_text("There is no results")

        courses_list_empty_description_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(courses_list_empty_description_text).to_be_visible()
        expect(courses_list_empty_description_text).to_have_text(
            "Results from the load test pipeline will be displayed here")