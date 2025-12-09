def generate_table_of_5():
    """Generates the multiplication table for 5."""
    table = []
    for i in range(1, 11):
        table.append(f"5 x {i} = {5 * i}")
    return table

def print_table_of_5():
    """Prints the multiplication table for 5."""
    lines = generate_table_of_5()
    for line in lines:
        print(line)

if __name__ == "__main__":
    print_table_of_5()
