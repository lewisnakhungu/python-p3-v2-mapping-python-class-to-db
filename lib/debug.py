#!/usr/bin/env python3
# lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

# Ensure table exists
Department.create_table()

# Optionally drop and recreate for testing clean state
# Department.drop_table()
# Department.create_table()

# Add a test department instance (optional, if you have a save method)
test_dept = Department(name="Engineering", location="Building A")

# Start debugging session
ipdb.set_trace()
