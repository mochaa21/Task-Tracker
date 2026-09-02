import sys
import json
from datetime import datetime
import os

if len(sys.argv) < 2:
    print("Error: Missing required argument.")
    print("Usage: python script.py <your_argument>")
    sys.exit(1)  # Stop execution with an error code

SyalwaSlutt = sys.argv[1]

if SyalwaSlutt == "SyalwaSlutt":
    if len(sys.argv) < 3:
        print("Error! Argument 3 is not defined.")
    else:
        print(sys.argv)