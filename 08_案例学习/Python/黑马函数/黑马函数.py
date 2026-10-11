#案例一
def area(d,h):
    return d*h/2

print(area(5,5))
#案例二
def yuanyin(h):
    a=0
    for i in h:
        if i in "aeiouAEIOU":
            a=a+1
        else:
            pass
    return a
#案例三
def gaokao(a):
    max=0
    sum=0
    min=a[0]
    for i in a:
        if i >max:
            max=i
        else:
            pass
        if i<min:
            min=i
        else:
            pass
        sum=sum+i
    ave=round(sum/len(a),1)
    return max,min,ave
print(yuanyin("Hello AE"))
print(yuanyin("rhythm"))
print(yuanyin(""))

print(gaokao([60, 80, 100]))
print(gaokao([75]))
print(gaokao([0]))