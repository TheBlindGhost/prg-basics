import re



def email_sender(content):
    mail = ''
    for line in content:
       if re.match("From: " + r'[*]{0,50}', line):
        mail = line
    return mail

    

def email_recipient(content):
    mail = ''
    for line in content:
       if re.match("To: " + r'[*]{0,50}', line):
        mail = line
    return mail

def email_subject(content):
    mail = ''
    for line in content:
       if re.match("Subject: " + r'[*]{0,50}', line):
        mail = line
    return mail

def email_body(content):
    line_num = 0
    for line in content:
        if re.match("Hi" + r'[*]{0,50}', line):
            break
        line_num += 1
    for i, line in enumerate(content):
        if i >= line_num:
            print(line)