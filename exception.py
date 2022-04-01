from decimal import DivisionByZero


def run(num, div):
    # result = num / 0 -> division by zero
    try:
        result = num / div
    except:
        print('Can Not Divide By Zero')
    finally:
        result = num
    print(result)

run(100, 0)
run(100, 10)
