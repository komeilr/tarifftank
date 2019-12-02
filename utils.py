import os


def check_env_vars():
    """checks to see if environment variables have been set
    Raises error"""

    env_vars = [
        'FLASK_APP',
        'FLASK_ENV',
        'DATABASE_URI',
        'SECRET_KEY'
    ]

    for var in env_vars:
        if var not in os.environ.keys():
            raise AttributeError(f"{var} environment variable not set - source .env")
        


