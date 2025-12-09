def generate_table_of_10():
    """Generates the multiplication table for 10."""
    table = []
    for i in range(1, 11):
        table.append(f"10 x {i} = {10 * i}")
    return table

def print_table_of_10():
    """Prints the multiplication table for 10."""
    lines = generate_table_of_10()
    print("\n--- Table of 10 ---")
    for line in lines:
        print(line)

if __name__ == "__main__":
    print_table_of_10()