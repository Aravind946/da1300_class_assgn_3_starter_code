from typing import List


def surviving_ships(ships: List[int]) -> List[int]:
    """
    Problem 2: Spaceship collisions.

    Given a list of ship engine powers (sign = direction: positive is
    right, negative is left), resolve all collisions between ships
    moving toward each other and return the engine powers (with sign)
    of the ships that remain.

    Args:
        ships: list of signed engine powers.

    Returns:
        List of signed engine powers of surviving ships, left to right.
    """
    l=[]
    for i in ships:
        if len(l)==0:
            l.append(i)
            continue
        while True:
            if len(l)==0:
                 l.append(i)
                 break
            if l[-1]>0 and i<0:
                if abs(l[-1])>abs(i):
                        break
                elif abs(l[-1])<abs(i):
                        l.pop()
                elif abs(l[-1])==abs(i):
                     l.pop()
                     break
            else:
                 l.append(i)
                 break
    return l
    pass


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8,-8]))     # expected: []
