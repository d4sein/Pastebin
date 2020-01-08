import os

# Defines the application directory
DATABASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

if not os.path.exists(DATABASE_DIR):
    os.mkdir(DATABASE_DIR)

THREADS_PER_PAGE = 2

# Enables protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Secret key for signing the data. 
CSRF_SESSION_KEY = 'secret'

SESSION_COOKIE_SECURE = True

# Secret key for signing cookies
# >>> import secrets
# >>> secrets.token_urlsafe(16)
SECRET_KEY = 'Drmhze6EPcv0fN_81Bj-nA'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE_DIR, 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
