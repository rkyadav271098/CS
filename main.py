def generate_table_of_3():
    lines = ["Multiplication Table of 3:"]
    for i in range(1, 11):
        lines.append(f"3 x {i} = {3 * i}")
    return lines

def print_table_of_3():
    lines = generate_table_of_3()
    for line in lines:
        print(line)

if __name__ == "__main__":
    print_table_of_3()
