b3b3 = __import__("0x20bf")
logger = __import__("logger")


def test_version():
    assert b3b3.__version__ == "0.1.0"
    logger.info(b3b3.__version__)
