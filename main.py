import re
import shutil


# create function that gets all emails from a file
# function should also write to a new file called
def get_emails(file):
    """[Function]: Parses out file for emails and sets number.
       [Params]: file - takes in a file location
     """
    try:
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
            # print(f'({email_count})Email: {email}')
        return email
    except:
        raise Exception


#     create function to get phone numbers
def get_phone_numbers(file):
    try:
        file_stringified = ''
        all_phone_numbers = []
        with open(file) as f:
            read_file = f.readlines()
        for text in read_file:
            file_stringified += text
        #     find all phone numbers with a xxx-xxx-xxxx format
        phone_numbers = re.findall("\w{3}-\w{3}-\w{4}", file_stringified)
        phone_number_count = 0
        for number in phone_numbers:
            phone_number_count += 1
            all_phone_numbers.append(number)
            # print(f'{phone_number_count} Phone#: {number}')
        return all_phone_numbers


    except:
        raise Exception


if __name__ == "__main__":
    text_file = 'assets/potential-contacts.text'
    get_emails(text_file)
    get_phone_numbers(text_file)