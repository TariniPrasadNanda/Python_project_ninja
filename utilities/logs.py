import logging
import inspect
import allure
import pytest


def get_logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False


def allure_log(text):
    with allure.step(text):
        pass


def step_fail(text):
    #ytest.mark.xfail(allure_log())
    pytest.fail(logging.log.error(text))
