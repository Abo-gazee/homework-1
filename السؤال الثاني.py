def converter(binary_num):
    decimal_num=0
    l=[]
    try:
        for i in binary_num:
            l.append(int(i))
        l.reverse()
        for i in range(len(l)):
            decimal_num+=l[i]*2**i
        return decimal_num
    except ValueError as e:
        return e
        
b=input("input binary number: ")
print(converter(b))
