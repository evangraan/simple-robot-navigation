from .navigation import Navigation
import logging
import os.path
from . import aspects
from .interpreter import Interpreter


class Robot:
    __interpreter: Interpreter = Interpreter()
    __logger: logging.getLogger() = logging.getLogger()
    debug: bool = False
    nav: Navigation = Navigation()

    def __init__(self):
        self.nav.reset()
        self.__configure_logging()
        self.__interpreter.logger = self.__logger
        self.__interpreter.nav = self.nav

    def operate(self, instructions_file: str, debug: bool = False) -> bool:
        self.nav.reset()
        self.debug = debug
        self.__interpreter.debug = debug

        if not instructions_file:
            self.__logger.error('missing instructions file')
            return False

        try:
            return self.__process(instructions_file)

        except IOError:
            self.__logger.error('could not open instructions file')
            return False

    def get_notifications(self) -> [str]:
        for handler in logging.getLogger().handlers:
            handler.flush()

        return aspects.load_file_as_list(aspects.log_file)

    def __process(self, instructions_file: str) -> bool:
        if self.__interpreter.process_instructions_file(instructions_file):
            if self.debug:
                self.__logger.debug('Operations: completed')

            result = self.nav.loops > 0
            self.__logger.info(str(result))
            return result

        self.__logger.info("False")
        return False

    def __configure_logging(self):
        if os.path.isfile(aspects.log_file):
            os.remove(aspects.log_file)

        self.__logger = logging.getLogger(aspects.log_name)
        self.__logger.setLevel(level=logging.DEBUG)
        file_handler = logging.FileHandler(aspects.log_file)
        file_handler.setLevel(logging.DEBUG)
        self.__logger.addHandler(file_handler)
