#!/usr/bin/env python3
from imports import *
from configs import *
# MESSAGE_TREE is used to create a git topic branch
# associated with a specific SHA256(GPGR+GPGS) message pair
global MESSAGE_TREE

def searchGPGR(GPGR):
    try:
        global r
        request = api.request('search/tweets', {'q':GPGR})
        try:
            with open(GPGR+"_"+btc_unix_time_millis, 'w+') as f:
                f.write(request.text)
                f.close
        except:
            logger.info("TRY GPGR FAILED!")
            pass
    except:
        logger.info("GPGR SEARCH FAILED!")
        pass

def searchGPGS(GPGS):
    try:
        global s
        s = api.request('search/tweets', {'q':GPGS})
        try:
            with open(GPGS+"_"+btc_unix_time_millis, 'w+') as f:
                f.write(s.text)
                f.close
        except:
            logger.info("TRY GPGS FAILED!")
            pass
    except:
        logger.info("GPGS SEARCH FAILED!")
        pass

def DELIMITER_STRIPPER(string):
    # avoiding incorrect SHA256 hashes
    string.strip(":")
    string.strip(".")
    return string.strip(":")

def test_hash_lib():
    TEST_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert TEST_256.digest_size == pow(2,5)
    assert TEST_256.block_size == pow(2,6)
    assert TEST_256.hexdigest() == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    return TEST_256.hexdigest()

def HEX_MESSAGE_TREE(recipient, sender):
    recipient = DELIMITER_STRIPPER(recipient)
    sender = DELIMITER_STRIPPER(sender)

    n_256 = hashlib.sha256()
    if (HEX_LOGGER): logger.info("n_256:")
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # empty string reserved for protocol
    assert n_256.hexdigest() == test_hash_lib()

    # SHA256()+GPGR
    n_256.update(bytes(recipient, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info("n_256+recipient:")
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+GPGS
    n_256.update(bytes(sender, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    # if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info("n_256+recipient+sender:")
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # TODO: populate message tree
    if (HEX_LOGGER): logger.info(n_256.hexdigest())

    MESSAGE_TREE = n_256.hexdigest()
    return n_256.hexdigest()

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
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE
    n_256.update(bytes(message, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE+GPGS
    n_256.update(bytes(sender, 'utf-8'))
    # if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    # if (HEX_LOGGER): logger.info(n_256.digest_size)
    # if (HEX_LOGGER): logger.info(n_256.block_size)

    # TODO: populate message tree
    if (HEX_LOGGER): logger.info(n_256.hexdigest())

    return n_256.hexdigest()

# def message_header():
#     # BODY = str(":GPGR:"+GPGR+':DIGEST:'+DIGEST+':BTC:UNIX:'+BTC_UNIX_TIME_MILLIS()+":GPGS:"+GPGS+":")
#     HEADER = str(":GPGR:DIGEST:BTC_TIME:UNIX_TIME_MILLIS:GPGS:LOC:")
#     if (LOGGER): logger.info(HEADER)
#     return HEADER

def message_header():
    # the HEADER is prepended with GPGR
    # the HEADER is appended with GPGS
    DIGEST = HEX_MESSAGE_DIGEST(GPGR, MESSAGE ,GPGS)
    LOC="https://github.com/0x20bf-org/0x20bf/blob/main/"+GPGR+DIGEST+BTC_TIME()+UNIX_TIME_MILLIS()+GPGS+".txt.gpg"
    # LOC is appended on to DIGEST
    HEADER = str(
        ":"+GPGR+
        ':'+DIGEST+
        ':'+BTC_TIME()+":"+UNIX_TIME_MILLIS()+":"+GPGS+":"+LOC+":")

    if (LOGGER): logger.info(HEADER)
    # HEADER_STRUCTURE = str(":GPGR:DIGEST:BTC_TIME:UNIX_TIME_MILLIS:GPGS:LOC:")
    return HEADER

def tweet_message():
    current_btc_time = BTC_TIME()
    header = message_header()
    # body = message_body()
    if (LOGGER): logger.info(header)
    if (current_btc_time != OBT):
        if (TWEET):
            request = api.request('statuses/update', {'status': header})
            if (request.status_code == 200):
                logger.info('api.request SUCCESS')
            else:
                logger.info('api.request FAILURE')
        else: logger.info("TWEET="+str(TWEET))
    else:
        logger.info('tweetblock_time() FAILURE')

# logger.info(BTC_UNIX_TIME_MILLIS())

# GPGR='4DC9817F' #bitkarrot
# GPGR='BB06757B' #RECIPIENT
# GPGR='7C048F04'
GPGR='4DC9817F' #bitkarrot
logger.info(GPGR)
GPGS='BB06757B' #SENDER
logger.info(GPGS)
MESSAGE='text human readable message'
if (HEX_LOGGER): logger.info(HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS))
# logger.info("HEX_MESSAGE_TREE"+HEX_MESSAGE_TREE(GPGR, GPGS))
HEX_MESSAGE_TREE(GPGR, GPGS)
HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS)
# logger.info(str(message_header()))
# test_hash_lib()
# tweet_block_time()
# message_header()
# tweet_message()
# searchGPGR(GPGR)
# searchGPGS(GPGS)
# logger.info(block_time())
# getMempoolAPI('https://mempool.space/api/v1/difficulty-adjustment', DIFFICULTY)

