import os, sys
try:
    __import__("CRK").menu()
except Exception as e:
    exit(str(e))
