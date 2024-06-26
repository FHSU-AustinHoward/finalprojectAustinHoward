### Final Project
### Austin Howard
### INF601 - Advanced Programming in Python

# Final Project - VLNRbull Scanning System

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

This project ended up using other elements not necessarily Python related, such
as Javascript, and serves as an introduction to full stack web development.  I developed
this initially in MacOS before porting it to Windows.

## Authors
Austin Howard - [Email](A_Howard4@mail.fhsu.edu)  

## Getting Started
The running environment and all dependencies can be obtained through the command console in the Python IDE of your 
choosing.

### Step 1: Obtain NVD API Key
Before bothering with the terminal, it would be a good idea to get an API key. This program might
run without one, but it will be many times slower and possibly timeout some of the queries. 

To obtain an NVD API Key you'll need to have one commissioned from the National Institute of Standards and Technology's 
[Website](https://nvd.nist.gov/developers/request-an-api-key). After agreeing to the terrms of use, an API key will be
emailed to you. This can take a few minutes.

### Step 2: Install project requirements
While you're waiting on the API key, you will need to install this application's dependencies.  

In a terminal window, please type the following:  
```pip install -r requirements.txt```

### Step 3: Setup environment variables
I've made a script to apply that fancy new API key.

Let's change the directory to find that file in the terminal and accomplish later tasks:  
```cd VULNRbull```

Then call the env creator to setup the file:  
```python env_creator.py```

Type or paste in your responses as indicated, you will see a new file created in ./VULNRbull/devices, a subdirectory
of your present working directory. A console print statement should confirm this.

### Step 4: Create migration and database
Django now has the information it needs to start building up VULNRbull's migrations and databases.

To build the migration, we'll send this to the console:  
```python manage.py makemigrations devices```

This tells Django how to build VULNRbull databases, but doesn't apply them.   
Next you'll run this to actually build them:  
```python manage.py migrate```

### Step 5: Create superuser to manage admin portal
The app is built, but you'll need to be able to make administrative accounts who can manage it.

Type this in the console, following the prompts on screen to create a superuser account:  
```python manage.py createsuperuser```

### Step 6: Run the server on your localhost
You're all set, now we just need to launch the site.

To serve your requests, you'll need to type the following into your console:  
```python manage.py runserver```

After that you have a running instance of VULNRbull! Follow the link in the console to navigate to the home page.

Be sure to run a scan on one of your computers and checkout the /admin page to see how the site is administered.

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
