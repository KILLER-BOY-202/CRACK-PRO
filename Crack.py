import os, sys
try:
    __import__("KILLER").menu()
except Exception as e:
    exit(str(e))
