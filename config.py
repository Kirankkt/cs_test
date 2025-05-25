import os

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', 'true').lower() in ('true', '1')
    TESTING = False
    # Add database URIs or other settings here
