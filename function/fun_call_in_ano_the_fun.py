#non-recursive function
print("welcome")

    
def display():
    print("this is display")
    show()
    print("end of display")
    return
def show():
    print("this is show")
    return


display()

print("end of program")
