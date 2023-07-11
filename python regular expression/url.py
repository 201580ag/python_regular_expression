import re

# 문자열에 url 주소가 있으면 url 주소만 추출해서 출력하는 코드.

text = "Visit my website at https://www.google.com/."
pattern = r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
urls = re.findall(pattern, text)
print(urls)  # 출력: ['https://www.example.com']
