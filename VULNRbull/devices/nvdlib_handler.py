# INF601 - Advanced Programming with Python
# Austin Howard
# Final Project

import os
import platform
from dotenv import load_dotenv
import nvdlib

# .env vars
load_dotenv()
DEBUGGING = os.getenv("NVDLIB_DEBUGGING", "TRUE").lower() == "true"
KEY = os.getenv("NVDLIB_KEY")
MIN_CVE_SCORE = float(os.getenv("NVDLIB_MIN_CVE_SCORE"))


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

    def debug_print(self):
        """
        Prints vulnerability details if debug mode is enabled.
        """
        if DEBUGGING:
            print(f"- CVE ID: {self.cve_id}, "
                  f"Score: {self.cve_score}, "
                  f"URL: {self.cve_url}")


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
            # Search for CPE entries based on the software name
            cpe_entries = nvdlib.searchCPE(keywordSearch=name, key=KEY, delay=1)

            # Iterate through the CPE entries
            for cpe in cpe_entries:
                cpe_name = cpe.cpeName
                # Add the CPE name to the cache
                Software.cpe_name_cache[name] = cpe_name
                return cpe_name
            else:
                return None  # Return None if no CPE name is found
        except Exception as e:
            if DEBUGGING:
                print(f"Error searching CPEs for {name}: {e}")
            return None  # Return None in case of an error

    def fetch_vulnerabilities(self):
        """
        Fetches vulnerabilities associated with the software.
        """
        try:
            # Search for CVE entries based on the CPE name
            cve_entries = nvdlib.searchCVE(cpeName=self.cpe_name, key=KEY, delay=1)

            # Iterate through the CVE entries
            for cve in cve_entries:
                # Check if the score is greater than or equal to the minimum score
                if cve.score[1] >= MIN_CVE_SCORE:
                    # Create Vulnerability object with CVE details and append to vulnerabilities list
                    vulnerability = Vulnerability(
                        cve.id, cve.descriptions, cve.score[1], cve.url
                    )
                    self.vulnerabilities.append(vulnerability)

            if DEBUGGING:
                print(f"Vulnerabilities found for {self.name}!")
        except Exception as e:
            if DEBUGGING:
                print(f"Error fetching vulnerabilities for {self.name}: {e}")

    def debug_print(self):
        """
        Prints software vulnerabilities if debug mode is enabled.
        """
        if DEBUGGING:
            for cve in self.vulnerabilities:
                cve.debug_print()


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
        self.software, self.vulnerabilities = self.get_cpes()

    def get_cpes(self):
        """
        Retrieves a list of installed software with their associated vulnerabilities.

        Returns:
            tuple: A tuple containing two lists:
                - A list of Software objects representing installed software.
                - A list of Software objects representing vulnerabilities.
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
                        if DEBUGGING:
                            print(f"Fetching CPEs and CVEs for: {app}...")
                        software = Software(app)
                        installed_cpes.append(software)

        else:
            if DEBUGGING:
                print("Unsupported operating system.")

        # Extract vulnerabilities from installed software
        vulnerabilities = []
        for software in installed_cpes:
            vulnerabilities.extend(software.vulnerabilities)

        return installed_cpes, vulnerabilities

    def debug_print(self):
        """
        Prints device details and associated vulnerabilities if debug mode is enabled.
        """
        print("\nDevice:")
        print(f"Device name: {self.device_name}")
        print(f"Owner: {self.username}")
        print(f"Operating System: {self.os_name}")
        print("\nVulnerabilities:")
        for cpe in self.software:
            cpe.debug_print()


def debug_info(username, device_name):
    """
    Displays debug information about the device and its software vulnerabilities.

    Args:
        username (str): The username of the device owner.
        device_name (str): The name of the device.
    """
    print(
        f"Hi, @{username}. "
        f"We're searching NIST NVD Database for software installed on "
        f"{device_name}.\n"
        f"This can take several minutes!\n\n"
        f"Debugging mode: {DEBUGGING}"
    )
    if DEBUGGING:
        print(
            f"API key: {KEY}\n"
            f"Minimum CVE Score: {MIN_CVE_SCORE}\n"
        )
    device = Device(username, device_name)
    if DEBUGGING:
        device.debug_print()


def main():
    # UNCOMMENT TO TEST
    # username = "test_user"
    # device_name = "MyMac"
    # debug_info(username, device_name)
    pass


if __name__ == "__main__":
    main()