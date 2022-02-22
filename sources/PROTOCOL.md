
---

[0x20bf.org](https://github.com/0x20bf-org) \<[admin@0x20bf.org](mailto:admin@0x20bf.org)\>
Randy McMillan \<[randymcmillan@protonmail.com](mailto:randymcmillan@protonmail.com)\>
Category: Standards Track

---

<center><H4>0xbf20 - A general purpose messaging protocol</center>

## Status of this Proposal

This document proposes an Internet standards track protocol for transporting, broadcasting and syndication of messages over common internet communications channels. The distribution of all documents related to this proposal are unlimited and unencumbered by any [LICENSE](LICENSE), but some are included anyway.

## Abstract

This document describes the ox20bf protocol message structure and related operations associated with message field ordering and data typing. 0x20bf is meant to be simple, enabling flexability of implementation. Gnupg is used for text message encryption. Git version control is used for archiving messages. These dependancies are for convienence.

# Protocol - Field definitions

`:` - message field delimiter
--

`GPGR` - gnupg (short/long) id of the reciever of a message
--

`GPGS` - gnupg (short/long) id of the sender of a message
--

##### Example - ping short format
`:GPGR:GPGS:` :\<recipient\>:\<sender\>:
--

`:BTC_TIME:` - a Bitcoin block height in the "time chain".
--

`:UNIX_TIME_SECONDS:` - UTC Time in seconds
--

`:UNIX_TIME_MILLIS:` - UTC Time in milliseconds
--

##### Example - ping time chain format
`:GPGR:GPGS:BTC_TIME:` :\<recipient\>:\<sender\>:\<block height\>

##### Example - ping UTC time format
`:GPGR:GPGS:UNIX_TIME_SECONDS:` :\<recipient\>:\<sender\>:\<utc time\>

##### Example - ping full format (seconds)
`:GPGR:GPGS:BTC_TIME:UNIX_TIME_SECONDS:` :\<recipient\>:\<sender\>:\<block height\>:\<utc time seconds\>

##### Example - ping full format (milliseconds)
`:GPGR:GPGS:BTC_TIME:UNIX_TIME_MILLIS:` :\<recipient\>:\<sender\>:\<block height\>:\<utc time milliseconds\>

