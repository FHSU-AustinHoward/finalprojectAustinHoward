### Final Project
### Austin Howard
### INF601 - Advanced Programming in Python

# Final Project - VLNRbull Reporting System (Part 2)

## Description
VULNRbull scans your filesystem for installed applications and discovers
vulnerabilities associated with them. Store all your devices in it to see
what threats you face in your environment.

As someone majoring in Networking with an emphasis in cybersecurity, it is always
pertinent to stay on top of threats to your attack surface. VULNRbull helps keep
track of the bigger picture. This is just a demo for a capstone project in INF601 - 
Programming with Python, but I could see this being used by banking or security 
companies to warn their clients on threats and help prevent future cybercrime.

To meet project requirements, VULNRbull uses the Django framework and makes 
get requests to the NIST NVD database using NVDLib as the primary API. Usage
of this is most prominent in the API handler I created in the Devices application.

## Authors
Austin Howard - [Email](A_Howard4@mail.fhsu.edu)  

## Getting Started [NEEDS_REVIEW]
The running environment and all dependencies can be obtained through the command console in the Python IDE of your 
choosing.

### Step 1: Pip install requirements.txt
Before getting started, you will need to install this application's dependencies.  

In a terminal window, please type the following:
```
pip install -r requirements.txt
```

## Version History

* 0.1
    * Initial release to complete the assignment

## License

This project is licensed under the GNU GPL-3.0 License - see the LICENSE file for details

## Acknowledgments
### Huge thanks to:
* [NIST NVD API](https://nvd.nist.gov/developers/vulnerabilities)
* [NVDLib](https://nvdlib.com/en/latest/#:~:text=NVDLib%20is%20a%20Python%20API,National%20Vulnerability%20Database%20(NVD).&text=NVDLib%20is%20able%20to%20pull,Platform%20Enumeration%20(CPE)%20names)
* [Django](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
* [Jason Zeller](https://youtube.com/playlist?list=PLE5nOs3YmC2THmgcLi-ogD8KiIfCjS06V&si=zSLvUfz8xb-AnGO4)

###### END OF CONTENT #####

## Project Requirements [DELETE_BEFORE_SUBMISSION]

* 30%  [INCOMPLETE] Program handles erroneous or unexpected input gracefully; action is taken without surprising the user.
* 0%   [INCOMPLETE] You need to have at least one Django page that utilizes a form.
* 0%   [INCOMPLETE] You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but the more practice here the better. You need to at least make use of a modal.
* 0%   [IN PROGRESS] There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations. You will need to explain the steps of initializing the database and then how to run the development server for your project.

### Rough Draft - Installation Instructions
1. Obtain API Key
2. Install requirements.txt
3. Run env_creator.py

### Rough Draft - Helpful Commands
* Check Django version: ```python -m django --version```
* Create Django project: ```django-admin startproject VULNRbull```
* Create Django application: ```python manage.py startapp devices```
* Setup environment variables: ```python env_creator.py```
* Run the project server: ```python manage.py runserver```
* Create migrations for a particular app: ```python manage.py makemigrations devices```
* Perform the created migrations: ```python manage.py migrate```
* Create Super User ```python manage.py createsuperuser```

### ToDo
1. Ensure compatibility with windows
2. Make default screen the index page
3. Setup the index page to show that it is loading
4. Fix styles for the registration pages