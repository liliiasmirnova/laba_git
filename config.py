import os

# Token is read from the environment, never stored in code
GH_TOKEN = os.environ.get("GH_TOKEN", "")
DEBUG = True
