
def print99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d x %d = %d" % (j, i, j * i), end = " ")
        print("")


print99()


def wordCount(str):
    count = 0
    wordList = str.split(" ")
    for word in wordList:
        if len(word) > 0:
            count += 1
    #print("count =", count)
    return count

res = wordCount("sunck is a good man")
if res >= 5:
    print("right")
else:
    print("aaa")




def printsxh():
    sxhList = []
    for num in range(100, 1000):
        a = num % 10
        b = num // 10 % 10
        c = num // 100

        if num == a**3 + b**3 + c**3:
            sxhList.append(num)
    return  sxhList

l = printsxh()
print(l)

