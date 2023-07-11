import re

# html 주소에서 html 태그만제거 하여 택스트만 출력하는 코드.

html = "<p>This is <b>bold</b> text.</p>"
pattern = r"<.*?>"
clean_text = re.sub(pattern, "", html)
print(clean_text)  # 출력: This is bold text.
