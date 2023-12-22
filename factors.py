#!/usr/bin/python3
def factorize(n):
    """
    Factorize a number into a product of two smaller numbers.

    Args:
        n (int): The number of to factorize.

    Return:
        tuple: A tuple containing two factors of the number.
    """
    for i in range(2, int(n**0.5) + 1):
        if n %i:
            continue
        return i, n // i
    return 1, n

def main():
    """
    Main function to read numbers from a file, factorize them,
    and print the results
    """
    import sys
    if len(sys.argv) != 2:
        print("usage: {} <file>".format(sys.argv[0]))
        return

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            n = int(line.strip())
            p, q = factorize(n)
            print("{} = {} * {}".format(n, p, q))

if __name__ == "__main__":
    """
    Excecute main function if the script is run as a standalone module.
    """
    main()
