import re


with open('potential-contacts.txt', 'r') as f:
    file = f.read()
    numbers = re.findall(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",file)
    not_dub_nums = list(dict.fromkeys(numbers))
    not_dub_nums.sort()
            
with open('phone_numbers.txt', 'w') as nums:
    content = ''
    for i in not_dub_nums:
        content+= i+'\n'
    nums.write(content)

with open('potential-contacts.txt', 'r') as fTwo:
    file = fTwo.read()
    mails = re.findall(r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}",file)
    not_dub_mails = list(dict.fromkeys(mails))
    not_dub_mails.sort()
    print(len(not_dub_mails))

with open('emails.txt', 'w+') as mail:
    content = ''
    for i in not_dub_mails:
        content+= i+'\n'
    mail.write(content)