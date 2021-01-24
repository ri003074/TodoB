from .base import *  # noqa
import logging

DEBUG = True

ACCOUNT_EMAIL_VERIFICATION = "none"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)
