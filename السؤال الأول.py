print("السؤال الأول")
print("الطلب A")
d={}
def func(k,v):
    d[k]=v
L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53]
for i in range(len(L1)):
    func(L1[i],L2[i])
print(d)

print(50*"*")
print("الطلب B")

def f(n):
    x=1
    if n>0:
        for i in range(1,n+1):
            x=x*i
        return x
    elif n==0:
        return 1
    else:
        return "error"
i=int(input("Enter number: "))
print(f(i))


print(50*"*")
print("الطلب C")

L=['Network','Bio','Programming','Physics','Music']
for i in range(len(L)):
    if L[i][:1]=='B':
        print(L[i])

print(50*"*")
print("الطلب D")

d={x:x+1 for x in range(11)}
print(d)
