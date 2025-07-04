import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course')

    @allure.step("Check enabled or disabled course toolbar view")
    def check_visible(self, is_create_course_disabled=True):

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):

        self.create_course_button.click()