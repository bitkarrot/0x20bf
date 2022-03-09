#!/usr/bin/env python3
import builtins
import importlib
import types
from inspect import getmembers, iscoroutinefunction, isfunction, ismodule

importlib.import_module("_0x20bf", package=0x20BF)
# importlib.import_module("logger", package=0x20bf)
# importlib.import_module("time_functions", package=0x20bf)
#
# _0x20bf = builtins.__import__('0x20bf')
# B = builtins.__import__('0x20bf')

B = builtins.__import__(
    "0x20bf",
    globals(),
    locals(),
    [
        "delimiter_stripper",
        "depends",
        "hex_message_digest",
        "imports",
        "logger",
        "mempool_height",
        "message_header",
        "search_gpg_key",
        "time_functions",
        "touch_block_time",
        "tweet_block_time",
        "twitter_api_keys",
    ],
    0,
)

# time_functions = builtins.__import__('0x20bf.time_functions')

# help(B)

print([o for o in getmembers(B, isfunction)])
print([o for o in getmembers(B, ismodule)])
print([o for o in getmembers(B, iscoroutinefunction)])


print([getattr(B, a) for a in dir(B) if isinstance(getattr(B, a), types.FunctionType)])

# B.main(sys.argv[1:])
