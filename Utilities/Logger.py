import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        log_directory = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "Logs"
        )

        os.makedirs(log_directory, exist_ok=True)

        log_file = os.path.join(
            log_directory,
            "execution.log"
        )

        logger = logging.getLogger()

        # Prevent duplicate logs
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        file_handler = logging.FileHandler(log_file)

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        return logger