# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project

import os
import platform
from dotenv import load_dotenv
import nvdlib


class Vulnerability:
    """
    Represents a vulnerability with its details.
    """

    def __init__(self, cve_id, cve_descriptions, cve_score, cve_url):
        """
        Initializes a Vulnerability object.

        Args:
            cve_id (str): The CVE ID.
            cve_descriptions (str): Description of the CVE.
            cve_score (float): The severity score of the CVE.
            cve_url (str): URL to the CVE details.
        """
        self.cve_id = cve_id
        self.cve_descriptions = cve_descriptions
        self.cve_score = cve_score
        self.cve_url = cve_url

    def debug_print(self, debug=False):
        """
        Prints vulnerability details if debug mode is enabled.

        Args:
            debug (bool, optional): Whether debug mode is enabled. Defaults to False.
        """
        if debug:
            print(f"   CVE ID: {self.cve_id}")
            print(f"   CVE URL: {self.cve_url}")
            print(f"   CVE Score: {self.cve_score}")
            print(f"   ---------------")


class Software:
    """
    Represents software installed on the device.
    """
    # Cache to store CPE names
    cpe_name_cache = {}

    def __init__(self, name):
        """
        Initializes a Software object.

        Args:
            name (str): The name of the software.
        """
        self.name = name
        self.cpe_name = self.get_cpe_name(name)
        # Initialize vulnerabilities list
        self.vulnerabilities = []
        if self.cpe_name:
            self.fetch_vulnerabilities()

    def get_cpe_name(self, name):
        """
        Retrieves the Common Platform Enumeration (CPE) name for the software.

        Args:
            name (str): The name of the software.

        Returns:
            str: The CPE name of the software if found, None otherwise.
        """
        # Check if the CPE name is already cached
        if name in Software.cpe_name_cache:
            return Software.cpe_name_cache[name]

        try:
            # Load API key from environment variables
            load_dotenv()
            api_key = os.environ.get("API_KEY")

            # Search for CPE entries based on the software name
            cpe_entries = nvdlib.searchCPE(keywordSearch=name, key=api_key, delay=1)

            # Iterate through the CPE entries
            for cpe in cpe_entries:
                cpe_name = cpe.cpeName
                # Add the CPE name to the cache
                Software.cpe_name_cache[name] = cpe_name
                return cpe_name
            else:
                return None  # Return None if no CPE name is found
        except Exception as e:
            print(f"Error searching CPEs for {name}: {e}")
            return None  # Return None in case of an error

    def fetch_vulnerabilities(self, debug=False):
        """
        Fetches vulnerabilities associated with the software.
        """
        try:
            # Load API key from environment variables
            load_dotenv()
            api_key = os.environ.get("API_KEY")

            if debug:  # Check if debug mode is enabled
                # Print the name of the software being fetched
                print(f"Fetching vulnerabilities for {self.name}...")

            # Search for CVE entries based on the CPE name
            cve_entries = nvdlib.searchCVE(cpeName=self.cpe_name, key=api_key, delay=1)

            # Iterate through the CVE entries
            for cve in cve_entries:
                # Create Vulnerability object with CVE details and append to vulnerabilities list
                vulnerability = Vulnerability(
                    cve.id, cve.descriptions, cve.score[1], cve.url
                )
                self.vulnerabilities.append(vulnerability)

            if debug:  # Check if debug mode is enabled
                # Print a message indicating that vulnerabilities for the software have been retrieved
                print(f"Vulnerabilities fetched for {self.name}.")
        except Exception as e:
            if debug:  # Check if debug mode is enabled
                # Print error message if fetching vulnerabilities fails
                print(f"Error fetching vulnerabilities for {self.name}: {e}")

    def debug_print(self, debug=False):
        """
        Prints software vulnerabilities if debug mode is enabled.

        Args:
            debug (bool, optional): Whether debug mode is enabled. Defaults to False.
        """
        if debug:
            print(f"\nSoftware: {self.name}")
            for cve in self.vulnerabilities:
                cve.debug_print(debug)


class Device:
    """
    Represents a device with its installed software and vulnerabilities.
    """

    def __init__(self, username, device_name):
        """
        Initializes a Device object.

        Args:
            username (str): The username of the device owner.
            device_name (str): The name of the device.
        """
        self.username = username
        self.device_name = device_name
        self.os_name = platform.platform()
        self.software = get_cpes()
        self.vulnerabilities = self.get_cpes()

    def get_cpes(self, debug=False):
        """
        Retrieves a list of installed software with their associated vulnerabilities.

        Returns:
            list: A list of Software objects representing installed software.
        """
        system = platform.system()
        installed_cpes = []

        if system == "Darwin":
            app_directories = [
                "/Applications",
                os.path.expanduser("~/Applications")
            ]
            for directory in app_directories:
                if os.path.exists(directory):
                    apps = [
                        os.path.splitext(app)[0]
                        for app in os.listdir(directory)
                        if app.endswith('.app')
                    ]
                    for app in apps:
                        if debug:  # Check if debug mode is enabled
                            # Print the name of the software being fetched
                            print(f"Fetching software: {app}...")
                        software = Software(app)
                        installed_cpes.append(software)
                        if debug:  # Check if debug mode is enabled
                            # Print a message indicating that software has been fetched
                            print(f"Software fetched: {app}.")
        else:
            print("Unsupported operating system.")

        return installed_cpes

    def debug_print(self, debug=False):
        """
        Prints device details and associated vulnerabilities if debug mode is enabled.

        Args:
            debug (bool, optional): Whether debug mode is enabled. Defaults to False.
        """
        if debug:
            print("\nDevice:")
            print("Device name:", self.device_name)
            print("Owner:", self.username)
            print("\nSoftware:")
            for cpe in self.software:
                cpe.debug_print(debug)
            print("\nVulnerabilities:")
            for cve in self.vulnerabilities:
                cve.debug_print(debug)


def get_cpes():
    """
    Retrieves a list of installed software with their associated vulnerabilities.

    Returns:
        list: A list of Software objects representing installed software.
    """
    system = platform.system()
    installed_cpes = []

    # Mac OS
    if system == "Darwin":
        app_directories = [
            "/Applications",
            os.path.expanduser("~/Applications")
        ]
        for directory in app_directories:
            if os.path.exists(directory):
                apps = [
                    os.path.splitext(app)[0]
                    for app in os.listdir(directory)
                    if app.endswith('.app')
                ]
                for app in apps:
                    # Print the name of the software being fetched
                    print(f"Fetching software: {app}...")
                    software = Software(app)
                    installed_cpes.append(software)
                    # Print a message indicating that software has been fetched
                    print(f"Software fetched: {app}.")
    else:
        print("Unsupported operating system.")

    return installed_cpes


def debug_info(username, device_name, debug):
    """
    Displays debug information about the device and its software vulnerabilities.

    Args:
        username (str): The username of the device owner.
        device_name (str): The name of the device.
        debug (bool, optional): Whether debug mode is enabled. Defaults to False
    """
    if debug:
        load_dotenv()
        api_key = os.environ.get("API_KEY")

        print(f"Debug mode: {debug}")
        print(f"API key: {api_key}")
        print(f"Hi, @{username}. "
              f"We're searching NIST NVD Database for software installed on "
              f"{device_name}.")
        print(f"This can take several minutes!\n")
        device = Device(username, device_name)
        device.debug_print(True)


def main():
    # Variables intended to be fetched by Django later, they are in the main
    # function for debugging purposes only
    username = "test_user"
    device_name = "MyMac"
    debug = True

    debug_info(username, device_name, debug)


if __name__ == "__main__":
    main()
