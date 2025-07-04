from playwright.sync_api import Page, expect

from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')

        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-title-text'
        )
        self.preview_image_upload_description = page.get_by_test_id(
            'create-course-preview-image-upload-widget-info-description-text'
        )
        self.preview_image_upload_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )
        self.preview_image_remove_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-remove-button'
        )
        self.preview_image_upload_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')


    def check_visible_image_upload_view(self, is_image_uploaded: bool = False):
        expect(self.preview_image_upload_icon).to_be_visible()

        expect(self.preview_image_upload_title).to_be_visible()
        expect(self.preview_image_upload_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.preview_image_upload_description).to_be_visible()
        expect(self.preview_image_upload_description).to_have_text('Recommended file size 540X300')

        expect(self.preview_image_upload_button).to_be_visible()

        if is_image_uploaded:
            expect(self.preview_image_remove_button).to_be_visible()

    def click_remove_image_button(self):
        self.preview_image_remove_button.click()

    def check_visible_preview_image(self):
        expect(self.preview_image).to_be_visible()

    def upload_preview_image(self, file: str):
        self.preview_image_upload_input.set_input_files(file)


    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        expect(exercise_title_input).to_have_value(title)

        exercise_description_input.fill(description)
        expect(exercise_description_input).to_have_value(description)