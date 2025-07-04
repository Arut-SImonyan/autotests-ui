from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview Image')

        self.image_upload_info_icon = Image(page, f'{identifier}-image-upload-widget-info-icon', 'Upload Info Icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Upload Info Title')
        self.image_upload_info_description = Text(page, f'{identifier}-image-upload-widget-info-description-text', 'Upload Info Description')

        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload Button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload Input')

    def check_visible(self, is_image_uploaded: bool = False):

        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(text='Tap on "Upload image" button to select file')

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text(text='Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )