def isFull(n, s, top):
    if top == n:
        return True
    else:
        return False

def isEmpty(top):
    if top == 0:
        return True
    else:
        return False

def push(s, n, top):
    if isFull(n, s, top):
        print("Cannot push: Stack is full")
    else:
        element = input("Enter the element to push: ")
        s.append(element)
        return top + 1  # Return updated top position

def pop(s, top):
    if isEmpty(top):
        print("Cannot pop: Stack is empty")
    else:
        popped_element = s.pop()
        print(f"{popped_element} is popped")
        return top - 1  # Return updated top position

# Main program
n = int(input("Enter size of stack: "))
s = []
for i in range(n):
    element = input("Enter element: ")
    s.append(element)
top = 0

print("Initial stack:", s)

while True:
    inp = input("Enter the choice (1-push, 2-pop, 3-display, 4-exit): ")

    if inp == "1":
        top = push(s, n, top)
        print("Pushed the element")

    elif inp == "2":
        print("Popped the element")
        top = pop(s, top)

    elif inp == "3":
        print("Elements in stack:", s)

    elif inp == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1-push, 2-pop, 3-display, or 4-exit")
