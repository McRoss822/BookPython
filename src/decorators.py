from datetime import date
from exceptions import OutOfBooksException
import re
from functools import wraps
import logging


def method_log(method):
    """
    decorator for logging function call history
    """

    def wrapper(*args, **kwargs):
        day = date.today()
        logging.basicConfig(filename="call log.txt",
                            format="%(asctime)s %(message)s:",
                            filemode="w")
        logging.info(f"Method called at")
        result = method(*args, **kwargs)
        return result

    return wrapper


def convention_check(func):
    """
    decorator for checking if function name applyies to snake case
    """

    def wrapper(*args, **kwargs):
        name = func.__name__
        if re.search("[a-z]+_[a-z]+", name):
            result = func(*args, **kwargs)
            return result
        print("Function is not snake-case ", func.__name__)

    return wrapper


def exception_logger(exception, mode):
    """
    decorator for logging exceptions history
    """
    def inside(method):
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = method(*args, **kwargs)
            except exception:
                if mode == "file":
                    logging.basicConfig(filename='exceptions.log',
                                        format=f"%(asctime)s:%(levelname)s:"
                                               f"{method.__name__}():%(message)s")
                    logging.error(exception())
                if mode == "console":
                    logging.basicConfig(format=f"%(asctime)s:%(levelname)s:"
                                               f"{method.__name__}():%(message)s")
                    logging.error(exception())
            return result
        return wrapper
    return inside
