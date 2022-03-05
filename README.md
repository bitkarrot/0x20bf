[🐝](https://keys.openpgp.org/vks/v1/by-fingerprint/E616FA7221A1613E5B99206297966C06BB06757B) [🥕](https://keys.openpgp.org/vks/v1/by-fingerprint/57C5E8BB2F2746C3474B8A511421BF6C4DC9817F) [Github](http://github.com/0x20bf-org) [Twitter](https://twitter.com/0x20bf_org)<HR>

<center><H4>0xbf20 - A general purpose messaging protocol</center>

## Status of this Proposal

This document proposes an Internet standards track protocol for transporting, broadcasting and syndication of messages over common internet communications channels. The distribution of all documents related to this proposal are unlimited and unencumbered by any [LICENSE](LICENSE), but some are included anyway.

## Abstract

This document describes the ox20bf protocol message structure and related operations associated with message field ordering and data typing. 0x20bf is meant to be simple, enabling flexability of implementation. Gnupg is used for text message encryption. Git version control is used for archiving messages.

## Protocol - Field definitions

### message field delimiter
`:` - message field delimiter

### gnupg (long/short key ID) of the reciever of a message
`GPGR` - gnupg (long/short key ID) of the reciever of a message

### gnupg (long/short key ID) of the sender of a message
`GPGS` - gnupg (long/short key ID) of the sender of a message

##### Example - ping short format
`:GPGR:GPGS:` `:<recipient>:<sender>:`

### algorithm field
`:ALGO:` indicates encryption algorithm used for message construction

##### Example
`:ALGO:ALGO:ALGO:ALGO:`

`:PUBKEY:CIPHER:HASH:COMPRESSION:`

`:RSA:AES256:SHA256:ZIP:`

##### gnupg supported algorithms:
```
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2
```

We assume messages are sent in the blind: `--include-key-block` will be the default, to enable offline decryption. [OpenPGP-Options.html](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Options.html)

### time fields
`:BTC_TIME:` - a Bitcoin block height in the "time chain".

`:BTC:` - a Bitcoin block height in the "time chain".

`:UNIX_TIME_SECONDS:` - UTC Time in seconds

`:UNIX_TIME_MILLIS:` - UTC Time in milliseconds

`:TIME:` - UTC Time in milliseconds

##### Example - ping time chain format
`:GPGR:GPGS:BTC_TIME:`

##### Example - ping UTC time format
`:GPGR:GPGS:UNIX_TIME_SECONDS:`

##### Example - ping full format (seconds)
`:GPGR:GPGS:BTC_TIME:UNIX_TIME_SECONDS:`

##### Example - ping full format (milliseconds)
`:GPGR:GPGS:BTC_TIME:UNIX_TIME_MILLIS:`

##### Example - ping abridged format (milliseconds) - abridged `:TIME:` is in millisoeconds
`:GPGR:GPGS:BTC:TIME:`

---

TODO: more message structure

TODO: file structure

TODO: LOC - location specifications for offline resources

---



<br>[![python.yml](https://github.com/0x20bf-org/0x20bf/actions/workflows/python.yml/badge.svg)](https://github.com/0x20bf-org/0x20bf/actions/workflows/python.yml)


## Getting Started

##### [git](https://git-scm.com/downloads)

```
git clone https://github.com/0x20bf-org/0x20bf.git
cd 0x20bf
```

##### [python@3.8+](https://www.python.org/downloads/)

```
git clone https://github.com/0x20bf-org/0x20bf.git
cd 0x20bf
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

##### [make](https://www.gnu.org/software/make/)
 	  help
 	  init           initialize requirements
 	  venv           create python3 virtual environment
 	  test-venv      python3 ./tests/py.test
 	  test-gnupg     python3 ./tests/depends/gnupg/setup.py install
 	  test-gnupg     python3 ./tests/depends/gnupg/test_gnupg.py
 	  build          python3 setup.py build
 	  install        pip install -e .
 	  report         environment args
 	  initialize     run scripts/initialize
 	  requirements   pip install --user -r requirements.txt
 	  seeder         make -C depends/seeder
 	  legit          pushd depends/legit && cargo build --release
 	  gogs           make -C depends/gogs
 	  install-gnupg  install python gnupg on host
 	  gnupg-test     test depends/gnupg library
 	  install-p2p    install python p2p-network on host
 	  depends        build depends
 	  pre-commit     pre-commit run -a
 	  docs           build docs from sources/*.md

## [Contributing](./sources/CONTRIBUTING.md)

Check linting and formatting
`pre-commit run -a`

Build for distribution
`python3 setup.py build`

---

<details>
<summary>Referral Links:</summary>
<p>

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=ae5c7d05da91&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

</p>
</details>
