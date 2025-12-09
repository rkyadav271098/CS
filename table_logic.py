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

if __name__ == "__main__":
    print_table_of_7()
