# num_of_students=int(input("enter the number of students"))
# start=1
# total_students_marks=[]
# while start<=num_of_students:
#     print(f"***********ROLL NO:{start}***********")
#     for i in range(1):
#         nep=int(input("ENTER NEPALI MARKS:"))
#         eng=int(input("ENTER ENGLISH MARKS:"))
#         math=int(input("ENTER MATH MARKS:"))
#         chem=int(input("ENTER CHEMISTRY MARKS:"))
#         phy=int(input("ENTER PHYSIC MARKS:"))
#         comp=int(input("ENTER COMPUTER MARKS:"))
#         total=nep+eng+math+chem+phy+comp
#         total_students_marks.append(total)
#     start+=1


# i=1
# for total in total_students_marks:
#     per=total/6
#     grade=""
#     if per>35 and per<=45:
#         grade="D"
#     elif per>45 and per<=55:
#          grade="C"
#     elif per>55 and per<=65:
#          grade="B"
#     elif per>65 and per<=75:
#          grade="A"
#     elif per>75 and per<=100:
#         grade="A+"
#     else:
#         grade="fail"
#     print(f"ROLL NO:{i} TOTAL:{total} PERCENTAGE:{per} GRADE:{grade}")
#     i+=1

# print("**********PRODUCT MODULE**********")
# num=int(input("enetr the number of products"))
# product_list=[]
# x=1
# while x<=num:
#     print(f"********PRODUCT NO:{x}********")
#     name=input("enter the name of product:")
#     quantity=int(input("enter the no of product:"))
#     price=int(input("enter the price of the product:"))
#     total=quantity*price
#     p_data={"NAME":name,"QUANTITY":quantity,"PRICE":price,"TOTAL":total}
#     product_list.append(p_data)
#     x+=1
# print("PRODUCT NAME\t QUANTITY\t PRICE\t TOTAL")
# for product in product_list:
#     print(f"{product['NAME']}\t\t {product['QUANTITY']}\t\t{product['PRICE']}\t\t{product['TOTAL']}")    


# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sita','gender':'female','status':False},
#     {'name':'hari','gender':'male','status':False},
#     {'name':'geta','gender':'female','status':False},
#     {'name':'ramu','gender':'male','status':True},
#     {'name':'sophia','gender':'female','status':True}
#     ]
# total_students=len(students)
# total_male=0
# total_female=0
# active_male=0
# active_female=0
# inactive_male=0
# inactive_female=0
# for student in students:
#     if student['gender']=='male':
#         total_male+=1
#         if student['status']==True:
#               active_male+=1
#         else:
#          inactive_male+=1
    
#     else:
#         total_female+=1
#         if student['status']==True:
#              active_female+=1
#         else:
#             inactive_female+=1 
# print(f'total students:{total_students}')
# print(f'total male:{total_male}')
# print(f'total female:{total_female}')   
    
       
# print(f'total active male students:{active_male}')
# print(f'total active female students:{active_female}')
# print(f'total inactive male students:{inactive_male}')
# print(f'total inactive female students:{inactive_female}')  

x=1
while x<=50:
    if x==22 or x==33 or x==44 or x==49:
        print(x) 
        x+=1






