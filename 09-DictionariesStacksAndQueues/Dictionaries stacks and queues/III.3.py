import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct


   
   


brackets = queue.LifoQueue()

def brackets_ok(expression):
    for i in expression:
        if i in ("(","[","{"):
            brackets.put(i)
        if i in (")","]","}"):
            bracket = brackets.get()
            if i == ")" and bracket == "(":
                continue
            elif i == "]" and bracket == "[":
                continue
            elif i == "}" and bracket == "{":
                continue
            else:
                return False
    if brackets.empty() == False:
        return False
    return True



if brackets_ok(expression1):
   print("Correct Brackets")
else:
   print("Wrong Bracketts")


if brackets_ok(expression2):
   print("Correct Brackets")
else:
   print("Wrong Bracketts")

if brackets_ok(expression3):
   print("Correct Brackets")
else:
   print("Wrong Bracketts")


