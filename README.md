# CodeAlerts
Alert functions for sending notifications to email (for now). It sends an email from you to yourself with a custom alert.

## Installation
```
pip install git+https://github.com/nicoacevedor/codealerts.git
```

## Usage
1. Import both `chech_env` and `send_email` functions
```
from codealerts import check_env, send_email
```

2. Call `check_env` early in the code
```
from codealerts import check_env, send_email

check_env()

### SOME CODE
```
This function will check if `.notification_credentials` file exists. If not, it will ask you your credentials and create it. This file should look like
```
EMAIL="youremail@domain.com"
PASSWORD="yourpassword"
```
For Gmail (the only service supported, for now) this password is an [App Password](https://www.hostpapa.com/knowledgebase/how-to-create-and-use-google-app-passwords/), NOT the account password.

3. Call `send_email` wherever you want.

```
from codealerts import check_env, send_email

check_env()

### SOME CODE

send_email(SUBJECT, BODY)

### MORE CODE
```
You must provide the subject and body of the email you want to receive. And that's it :)
