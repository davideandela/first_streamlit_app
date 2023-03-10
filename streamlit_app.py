#!/usr/bin/env python
"""First attempt at a Python code"""

import streamlit
streamlit.title('What is this all about')

print('=' * 150)
print(f"Script path                                         | {os.path.abspath(__file__)}")
print(f"Python version                                      | {sys.version}")
print(f"Python path                                         | {sys.executable}")
print(f"Application environment                             | {os.getenv('APP_ENV')}")
print(f"Application host                                    | {os.getenv('APP_HOST')}")
print(f"Email recipients list                               | {os.getenv('EMAIL_LIST')}")
print(f"Pythonpath variable                                 | {sys.path}")
print('=' * 150)
