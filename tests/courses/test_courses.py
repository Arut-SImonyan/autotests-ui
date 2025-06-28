import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):

        courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page_with_state.navbar.check_visible('username')
        courses_list_page_with_state.sidebar.check_visible()

        courses_list_page_with_state.check_visible_courses_title()
        courses_list_page_with_state.check_visible_create_course_button()
        courses_list_page_with_state.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.check_visible_image_upload_view()

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.create_course_exercises_toolbar_view.click_create_exercise_button()

        create_course_page.upload_preview_image("D:/autotests-ui/testdata/files/image.png")

        create_course_page.create_course_form.fill(title = "Playwright", estimated_time = "2 weeks", description = "Playwright", max_score = "100", min_score = "10")
        create_course_page.create_course_form.check_visible(title = "Playwright", estimated_time = "2 weeks", description = "Playwright", max_score = "100", min_score = "10")

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.check_visible_courses_title()
        courses_list_page.check_visible_create_course_button()
        courses_list_page.check_visible_course_card(index=0, title ="Playwright", estimated_time ="2 weeks", max_score ="100", min_score ="10")

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_form.fill(title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10")
        create_course_page.create_course_form.check_visible(title="Playwright", estimated_time="2 weeks", description="Playwright", max_score="100", min_score="10")
        create_course_page.upload_preview_image("D:/autotests-ui/testdata/files/image.png")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.check_visible_course_card(index=0, title="Playwright", estimated_time="2 weeks", max_score="100", min_score="10")

        courses_list_page.click_edit_course(index=0)
        create_course_page.create_course_form.fill(title="Python", estimated_time="1 day",description="Python", max_score="10", min_score="5")
        create_course_page.create_course_form.check_visible(title="Python", estimated_time="1 day", description="Python", max_score="10", min_score="5")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.check_visible_course_card(index=0, title="Python", estimated_time="1 day", max_score="10", min_score="5")

