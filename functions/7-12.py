#f(4) returns "*/*/*/*"
#f(1) returns "*"

def f(n):
    return "/".join(["*"] * n)

print(f(4)) 
print(f(1)) 