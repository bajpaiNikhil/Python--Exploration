import re

print("calculator==>MAGIC!!!!!!")
print("type 'quit' to exit!\n")

previous=0
run=True
equation=" "
def performMath():
    global run
    global previous
    #equation=" "
    if(previous==0):
        equation=input("Enter equation!")
    else:
        equation=input(str(previous))

    if (equation=="quit"):
        print("goodbye!!!!")
        run=False
    else:

        equation=re.sub('[a-zA-Z,.:()" "]', '',equation)
        if(previous==0):
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)


while run:
    performMath()
