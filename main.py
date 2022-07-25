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
        all_emails = []
        with open(file) as f:
            read_file = f.readlines()
        for text in read_file:
            file_stringified += text
        # find all the emails
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', file_stringified)
        # set email count so we know how many we have

        for email in emails:
            all_emails.append(email)
        emails_file = open(r'assets/emails.text', 'w')
        email_count = 0
        for new_contact in all_emails:
            email_count += 1
            emails_file.write(f'{email_count} Email: {new_contact}' + '\n')
        phone_numbers_file.close()

        return all_emails
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
        phone_numbers = re.findall("[0-9-]+[0-9-]+[0-9-]", file_stringified)

        for number in phone_numbers:
            if 8 < len(number) < 15:
                all_phone_numbers.append(number)
        # write to the email  file
        phone_numbers_file = open(r'assets/phone_numbers.text', 'w')
        phone_number_count = 0
        for number in all_phone_numbers:
            phone_number_count += 1
            phone_numbers_file.write(f'{phone_number_count} Phone#: {number}' + '\n')
        phone_numbers_file.close()

        return all_phone_numbers


    except:
        raise Exception


if __name__ == "__main__":
    text_file = 'assets/potential-contacts.text'
    print(get_emails(text_file))
    print(get_phone_numbers(text_file))

