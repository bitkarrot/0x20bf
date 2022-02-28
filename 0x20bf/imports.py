#!/usr/bin/env python3
import os
import sys

sys.path.append('.')
sys.path.append("/usr/local/lib/python3.10/site-packages")
sys.path.append("/usr/local/lib/python3.9/site-packages")
sys.path.append("/usr/local/lib/python3.8/site-packages")
sys.path.insert(0, os.cwdget() + "/0x20bf/p2p")
sys.path.insert(0, os.cwdget() + "/0x20bf/gnupg")
# os.environ["PYTHONIOENCODING"] = "utf-8"
