def sum_and_mul(a,b):
    return a+b, a*b

a = sum_and_mul(3,4)
print(a)

def say_myself(name, age, man = True):
    print("My name is %s." %name)
    print("I'm %d years old." %age)
    if man:
        print("Male.")
    else:
        print("Female.")

say_myself("Tom", 26, True)
say_myself("James", 22)
say_myself("Alice", 24, False)
