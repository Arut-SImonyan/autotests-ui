from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
import pytest


@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(email="test@email.com", username="username", password="password")
    registration_page.click_registration_button()
