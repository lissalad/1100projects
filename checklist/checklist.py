# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

checklist = []


def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
        index = 0
        for list_item in checklist:
            print("{} {}".format(index, list_item))
            index += 1

def mark_completed(index):
    # checklist[index] = "√ " + checklist[index]
    update(index, "√ " + checklist[index]) # QUOTES?
    print(checklist[index])

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
            # This is where we want to stop our loop
            return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    return input(prompt)


def test():
    user_value = user_input("Please Enter a value:")
    print(user_value)

    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))
    # # print(read(1)) 

    # list_all_items()
    # mark_completed(0)

    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()

# test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)