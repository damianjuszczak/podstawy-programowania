import re

def email_sender(content):
    match = re.search(r'From: .*<(.+?)>', content)
    return match.group(1)

def email_recipient(content):
    match = re.search(r'To: .*<(.+?)>', content)
    return match.group(1)

def email_subject(content):
    match = re.search(r'Subject: (.+)', content)
    return match.group(1)

def email_body(content):
    parts = content.split('\n\n', 1)
    return parts[1].strip()
