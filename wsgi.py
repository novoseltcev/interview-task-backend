import sys
from os import path

from app import create_app

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
application = create_app()
