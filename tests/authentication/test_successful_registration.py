import allure
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):

        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="test@email.com", username="username", password="password")
        registration_page.registration_button.click()
