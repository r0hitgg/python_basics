# Decorator 

def star(func):
    def print_star(*args, **kwargs):
        print('*'*30)
        func(*args, **kwargs)
        print('*'*30)
    return print_star

@star
def print_message(message):
    print(message)

print_message('ROHIT')