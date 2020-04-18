import re
'''
给你一串字符串，判断这是否是手机号码
'''


def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39" and str[1:3] != "31":
        return False

    for i in range(3, 11):
        if str[i] < "0" or str[i] > "9":
            return False
    return True

def checkPhone2(str):
    #13912345678
    pat = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat, str)
    return res

'''
print(checkPhone2("13912345678"))
print(checkPhone2("139123456785"))
print(checkPhone2("1391234a678"))
print(checkPhone2("23912345678"))
print(checkPhone2("19012345678"))
'''

checkPhone2("asfjiawe13709876543afegerhg13599999999sgve")


'''
QQ        6到10位，全是数字
mail      suncksunck@163.com
phone     010-55348765
user      6到12位
passwd
ip
url
'''

re_QQ = re.compile(r"^[1-9]\d{5,9}$")
print(re_QQ.search("123567890987"))

