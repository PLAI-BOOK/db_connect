from setuptools import setup, find_packages

setup(
    name='db_connect',             # Name of the package
    version='1.0.0',               # Version of the package
    description='A utility for database connections',
    author='Manuel Ruffieux',
    author_email='',
    url='https://github.com/PLAI-BOOK/db_connect',
    packages=find_packages(),      # Automatically finds all packages in the directory
    install_requires=[
        'psycopg2',  # Required for PostgreSQL connection
        'python-dotenv'  # Required for loading environment variables from a .env file
    ],
    entry_points={
        'console_scripts': [
            'db_connect=db_connect:main',  # Optional if you have a main script entry point
        ],
    },
)
