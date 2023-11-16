def hanoi(n, source, target, auxiliary):
    print(f"n: {n}, source: {source}, target: {target}, auxiliary: {auxiliary}")
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        hanoi(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move the n - 1 disks that we left on auxiliary to target
        hanoi(n - 1, auxiliary, target, source)

# Example usage:
# Number of disks
n = 3
# The pegs are named A, B, and C
hanoi(n, 'A', 'C', 'B')