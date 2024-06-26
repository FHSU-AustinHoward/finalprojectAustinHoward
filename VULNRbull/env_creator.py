# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

import os

from django.core.management import execute_from_command_line
from django.core.management.utils import get_random_secret_key


def create_env_file():
    """
    Creates a .env file with user input values or prints its contents if it already exists.
    If the .env file does not exist, it generates a Django secret key, writes environment
    variables to the .env file, and runs specified command lines in the console.

    Args:
        None

    Returns:
        None
    """
    # Check if .env file already exists
    if os.path.exists('.env'):
        # If .env file exists, print its contents to the command line
        print("A .env file already exists. Please rename or remove this file before trying again.\n")
    else:
        # Generate Django secret key
        django_key = get_random_secret_key()

        # Write environment variables to .env file
        env_content = [
            "NVD_API_KEY = '{}'".format(input("Enter NVDLIB_KEY: ")),
            "NVDLIB_DEBUGGING = {}".format(True),
            "DJANGO_KEY = '{}'".format(django_key)
        ]
        with open('.env', 'w') as env_file:
            env_file.write('\n'.join(env_content))

        # Print a success message
        print(".env file has been created successfully.")


if __name__ == "__main__":
    create_env_file()
