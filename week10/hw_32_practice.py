def push(stack, data, top):
    stack[top+1] = data;
    return (top+1)
def pop(stack, top):
    return top - 1;
def isMatch(x, y, left, right):
    if left.index(x)==right.index(y): return True
    return False
    
def M(s):
    stack = ['' for i in range(20)]
    left, right = ['{','[','(',"<","⊂"], ['}',']',')',">","⊃"]
    top =-1;
    for i in range(len(s)):
        if s[i] in left:
            top = push(stack,s[i],top)
        elif s[i] in right:
            if (top==-1): 
                return False
            if isMatch(stack[top], s[i], left, right)==False: 
                return False    
            top=pop(stack,top)
    if top==-1: 
        print("Pass")
        print(s.count("+"),s.count("-"),s.count("*"),s.count("/"),end=" ")
        
    else: 
        print("Fail")

def main():
    n=int(input())
    for s in range(n):
        s=input()
        M(s)
    

main()