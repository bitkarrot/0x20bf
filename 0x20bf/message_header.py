from configs import HEX_LOGGER, LOGGER
from hex_message_digest import HEX_MESSAGE_DIGEST
from time_functions import BTC_TIME, UNIX_TIME_MILLIS


def message_header(GPGR, MESSAGE, GPGS, LOC):
    # the HEADER is prepended with GPGR
    # the HEADER is appended with GPGS
    DIGEST = HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS)
    if LOGGER:
        logger.info(DIGEST)
    # TODO branch will be dynamic based on message tree - tbd
    # LOC isnt nesseccsarally a web asset
    # LOC is just a string - maybe a geo location for example
    BRANCH = "main"
    LOC = "https://github.com/0x20bf-org/0x20bf/blob/" + BRANCH
    # LOC is appended on to DIGEST
    HEADER = str(
        ":"
        + GPGR
        + ":"
        + DIGEST
        + ":"
        + str(BTC_TIME())
        + ":"
        + UNIX_TIME_MILLIS()
        + ":"
        + GPGS
        + ":"
        + LOC
        + ":"
    )

    if LOGGER:
        logger.info(HEADER)
    # ":GPGR:DIGEST:BTC_TIME:UNIX_TIME_MILLIS:GPGS:LOC:"
    return HEADER


def test_message_header():
    logger.info("test_message_header()")
    GPGR = "4DC9817F"  # bitkarrot
    logger.info(GPGR)
    GPGS = "BB06757B"  # randymcmillan
    logger.info(GPGS)
    MESSAGE = "text human readable message"
    if HEX_LOGGER:
        logger.info(HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS))
    logger.info(str(message_header(GPGR, MESSAGE, GPGS, "test/location")))
    return message_header(GPGR, MESSAGE, GPGS, "test/location")


logger.info(test_message_header())
