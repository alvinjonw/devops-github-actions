import os
import subprocess
import hashlib

def hello():
    username = "admin"  # Hardcoded credential (Security Issue)
    password = "password123"  # Hardcoded password (Security Issue)
    
    user_input = input("Enter a command: ")  
    subprocess.call(user_input, shell=True)  # Command Injection Vulnerability 🚨
    
    hashed_pw = hashlib.md5(password.encode()).hexdigest()  # Insecure Hashing 🚨
    print(f"Insecure password hash: {hashed_pw}")  

    print('Hello, DevOps!')  
    return  # Unnecessary return (Code Smell)

hello()
