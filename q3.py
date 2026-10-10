from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right


def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each node has a `salary`,
    count the number of nodes whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root TreeNode of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    ans=0
    l=[]
    def findmanagers(node):
        nonlocal l
        if node==None:
            return
        l.append(node)
        findmanagers(node.left)
        findmanagers(node.right)
    findmanagers(root)
    salaries=[]
    salary=[]
    def findsalaries(node):
        nonlocal salaries
        nonlocal salary
        if node==None:
            return
        salary.append(node.salary)
        findsalaries(node.left)
        findsalaries(node.right)
    for i in l:
        salary=[]
        findsalaries(i)
        salaries.append(sum(salary)//len(salary))
    for i in range(len(l)):
        if l[i].salary==salaries[i]:
            ans+=1
    return ans 


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
