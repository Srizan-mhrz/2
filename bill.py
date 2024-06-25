print("===============welcome user=============")
print("1.dell(rs:5000000) 2.hp(rs:6000000) 3.lenovo(rs:3000000)")
product_name=""
dell_price=0
hp_price=0
lenovo_price=0
quantity=0
option=int(input("enter what you whnat to buy:"))
if option==1:
    product_name="dell"
    quantity=int(input("enter how many do you want to buy:"))
    dell_price=5000000*quantity
elif option==2:
    product_name="hp"
    quantity=int(input("enter how many do you want to buy:"))
    hp_price=6000000*quantity
elif option==3:
    product_name="lenovo"
    quantity=int(input("enter how many do you want to buy:"))
    lenovo_price=3000000*quantity
else:
    print("invalid option")
    exit()

print("Delivery option: 1.home(rs:5000) 2.pickup(rs:0)")
delivery_price=0
delivery_mode=int(input("enter how you want your product to be delevered:"))
if delivery_mode==1:
    delivery_price=5000
elif delivery_mode==2:
    delivery_price=0    
else:
    delivery_price=0
print("packing option: 1.plastic_bag(rs:100) 2.gift_wrap(rs:500)")
packing_price=0
packing=int(input("enter how you would like to pack:"))
if packing==1:
    packing_price=100
elif packing==2:
    packing=500
else:
    packing_price=0
total_price=dell_price+hp_price+lenovo_price
tax_amount=0
print("Location: 1.ktm(sr:13%) 2.lalitpur(rs:0%) 3.bhaktapur(rs:0%)")
Location=int(input("enter the location:"))
if Location==1:
    tax_amount=total_price*0.13 
grand_total=total_price+tax_amount+delivery_price+packing_price
print("==========youu bill===========")
print("product name:",product_name)
print("quantity:",quantity)
print("delivery price:",delivery_price)
print("packing price:",packing_price)
print("total price:",total_price)
print("tax amount:",tax_amount)
print("grand total:",grand_total)
print("===========THANK YOU===========")                           
