## ---------- load data and create account list ----- ##
def load_list(file):
    b = open(file, 'r')
    data = b.readlines()
    b.close()

    accounts = []
    for i in data:
        accounts.append((i.strip().split(',')))
    return(accounts)
      
## ----------- get account index -------------------- ##
def account_index(name):
    for user in accounts:
        if user[0] == name:
            return user;

## ----------- check to see login is correct -------- ##
def is_login_valid(name,password):
    for i in accounts:
        if i[0] == name:
            if i[1] == password:
                return True
    return False

## ------------ displays account information --------- ##
def print_account(user):
    return(f"\nName: {user[2]}\nBalance: {user[3]}")
    print()

## ------------ runs program ------------------------ ##
accounts=load_list('data.txt')
logged_in = False

while not logged_in:
    print()
    print("|--------------------------------|")
    print()
    name = str(input("Enter Name: "))
    user = account_index(name)

    password = str(input("Enter Password: "))

    print()
    print("              ...              ")

    if (is_login_valid(name, password)):
        print(print_account(user))
        logged_in = True
        print()
        print("|--------------------------------|")
        print()
    else: 
        print()
        print("username and password not found")
    

logged_in = False