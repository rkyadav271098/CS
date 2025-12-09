def generate_table_of_7():
    """Generates the multiplication table for 7."""
    table = []
    for i in range(1, 11):
        table.append(f"7 x {i} = {7 * i}")
    return table

def print_table_of_7():
    """Prints the multiplication table for 7."""
    lines = generate_table_of_7()
    for line in lines:
        print(line)

def generate_table_of_10():
    """Generates the multiplication table for 10."""
    table = []
    for i in range(1, 11):
        table.append(f"10 x {i} = {10 * i}")
    return table

def print_table_of_10():
    """Prints the multiplication table for 10."""
    lines = generate_table_of_10()
    for line in lines:
        print(line)

if __name__ == "__main__":
    print("--- Table of 7 ---")
    print_table_of_7()
    print("\n--- Table of 10 ---")
    print_table_of_10()
