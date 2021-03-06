def sqrt(x):
    """comput square roots using the method of hern of alexandria
	Args:
	    x: the number for which the square root is to be computed
    Returns:
        the square root of x
    """
    if x < 0:
        raise ValueError('Cannot compute square root of negative number {}'.format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

		
def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError:
        print('Cannot compute aquare root of a negative number.')
    print('Program execution continues normally here')
	
	
if __name__ == '__main__':
    main()