import re

# html 주소에서 html 태그만 추출하여 출력하는 코드.

html = "<p>This is a <strong>bold</strong> statement.</p>"
pattern = r"<.*?>"
tags = re.findall(pattern, html)
print(tags)  # 출력: ['<p>', '<strong>', '</strong>', '</p>']
