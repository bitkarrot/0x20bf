#!/usr/bin/env python3
import hashlib

from configs import HEX_LOGGER
from logger import logger


def DELIMITER_STRIPPER(string):
    # avoiding incorrect SHA256 hashes
    string.strip(":")
    string.strip(".")
    return string.strip(":")


def test_hash_lib():
    TEST_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert TEST_256.digest_size == pow(2, 5)
    assert TEST_256.block_size == pow(2, 6)
    assert TEST_256.hexdigest() == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    return TEST_256.hexdigest()


def HEX_MESSAGE_DIGEST(recipient, message, sender):
    recipient = DELIMITER_STRIPPER(recipient)
    message = DELIMITER_STRIPPER(message)
    sender = DELIMITER_STRIPPER(sender)

    n_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert n_256.hexdigest() == test_hash_lib()

    # if (HEX_LOGGER): logger.info("%s",n_256.digest())
    # if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR
    n_256.update(bytes(recipient, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER):
        logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE
    n_256.update(bytes(message, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER):
        logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE+GPGS
    n_256.update(bytes(sender, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER):
        logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # TODO: populate message tree
    if (HEX_LOGGER):
        logger.info(n_256.hexdigest())

    return n_256.hexdigest()
