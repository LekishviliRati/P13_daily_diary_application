# Daily Dairy P13 👵

---
## Introduction

This is the last project of my training path as Python Software Developer at Openclassrooms.

The aim of this project is to identify a human need, and bring a solution to it, without 
seeking to make profits, but to help people.

Considering the difficulty of managing communication for nursing staff during covid, 
in retirement houses,
I decided to develop a web application to help health care personnel informing 
residents relatives by publishing daily posts on resident health status.
From my point of view, this solution provides daily information for residents relatives 
and at the same time it's freeing up nursing staff time to care for the elderly.
 
___

### *Key Features* 

- Responsive user interface.
- **Resident relative** : Access to daily posts on health status information.
- **Employees** : Create, update, delete posts and get access to resident's contacts.
- **Managers** : Create / update / delete users and manage all content of web application.

### *Deployment*

- Deployment on Digital Ocean :
  > https://cloud.digitalocean.com
  
- Apache2 :
  > https://httpd.apache.org/download.cgi

### *Website*

-  You can visit my application on : 
  > http://165.227.235.193

### *Install Python* ★

- Python 3.9
  > Install Python : https://www.python.org/downloads/
  
  > Python Documentation : https://www.python.org/doc/
  
### * Install Virtualenv*

- **Install** : pip3 install virtualenv
- **Create Virtualenv folder in the project** : virtualenv -p python3 env
- **Activate Virtualenv** : source env/bin/activate

### *Run Tests 👨‍🔬*

- **Overall tests** : python3 manage.py test
- **Coverage report** : coverage run manage.py test -v 2 && coverage report