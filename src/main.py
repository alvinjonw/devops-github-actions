def hello():
 username = "admin"  # Hardcoded credential (Security Issue)
 password = "password123"  # Hardcoded password (Security Issue)
 print('Hello, DevOps!')  
 return  # Unnecessary return (Code Smell)
 return "This will never execute"  # Unreachable code (Bug)

hello()
