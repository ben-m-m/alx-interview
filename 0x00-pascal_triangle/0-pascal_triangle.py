#!/usr/bin/python3


def pascal_triangle(n):
    # Check for invalid input
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        # Calculate the next row based on the previous row
        prev_row = triangle[-1]
        next_row = [1]  # The first element is always 1

        for j in range(1, i):
            next_element = prev_row[j - 1] + prev_row[j]
            next_row.append(next_element)

        next_row.append(1)  # The last element is always 1
        triangle.append(next_row)

    return triangle

# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)

