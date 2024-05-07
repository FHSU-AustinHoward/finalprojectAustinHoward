import platform
import os
from dotenv import load_dotenv
import nvdlib

# Load environment variables
load_dotenv()
DEBUGGING = os.getenv("NVDLIB_DEBUGGING", "False").lower() == "true"
KEY = os.getenv("NVD_API_KEY")
MIN_CVE_SCORE = float(os.getenv("NVDLIB_MIN_CVE_SCORE"))


def search_cves_by_cpe(cpe_name):
    """
    Searches for CVE entries based on the Common Platform Enumeration (CPE) name.

    Args:
        cpe_name (str): The CPE name of the software.

    Returns:
        list: A list of CVE entries.
    """
    try:
        # Search for CVE entries based on the CPE name
        return nvdlib.searchCVE(cpeName=cpe_name, key=KEY, delay=1)
    except Exception as e:
        if DEBUGGING:
            print(f"Error searching CVEs for {cpe_name}: {e}")
        return []


def search_cpe_by_name(software_name):
    """
    Searches for Common Platform Enumeration (CPE) names based on the software name.

    Args:
        software_name (str): The name of the software.

    Returns:
        str: The CPE name of the software if found, None otherwise.
    """
    try:
        # Search for CPE entries based on the software name
        cpe_entries = nvdlib.searchCPE(keywordSearch=software_name, key=KEY, delay=1)
        # Extract the CPE name from the first entry if found
        if cpe_entries:
            return cpe_entries[0].cpeName
        else:
            return None
    except Exception as e:
        if DEBUGGING:
            print(f"Error searching CPEs for {software_name}: {e}")
        return None


def search_installed_software():
    """
    Searches for installed software on the device.

    Returns:
        list: A list of installed software names.
    """
    system = platform.system()
    installed_software = []

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
                installed_software.extend(apps)
    else:
        if DEBUGGING:
            print("Unsupported operating system.")

    return installed_software


def debug_info(username, device_name):
    """
    Displays debug information about the device and its software vulnerabilities.

    Args:
        username (str): The username of the device owner.
        device_name (str): The name of the device.
    """
    if DEBUGGING:
        print(f"Username: {username}")
        print(f"Device Name: {device_name}")
        print(f"Operating System: {platform.platform()}")

        # Search for installed software
        installed_software = search_installed_software()

        # Print debug information about the installed software
        print("\nInstalled Software:")
        for software in installed_software:
            cpe_name = search_cpe_by_name(software)
            cpe_info = cpe_name if cpe_name else "No CPE Found"
            print(f"- {software} ({cpe_info})")
            # Search for vulnerabilities associated with the installed software
            if cpe_name:
                cve_entries = search_cves_by_cpe(cpe_name)
                for cve in cve_entries:
                    print(f"  - CVE ID: {cve.id}")
                    print(f"    Score: {cve.score[1]}")
                    print(f"    URL: {cve.url}")

        print("\n")


if __name__ == "__main__":
    debug_info("test_user", "MyMac")
