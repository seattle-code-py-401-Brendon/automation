import re
import shutil


# create function that gets all emails from a file
# function should also write to a new file called
def get_emails(file):
    """[Function]: Parses out file for emails and sets number.
       [Params]: file - takes in a file location
     """
    file_stringified = ''
    with open(file) as f:
        read_file = f.readlines()
    for text in read_file:
        file_stringified += text
    # find all the emails
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', file_stringified)
    # set email count so we know how many we have
    email_count = 0
    for email in emails:
        email_count += 1
        print(f'({email_count})Email: {email}')
    return email


#     create function to get phone numbers
def get_phone_numbers(file):
    try:
        pass

    except:
        raise Exception


if __name__ == "__main__":
    text_file = 'assets/potential-contacts.text'
    get_emails(text_file)