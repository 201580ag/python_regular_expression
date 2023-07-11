import re

# 문자열에 숫자가 있으면 숫자만 출력하는 코드.

text = "The price is $19.99."
pattern = r"\d+\.\d+"
numbers = re.findall(pattern, text)
print(numbers)  # 출력: ['19.99']
