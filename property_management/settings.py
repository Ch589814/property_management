import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use the appropriate engine
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Path to the database file
    }
}





