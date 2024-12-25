import random
import string
import sys

help_strings = ["--help", "-h"]


def print_help():
    print("""
# Password Generator
Usage: passgen [length] [flags]

Flags: 1000 for numbers,
       0100 for uppercase,             
       0010 for lowercase,           
       0001 for symbols

Example: passgen 8 1111  => output: '=B@9cMLl'            
         passgen 8 0010  => output: 'ckqmjbkg'            
         passgen 8 1000  => output: '75095112'            
    """)


def generate_password(length: int = 8, flags: string = "1111"):
    result =  ''.join(random.choice(""
                                 + (string.digits if flags[0] == "1" else "")
                                 + (string.ascii_uppercase if flags[1] == "1" else "")
                                 + (string.ascii_lowercase if flags[2] == "1" else "")
                                 + ("!@#$%^&*()_+=-" if flags[3] == "1" else "")
                                 ) for _ in range(length))



if __name__ == '__main__':
    args = sys.argv

    if len(args) == 2 and args[1].lower() in help_strings:
        print_help()
        sys.exit(0)

    pass_len = int(args[1]) if len(args) > 1 else 8
    if len(args) > 2 and 0 <= int(args[2]) <= 15:
        pass_flags = f"{int(args[2]):b}"
        pass_flags = f"{int(pass_flags):04}"
    elif len(args) > 2 and len(str(args[2])) == 4:
        pass_flags = str(args[2])
    else:
        pass_flags = "1111"

    if pass_flags != "0000":
        generate_password(pass_len, pass_flags)
