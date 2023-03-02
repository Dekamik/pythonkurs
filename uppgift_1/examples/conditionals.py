def if_else_elif(condition):
    if condition:
        return 1
    elif not condition:
        return -1
    else:
        return 0


def tertiary():
    return 1 if True else -1 if False else 0


def match():
    command = "read"
    match command:
        case "read":
            print("read selected")
            
        case "write":
            print("write selected")

        case _:
            print("unknown commnad")
