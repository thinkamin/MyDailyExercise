import re

# email
email_negex = re.compile('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w)*$')
email='774799513@qq.com'
email2 = 'www.baidu.com'
print(email_negex.match(email))
print(email_negex.match(email2))



