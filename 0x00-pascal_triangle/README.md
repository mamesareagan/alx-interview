## To create a function pascal_triangle(n) that returns a list of lists of integers representing Pascal’s triangle of n, we can use a nested loop to construct the triangle.

**Here's the implementation of the pascal_triangle function:**

``` def pascal_triangle(n):
        if n <= 0:
            return []

        triangle = [[1]]
        for i in range(1, n):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)
            triangle.append(new_row)

        return triangle
```
**The function first checks if n is less than or equal to 0 and returns an empty list in that case.**

For n greater than 0, the function starts with the first row [1] and then iterates from 1 to n - 1 to construct subsequent rows. The new row is built using the elements of the previous row, summing up adjacent elements to get the elements of the new row.

Finally, the function returns the completed triangle containing all rows of Pascal's triangle.

## Now, when you run the provided test script:


```pascal_triangle = __import__('0-pascal_triangle').            pascal_triangle

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    if __name__ == "__main__":
        print_triangle(pascal_triangle(5))
```

**output**
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
