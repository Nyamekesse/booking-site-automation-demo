# Booking Site Automation Demo

This mini project will serves as a guide to web automation. It has most of the functionalities you will perform when automating task on the web using Python Selenium library.

The primary language for this mini project is solely Python and it follows PEP8 style guidelines.
Click to read more about [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

---

## Getting Started

### Pre-requisites and Local Development

In order to run this project locally, you should have Chrome browser, Chrome driver, Python 3, pip and selenium installed on your local machines.
Kindly check your chrome version and download it appropriate driver.
To check for your Chrome version, head on to your browser and type ` chrome://version` inside the URL bar and hit on enter. When done click [here](https://chromedriver.chromium.org/downloads) to download the appropriate driver version.

## Setting Up

#### Downloading chrome driver

---

In your local computer create a directory and name it `selenium-chrome-drivers`, download the chrome driver to this directory. In the config.py file check for `@TODO` and update the path to the chrome driver you have just downloaded.
If you have `chocalatey` installed on your computer make sure to update the chrome driver as this may cause errors if version is different from your chrome browser you are using.

#### Installing dependencies in virtual environment

---

Navigate to your preferred folder in which you will work in and clone the repository to it.

> For pycharm users, Pycharm automatically create one for you when you create a new project in the IDE.

#### Create a virtual environment

To create a virtual environment, open a terminal in the directory you will work in and run:

_For Mac / Linux users_

```python
$ pip install virtualenv
$ virtualenv <give it a name>
$ source virtualenv_name/bin/activate
```

_For Windows users_

```python
 pip install virtualenv
 python -m venv <give it a name>
 <name of virtual environment>\Scripts\activate.bat
```

After installing virtual environment, creating one and activating using the above commands, run ` pip install -r requirements.txt` to install all the necessary dependencies as well as it versions required to run the project.

#### Running the Project

---

Open the project in your preferred text editor and run the `main.py` file.
The browser will run on a new browser window by default.
The scripts is expected to perform these task

- Open the browser
- Navigate to this url [https://www.booking.com](https://www.booking.com)
- Select a currency based on the user preference
- Perform a search on a particular location
- Choose a check in and check out date.
- Select the number of adults, children and number of room reservations.
- Set the ages individually for the children and search to get a result.
- After getting a results the browser is taken to a result and sorted by rating stars.
- The number of results is then printed onto the terminal for the user to know.

## Deployment N/A

## Authors

Nyamekesse Samuel

## Acknowledgements

To the awesome club Phoenix Coding Club UCC.
