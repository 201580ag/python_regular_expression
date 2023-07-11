import re

text = "제 주민등록번호는 950101-1234567입니다."
pattern = r"\d{6}-\d{7}"
masked_text = re.sub(pattern, "******-*******", text)
print(masked_text)  # 출력: 제 주민등록번호는 ******-*******입니다.
