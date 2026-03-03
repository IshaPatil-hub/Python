# 8.Password strength checker
# Problem: Check if a password is "Weak", "Medium", or "strong". Criteria: <6 chars (weak), 6-10 chars (Medium), >10 char(strong).

password = "Secure3@Pass"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else: 
    strength = "Strong"

print("Password strength is: ", strength)


