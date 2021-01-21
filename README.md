# email_works
Easy module for working with mail based on smpt and gmail<br>
Uses ssl connection on port 465

## Install important libraries
###### All tested on python 3.8.5
Update pip
```shell
python -m pip install --upgrade pip
```
Install libraries
```shell
pip install smtplib
pip install email
```

## Import this module
###### 1. put email_works.py in derictory with your main file

###### 2. Just import it!
```python
from email_works import email_works
```
## Create variable for email works
```python
ew = email_works()
```

## Log in
```python
ew.login({"password":"yourpassword","sender":"youremail@gmail.com"})
```

## Send message with plain text
```python
ew.send_text(header="Hello, world!", text="some text...", receiver="somebody@gmail.com")
```

## Send message with html
```python
ew.send_html(header="Hello, world!", html="<a href='google.com'>some html...</a>", receiver="somebody@gmail.com")
```

## Log off'
```
ew.logoff()
```
