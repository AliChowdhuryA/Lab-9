
def _encrypt(s1):
    s2 = ''
    for x in s1:
        s2 += chr(ord(x)+4)
    return s2

def _decrypt(s1):
    s2 = ''
    for x in s1:
        s2 += chr(ord(x)-4)
    return s2
    
def main():
    s = "how do you do"
    s = _encrypt(s)
    print(s)
    print(_decrypt(s))
    
main()
