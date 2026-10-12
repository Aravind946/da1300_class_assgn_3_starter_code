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
    for j in range(len(ships)-1):
        counter=0
        for i in range(len(ships)-2,-1,-1):
            if i+1+counter==0:
                break
            if ships[i+counter]>0 and ships[i+1+counter]<0:
                if abs(ships[i+counter])<abs(ships[i+1+counter]):
                    ships.pop(i+counter)
                    counter+=0
                elif abs(ships[i+counter])>abs(ships[i+1+counter]):
                    ships.pop(i+1+counter)
                    counter+=0
                elif abs(ships[i+counter])==abs(ships[i+1+counter]):
                    ships.pop(i+counter)
                    ships.pop(i+counter)
                    counter-=1
    return ships
    pass


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8,-8]))     # expected: []
