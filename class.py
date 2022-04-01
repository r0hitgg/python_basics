class A:

    def print_some(self, message):
        message = 'A -> %s' % message
        print(message)
        return message

class B(A):

    def print_some(self, message):
        res = super().print_some(message)
        print('SUPER -> %s' % res)
        res += ' -> B -> %s' % message
        print(res)
        return res

class C(B):

    def print_some(self, message):
        res = super().print_some(message)
        return res

obj = C()
obj.print_some('ROHIT')
