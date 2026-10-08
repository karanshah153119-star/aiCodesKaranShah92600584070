#Tower Of Hanoi

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    tower_of_hanoi(n - 1, source, destination, helper)
    print("Move Disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, helper,source,destination)

# Number Of Disks
n = int(input("Enter number of disks : "))

# Solve Tower Of Hanoi
tower_of_hanoi(n, "A", "B", "C")

print("Total Moves : ", (2 ** n) - 1)