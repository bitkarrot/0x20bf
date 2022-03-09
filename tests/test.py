#!/usr/bin/env python3
import sys

b3b3 = __import__('0x20bf')
user = __import__('0x20bf.time_functions')
# import 0x20bf as b3b3
sys.path.insert(1, '0x20bf')
sys.path.insert(2, 'depends')
sys.path.insert(3, 'sources')

print("venv working...")
print(sys.version)
print(user)
0x02bf.main(sys.argv[1:])
