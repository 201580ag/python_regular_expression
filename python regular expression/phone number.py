import re

# 문자열에 전화번호가 있으면 전화번호만 추출해서 출력하는 코드.

text = "My phone number is 010-1234-5678."
pattern = r"\d{3}-\d{4}-\d{4}"
match = re.search(pattern, text)
if match:
    phone_number = match.group()
    print(phone_number)  # 출력: 010-1234-5678
