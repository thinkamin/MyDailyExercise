string="((1+2)+3))"
def test(string):
    test=[]
    for item in string:
        if item == "(":
            test.append(item)
        if item ==")":
            if test:
                test.pop()
            else:
                return False
    if test:
        return False
    else:
        return True
print(test(string))
