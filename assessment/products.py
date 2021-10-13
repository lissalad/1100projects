## ---------- load products and return list ------- ##
def load_list(file):
  pro = open(file, 'r')
  products = pro.readlines()
  pro.close()

  product_list = []
  for i in products:
      product_list.append((i.strip().split(',')))
  return(product_list)

## ----------- get product index ------------------ ##
def product_index(name):
    for i in product_list:
        if name.casefold() in i[1].casefold():
            return i

## ----------- check to see product exists -------- ##
def product_exists(item):
    for i in product_list:
        if name.casefold() in i[1].casefold():
          return True
    return False

## ------------ displays product information ------ ##
def print_product(item):
  product = item[1]
  price = float(item[2])
  count = float(item[3])
  total = count*price

  return(f"\n{product}\nPrice: {price}\nCount: {count}\nTotal: {total}")
  

## ------------ runs program ------------------------ ##
product_list=load_list('products.txt')
searching = True

while searching:
  print()
  print("|--------------------------------|")
  print()
  name = str(input("Search: ")) # PROMPT
  index = product_index(name)

  print()
  print("              ...              ")

  if (product_exists(name)):
    print(print_product(index)) # DISPLAY 
    print()
    print("|--------------------------------|")
    print()
  else: 
    print()
    print("item not found\n") # DISPLAY
  again = str(input("Search again? yes/no\n")) # PROMPT
  if not again == "yes":
    searching = False
