import re

str = "110   login"
if re.search(r'\d{1,4}\s+[a-z]+', str) and len(str) > 0 and len(str)<20:
    print("aaaaaaaaaa")
else:
    print("error")