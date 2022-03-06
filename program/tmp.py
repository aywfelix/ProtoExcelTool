import re

# str = "110   login"
# if re.search(r'\d{1,4}\s+[a-z]+', str) and len(str) > 0 and len(str)<20:
#     print("aaaaaaaaaa")
# else:
#     print("error")

def Singleton(cls):
    _instance = {}

    def _Singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _Singleton

@Singleton
class Tmp1(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    t1 = Tmp1()
    t2 = Tmp1()
    print(id(t1)==id(t2))
    
    k = {}
    k[1] = []
    k[2] = []
    print(k)
    k["aa"] = []
    print(k)
    
    kk = k["bb"] = "bb"
    print(kk)