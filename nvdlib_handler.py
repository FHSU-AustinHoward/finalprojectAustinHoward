# INF601 - Advanced Programming in Python
# Austin Howard
# Final Project



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

    def __init__(self):
        pass

    def get_cpe_name(self):
        pass

    def fetch_vulnerabilities(self):
        pass

    def debug_print(self):
        pass

class Device:

    def __init__(self):
        pass

    def get_cpes(self):
        pass

    def debug_print(self):
        pass


def get_cpes():
    pass

def debug_info():
    pass

def main():
    pass


if __name__ == "__main__":
    main()
