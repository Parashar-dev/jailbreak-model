#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Cybersecurity Lab - Master Command-Line and Interactive Controller
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from lab_runner import main

if __name__ == "__main__":
    main()
