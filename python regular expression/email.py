import re

# 이메일 주소를 입력하면 이메일 형식에 맞는지 아닌지 확인하는 코드.

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("이메일 주소를 입력 해 주세요. : ")

print(validate_email(email))

input()