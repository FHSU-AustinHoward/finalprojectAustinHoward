# INF601 - Advanced Programming with Python
# Austin Howard
# Final Project

def create_env_file():
    env_content = [
        "NVD_API_KEY = '{}'".format(input("Enter NVDLIB_KEY: ")),
        "NVDLIB_DEBUGGING = {}".format(input("Enter NVDLIB_DEBUGGING (True/False): ")),
        "NVDLIB_MIN_CVE_SCORE = {}".format(input("Enter NVDLIB_MIN_CVE_SCORE: ")),
        "DJANGO_KEY = '{}'".format(input("Enter DJANGO_KEY: "))
    ]

    with open('.env', 'w') as env_file:
        env_file.write('\n'.join(env_content))


if __name__ == "__main__":
    create_env_file()
    print(".env file has been created successfully.")