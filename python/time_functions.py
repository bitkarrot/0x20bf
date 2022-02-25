#!/usr/bin/env python3
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
