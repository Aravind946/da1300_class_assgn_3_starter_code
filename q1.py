from typing import List


def printer_queue_order(pages: List[int]) -> List[int]:
    """
    Problem 1: Round-robin printer.

    Given the number of pages for each document (in submission order),
    simulate round-robin printing (one page at a time, front of queue
    to back of queue) and return the document indices in the order
    they finish printing.

    Args:
        pages: pages[i] is the number of pages in document i.

    Returns:
        List of document numbers in the order they finish printing.
    """
    l=[i for i in range(len(pages))]
    counter=0
    while True:
        if len(pages)==0:
            break
        elif pages[0]==1:
            counter+=1
            pages.pop(0)
        else:
            pages.append(pages[0]-1)
            pages.pop(0)
            l.append(l[0])
            l.pop(0)
    return l
    pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    print(printer_queue_order([1, 1, 1]))  # expected: [0, 1, 2]
