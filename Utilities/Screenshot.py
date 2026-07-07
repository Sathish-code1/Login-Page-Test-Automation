import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        project_path = os.path.dirname(os.path.dirname(__file__))

        screenshot_folder = os.path.join(
            project_path,
            "Screenshots"
        )

        os.makedirs(screenshot_folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{test_name}_{timestamp}.png"

        file_path = os.path.join(
            screenshot_folder,
            filename
        )

        driver.save_screenshot(file_path)

        return file_path