import os
import sys


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-taza-association'
    
    # Handle Database for Vercel (Read-only filesystem)
    if os.environ.get('VERCEL'):
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/site.db'
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    # Mail Settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'tazaassociation81@gmail.com'
    MAIL_PASSWORD = 'udsq fzjy rqpa oabh'  # Official Google App Password
    MAIL_DEFAULT_SENDER = 'tazaassociation81@gmail.com'
    ADMIN_EMAIL = 'tazaassociation81@gmail.com'
