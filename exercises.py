def exercise1(arg):
    return [x for x in arg]

def exercise2(arg):
    return [x * x for x in arg]

def exercise3(arg):
    return [x for x in arg if x % 2 == 0]

def exercise3dot1(arg):
    return [x for x in arg if x % 3 == 0 or x % 5 == 0]

def exercise3dot2(arg):
    return [x * x for x in arg if x % 3 == 0 or x % 5 == 0]

def exercise4(arg):
    return [x*2 if x % 2 == 0 else x*3 for x in arg]

def exercise5(arg):
    return [x * x for x in [x * x for x in arg]]

def exercise6(arg):
    return [[y + idx for y in arg] for idx, x in enumerate(arg)]
