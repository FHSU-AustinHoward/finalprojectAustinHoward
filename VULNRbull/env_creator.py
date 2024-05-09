# INF601 - Advanced Programming with Python
# Austin Howard
# Final Project

# Function to create a .env file with user input values
def create_env_file():
    # Gather user input for environment variables
    env_content = [
        "NVD_API_KEY = '{}'".format(input("Enter NVDLIB_KEY: ")),
        "NVDLIB_DEBUGGING = {}".format(input("Enter NVDLIB_DEBUGGING (True/False): ")),
        "NVDLIB_MIN_CVE_SCORE = {}".format(input("Enter NVDLIB_MIN_CVE_SCORE: ")),
        "DJANGO_KEY = '{}'".format(input("Enter DJANGO_KEY: "))
    ]

    # Write the gathered environment variables to a .env file
    with open('.env', 'w') as env_file:
        env_file.write('\n'.join(env_content))


if __name__ == "__main__":
    # Call the function to create the .env file
    create_env_file()
    # Print a success message
    print(".env file has been created successfully.")
