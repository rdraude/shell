import turtle

_LENGTH = 22
_SCALE = 0.05

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
    """
    Writes the fibonacci shell graphics
    """
    dp_list = [0] * (_LENGTH + 1)
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    draw = turtle.Turtle()
    draw.color("blue")
    draw.speed(2)
    draw.shape("turtle")
    draw.width(10)
    #Fibonacci loop:
    for i in range(1, _LENGTH+1):
        fib(i, dp_list)
        draw.forward(dp_list[i] * _SCALE)
        draw.right(90)
        screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()