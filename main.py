import os
if not os.path.exists('user.txt'):
    handle=open('user.txt','w')
    handle.close()
books=[
    {'id':1,'name':'python','price':100},
    {'id':2,'name':'java','price':200},
    {'id':3,'name':'c++','price':300},
    {'id':4,'name':'c#','price':400},
    {'id':5,'name':'php','price':500}
]
def register():
    print("=========register=========")
    username=input("enter username:").strip()
    if username in open('user.txt').read():
        print("username already exists")
        exit()
    password=input("enter the password").strip()
    confirm_password=input("enter the password again").strip()
    if password!=confirm_password:
        print("password didnt match")
        exit()
    handle=open('user.txt','a')
    handle.write(f'{username},{password}\n')
    handle.close()
    print("user resgistered succesfully")

def login():
    print("=======login========")
    username=input("enter username:").strip()
    password=input("enter password:").strip()
    users=open('user.txt').readlines()
    is_login=False
    for user in users:
        user=user.strip().split(',')
        if user[0]==username and user[1]==password:
            is_login=True
        if is_login:
            print(f"=======welcome:{username}========")
            print("ID\t NAME\t PRICE")
            for book in books:
                print(f'{book['id']}\t{book['name']}\t{book['price']}')
                
            else:
                print("invalid username or password")
                exit()

question=input('do you have any account?(y/n):').strip()
if question=='y':
    login()
else:
    register()    






