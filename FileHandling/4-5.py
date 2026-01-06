import emails

with open('email.txt', 'r', encoding='utf-8') as file:
    content = file.read()

sender = emails.email_sender(content)
recipient = emails.email_recipient(content)
subject = emails.email_subject(content)
body = emails.email_body(content)

print(f'Email sender: {sender}')
print(f'Email recipient: {recipient}')
print(f'Email subject: {subject}')
print(f'Email body:\n{body}')