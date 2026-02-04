def imple_circuit(A, B, C):
    """Compute output Q of the shown circuit using bitwise operators.

    Circuit simplifies to: Q = (A & B) | (B & C)  == B & (A | C)

    Inputs may be 0/1 or booleans. Returns 0 or 1.
    """
    A = 1 if A else 0
    B = 1 if B else 0
    C = 1 if C else 0
    return (A & B) | (B & C)


if __name__ == "__main__":
    # If three arguments provided, compute single result; otherwise print full truth table.
    import sys

    if len(sys.argv) == 4:
        try:
            A, B, C = map(int, sys.argv[1:4])
        except ValueError:
            print("Provide three integers 0 or 1")
            sys.exit(1)
        print(imple_circuit(A, B, C))
    else:
        print("A B C | Q")
        for A in (0, 1):
            for B in (0, 1):
                for C in (0, 1):
                    print(f"{A} {B} {C} | {imple_circuit(A, B, C)}")
