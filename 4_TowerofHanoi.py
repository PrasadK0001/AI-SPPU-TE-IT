def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", target)
        return
    hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from rod", source, "to rod", target)
    hanoi(n-1, auxiliary, target, source)

# Example usage
n = 3
print("Tower of Hanoi with", n, "disks:")
hanoi(n, 'A', 'C', 'B')



'''The Towers of Hanoi is a classic mathematical puzzle that involves moving a stack of disks from one peg to another peg, with the constraint that only one disk can be moved at a time and no disk can be placed on top of a smaller disk.

The puzzle consists of three pegs and a number of disks of different sizes which can slide onto any peg. The initial state has all the disks stacked in increasing order of size on one peg, with the smallest disk at the top and the largest disk at the bottom. The objective is to move all the disks to another peg, following the rules, using the fewest possible moves.

The problem is usually solved recursively. The recursive solution can be stated as follows:

1. Move n-1 disks from the source peg to the auxiliary peg.
2. Move the nth disk from the source peg to the target peg.
3. Move the n-1 disks from the auxiliary peg to the target peg.

This recursive process is continued until all disks are moved to the target peg.

The number of moves required to solve the Towers of Hanoi puzzle with n disks is 2^n - 1.'''
