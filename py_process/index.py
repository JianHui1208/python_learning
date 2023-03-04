import string
import random

i = 1
while i < 10:
    try:
        text_title_length = 10
        title = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = text_title_length))    

        text_input_length = 100
        input = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = text_input_length))    

        with open(str(title)+'.txt', 'w') as f:
            f.write(str(input))
    except FileNotFoundError:
        print("The 'docs' directory does not exist")

    i += 1