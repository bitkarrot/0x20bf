#!/usr/bin/env python3
from imports import *
from configs import *

# Setup logging
global LOGGER
global HEX_LOGGER
global TIME_LOGGER
global MEMPOOL_LOGGER
LOGGER = True
HEX_LOGGER = False
TIME_LOGGER = False
MEMPOOL_LOGGER = False
logging.basicConfig(level=logging.INFO ,format='%(asctime)s %(message)s', datefmt='%j.%Y %I:%M:%S %p')
logger = logging.getLogger()
global TWEET
TWEET = False

# MESSAGE_TREE is used to create a git topic branch
# associated with a specific SHA256(GPGR+GPGS) message pair
global MESSAGE_TREE

try:
    # TODO finish session_id_lock
    session_id_lock  = getData(SESSION_ID_LOCK)
    if (session_id_lock == str(0)): logger.info(session_id_lock+"eq")
    if (session_id_lock != str(0)): logger.info(session_id_lock+"neq")
except:
    logger.info(session_id_lock+"except")

api  = TwitterAPI(CAK,CASK,AT,ATS)
# if (LOGGER): print(api)

def moveblock_time():
    try:
        shutil.move(os.getcwd()+"/BLOCK_TIME", os.getcwd()+"/OLD_BLOCK_TIME")
    except:
        logger.info("moveblock_time() failed!")
        f = open("BLOCK_TIME", "w")
        f.write("" + 0 + "\n")
        f.close()
        pass

def getMillis():
    global millis
    millis = int(round(time.time() * 1000))
    return millis

def getSeconds():
    global seconds
    seconds = int(round(time.time()))
    return seconds

def blockcypher_height():
    global block_time
    global blockcypher_height
    try:
        # block_cypher = blockcypher.get_latest_blockcypher_height(coin_symbol='btc')
        block_cypher = blockcypher.get_latest_blockcypher_height()
        # logger.info(block_cypher)
        blockcypher_height = repr(block_cypher)
        f = open("BLOCK_TIME", "w")
        f.write("" + blockcypher_height + "\n")
        f.close()
        return blockcypher_height
    except:
        return 0
        pass

def mempool_height():
    # curl -sSL "https://mempool.space/api/blocks/tip/height"
    if (MEMPOOL_LOGGER): logger.info(url)
    url = "https://mempool.space/api/blocks/tip/height"
    try:
        request = requests.get(url, stream=True)
    except:
        return 0
        pass
    return request.text

def BTC_TIME():
    global btc_time
    btc_time = str(block_time())
    return btc_time

def BTC_UNIX_TIME_MILLIS():
    global btc_unix_time_millis
    global SESSION_ID
    btc_unix_time_millis = str(BTC_TIME())+":"+str(getMillis())
    SESSION_ID = btc_unix_time_millis
    f = open("SESSION_ID", "w")
    f.write("" + SESSION_ID + "\n")
    f.close()
    f = open("SESSION_ID.lock", "w")
    f.write("" + SESSION_ID + "\n")
    f.close()
    return btc_unix_time_millis

def BTC_UNIX_TIME_SECONDS():
    global btc_unix_time_seconds
    btc_unix_time_seconds = str(BTC_TIME())+":"+str(getSeconds())
    return btc_unix_time_seconds

def UNIX_TIME_MILLIS():
    global unix_time_millis
    unix_time_millis = str(getMillis())
    return unix_time_millis

def UNIX_TIME_SECONDS():
    global unix_time_seconds
    unix_time_seconds = str(getSeconds())
    return unix_time_seconds

def tweet_block_time():
    if BTC_TIME() != OBT:
        request = api.request('statuses/update', {'status': BTC_UNIX_TIME_MILLIS()})
        if (LOGGER): logger.info(request)
        if (request.status_code == 200):
            logger.info('api.request SUCCESS')
        else:
            logger.info('api.request FAILURE')
    else:
        logger.info('tweetblock_time() FAILURE')

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

if (TIME_LOGGER): logger.info(block_time())
if (TIME_LOGGER): logger.info(getMillis())
if (TIME_LOGGER): logger.info(getSeconds())

def test_hash_lib():
    TEST_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert TEST_256.digest_size == pow(2,5)
    assert TEST_256.block_size == pow(2,6)
    assert TEST_256.hexdigest() == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    return TEST_256.hexdigest()


def DELIMITER_STRIPPER(string):
    # avoiding incorrect SHA256 hashes
    string.strip(":")
    string.strip(".")
    return string.strip(":")

def HEX_MESSAGE_TREE(recipient, sender):
    recipient = DELIMITER_STRIPPER(recipient)
    sender = DELIMITER_STRIPPER(sender)

    n_256 = hashlib.sha256()
    # empty string reserved for protocol
    assert n_256.hexdigest() == test_hash_lib()

    # SHA256()+GPGR
    n_256.update(bytes(recipient, 'utf-8'))
    if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info(n_256.digest_size)
    if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+GPGS
    n_256.update(bytes(sender, 'utf-8'))
    if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info(n_256.digest_size)
    if (HEX_LOGGER): logger.info(n_256.block_size)

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
    if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info(n_256.digest_size)
    if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE
    n_256.update(bytes(message, 'utf-8'))
    if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info(n_256.digest_size)
    if (HEX_LOGGER): logger.info(n_256.block_size)

    # SHA256()+GPGR+MESSAGE+GPGS
    n_256.update(bytes(sender, 'utf-8'))
    if (HEX_LOGGER): logger.info(n_256.digest())
    if (HEX_LOGGER): logger.info(n_256.hexdigest())
    if (HEX_LOGGER): logger.info(n_256.digest_size)
    if (HEX_LOGGER): logger.info(n_256.block_size)

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
logger.info(mempool_height())

