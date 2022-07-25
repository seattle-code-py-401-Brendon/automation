# LAB - Class 19
## Project: Automation
### Author: Brendon H.
### Links and Resources
- [back-end server url](#) (when applicable)
- [front-end application](#) (when applicable)
### Setup
`.env` requirements (where applicable)

**i.e.**

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db
#### How to initialize/run your application (where applicable)
- e.g. `python automation.py`
#### How to use your library (where applicable)
- use this by just calling main.py. you will see a list of all the emails/phone numbers extracted.
#### Tests
- How do you run tests?
  - run **pytest** in the terminal after instantiating a virtual environment.
- Any tests of note?
  - there are two tests
    - test_get_email():
      - gets an email from a string
    - test_get_phone_number():
      - gets a phone number from a string
      - the functionality is set to include numbers in larger and smaller formats but not by  much, a phone number is never in 4 digits for example.
- Describe any tests that you did not complete, skipped, etc
  - I added tests for basic functionality, I would have liked to add tests to test for duplicates and for anything too large to be a phone number or too small.


## Final Thoughts:
- I would like to dive deeper into try/excepts. I understand the basics of it, but I would like to use case scenarios so I can maybe build my own exceptions that give the user a better experiience in case of faults.