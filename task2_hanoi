def tower_of_hanoi(n, source, dest, aux, counter=[0]):
    """
    Solves the Tower of Hanoi puzzle.
    - n: Number of disks
    - counter: A list used as a mutable reference to track total moves
    """
    if n <= 0:
        return
    
    # Base Case: Move the smallest disk
    if n == 1:
        counter[0] += 1
        print(f"Step {counter[0]:02d}: Move disk 1 from {source} → {dest}")
        return
    
    # Step 1: Move (n-1) disks from Source to Aux
    tower_of_hanoi(n - 1, source, aux, dest, counter)
    
    # Step 2: Move the largest disk from Source to Dest
    counter[0] += 1
    print(f"Step {counter[0]:02d}: Move disk {n} from {source} → {dest}")
    
    # Step 3: Move (n-1) disks from Aux to Dest
    tower_of_hanoi(n - 1, aux, dest, source, counter)

def run_simulation():
    try:
        num_disks = int(input("Enter number of disks: "))
        if num_disks > 10:
            confirm = input(" This will take many steps. Continue? (y/n): ")
            if confirm.lower() != 'y': return

        print(f"\n--- Solving for {num_disks} disks ---")
        total_moves = [0] # Using a list to track state across recursive calls
        tower_of_hanoi(num_disks, 'Source (A)', 'Target (C)', 'Aux (B)', total_moves)
        
        print(f"\n Completed in {total_moves[0]} moves.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    run_simulation()
