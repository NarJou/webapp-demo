#!/usr/bin/python
activate_this ="~/flaskapp/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0,"/var/webapp/")
from app import application
