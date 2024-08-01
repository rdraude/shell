import turtle

length = 200

def fib(n, dp_list):
    """
    Computes the nth fibonacci number using dynamic programming
    """
    assert n > 0 #1-index, first fibonacci number is 1, so is the second, ...
    #Base cases:
    if n == 1: return 1
    if n == 2: return 1
    #Check to see if we have already calculated it
    if dp_list[n] != 0: return dp_list[n]
    nth_fib = fib(n-1, dp_list) + fib(n-2, dp_list)
    #assigns list
    dp_list[n] = nth_fib 
    return nth_fib


def main():
    dp_list = [0] * (length + 1)
    #add in turtle drawing
    for i in range(1, length+1):
        fib(i, dp_list)

if __name__ == "__main__":
    main()