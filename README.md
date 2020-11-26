# email_works
Easy module for working with mail based on smpt and gmail

## Import this module
###### 1. put email_works.py in derictory with your main file
It must looks like this:

![example](example.png)
###### 2. Just import it!
```python
import email_works
```
## Change message information
###### Works only on NT!
```python
email_works.sender = "your@gmail.com"        # your email
email_works.receiver = "somebody@gmail.com"  # receiver email
email_works.password = "your_password_here"  # your password
```

## Send message with text
```python
email_works.send(
header="Email_works test 1",   # header of message
text="Hello, world!",        # message text
)
```

## Send message with html
```python
email_works.send(
header="Email_works test 2",   # header of message
html="""
<html>
  <body>
    <a href="https://github.com/NVcoder24/email_works">Email works on github</a>
  </body>
</html>
"""                          # some html
)
```
