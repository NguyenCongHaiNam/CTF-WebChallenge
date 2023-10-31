import requests
import re
flag = "MSEC{"
for i in range(100):
    url = f"https://nguyenconghainam.github.io/CTF-WebChallenge/Redirect/chall{i}.html"
    res = requests.get(url).text
    print(f'chall{i}.html: ')
    if "part" in res:
        matches = re.findall(r'(?<=:\s).*', res)
# Kết quả là một danh sách các chuỗi sau dấu hai chấm (":")
        for match in matches:
            flag+=match
        print(f"Found: {flag}")
    if "part 2" in res:
        break
print(flag)