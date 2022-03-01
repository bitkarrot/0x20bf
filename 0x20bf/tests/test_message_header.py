# test_message_header

#from 0x20bf.message_header import test_message_header
from message_header import message_header
from logger import logger
from configs import HEX_LOGGER
from hex_message_digest import HEX_MESSAGE_DIGEST


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
   

def test_message_status():
    result = test_message_header()
    assert result != None
