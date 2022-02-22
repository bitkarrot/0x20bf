#!/usr/bin/env python

from datetime import datetime
import logging
import math
import numpy

logger = logging.getLogger(__name__)
if not logger.handlers:
    logger.addHandler(logging.NullHandler())

def convert_UTC_zulu_string_to_milliseconds_since_epoch(myUTCzuluString):
    try:
        dt_unix = datetime.strptime(myUTCzuluString, "%Y-%m-%dT%H:%M:%S.%fZ")
        logger.info("%s", str(dt_unix))
        epoch = datetime.utcfromtimestamp(0)
        logger.info("%s", str(epoch))
        delta = dt_unix - epoch
        logger.info("%s", str(delta))
        millisecondsSinceEpoch = int(delta.total_seconds() * 1000)
        logger.info("%s", str(millisecondsSinceEpoch))

    except:
        millisecondsSinceEpoch = 0
        logger.info("%s", str(millisecondsSinceEpoch))

    return millisecondsSinceEpoch

def TimestampMillisec64():
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)


#myUTCzuluString = "2015-06-27T02:10:05.653000Z"
#millisecondsSinceEpoch = convert_UTC_zulu_string_to_milliseconds_since_epoch(myUTCzuluString)
#logger.info("Milliseconds since epoch: %d",millisecondsSinceEpoch)
