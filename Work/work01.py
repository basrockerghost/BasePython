p = 100

def Compute_Price (a):
    global t
    t=a*p
    return float(t)

def Compute_Discount():
    if t>=1000:
        print('Discount :', t*0.05,'Baht')
        n=t-(t*0.05)
        return float(n)
    else:
        return float(t)

def main():
    print('Totalprice :',(Compute_Price(11)),'Baht')
    print('Netprice :',(Compute_Discount()),'Baht')

main()

# p=100
# a=int(input('Enter amount : '))
# t=a*p
# if float (t>=1000):
#     print('Discount :',t*0.05)
#     t=t-(t*0.05)
# print('Netprice :',t)

# tackle & data world