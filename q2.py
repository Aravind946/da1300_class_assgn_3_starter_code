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
    for i in range(len(ships)):
        for j in range(len(ships)-1):
            if ships[j]>0 and ships[j+1]<0:
                if abs(ships[j])<abs(ships[j+1]):
                    ships.pop(j)
                elif abs(ships[j])>abs(ships[j+1]):
                    ships.pop(j+1)
                elif abs(ships[j])==abs(ships[j+1]):
                    ships.pop(j)
                    ships.pop(j)
    return ships
    pass


if __name__ == "__main__":
    # Example sanity checks (see test.py for the real test cases)
    print(surviving_ships([6, 3, -5]))  # expected: [6]
    print(surviving_ships([8, -8]))     # expected: []
