# Hospito
hospito is a web-based application that lets you administrate your hospital or clinique and why not a country common health  system
## Guide
hospito is based on python so you need to have python installed and install
Flask And sqlite3 
Using
```bash
pip install flask
```
```bash
pip install sqlite3
```
After installing Python,Flask And sqlite3 
start the server by going to the hospito folder location in cmd or terminal and run
```bash
python app.py
```
the terminal will show you the server link
## Login
the server link will redirect always to the login page to login the first time and to be able to add staff you need to use the admin account<br />
username:1 / password:1<br />
you can change who is the admin (create and see all details about staff and can do any other work) by change the staff id on line 9 and 30 on the app.py file
## observation
the staff id is printed at the bottom of the staff card<br />
consultation id is printed at the bottom of the prescription<br />
client id is printed at the bottom of the client card
