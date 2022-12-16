import os, sys
try:
    __import__("Crack").approval()._run_()
except Exception as e:
    exit(str(e))
