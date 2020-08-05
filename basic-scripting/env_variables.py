import os

from secret import password

if os.environ.get("PASSWORD") is None:
    password_env = password
else:
    password_env = os.environ["PASSWORD"]

output = f"Your password is {password_env}"

print(output) 