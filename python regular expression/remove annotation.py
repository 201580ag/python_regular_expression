import re

# 주석이 되어 있는 코드에서 주석만 제거 하여 출력하는 코드.

code = """
def add(a, b):
    # 두 수를 더함
    return a + b

# 결과 출력
print(add(3, 4))
"""
pattern = r"#.*$"
clean_code = re.sub(pattern, "", code, flags=re.MULTILINE)
print(clean_code)
