amount=int(input('enter the amount'))
if amount<=1000:
    discount=0.05*amount
    print('Discount is',discount)
else:
     discount=0.1*amount
     print('Discount is',discount)
netpayableamount=amount-discount
print('Net payable amount is',netpayableamount)
