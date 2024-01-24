# 0x03. Log Parsing

`Algorithm` `Python`
 ```By: Alexa Orrico, Software Engineer at Holberton School```
 ```Weight: 1```
 ```Project will start Aug 14, 2023 6:00 AM, must end by Aug 18, 2023 6:00 AM```
 ```Checker was released at Aug 15, 2023 6:00 AM```
 ```An auto review will be launched at the deadline```

```
   Requirements
   General
-   Allowed editors: vi, vim, emacs
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly #!/usr/bin/python3
-   A README.md file, at the root of the folder of the project, is mandatory
-   Your code should use the PEP 8 style (version 1.7.x)
-   All your files must be executable
-   The length of your files will be tested using wc
```

## Tasks

```0. Log parsing                                                                  mandatory
Write a script that reads `stdin` line by line and computes metrics:

    - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)
    - After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
        + Total file size: `File size: <total size>`
        + where `<total size>` is the sum of all previous `<file size>` (see input format above)
        + Number of lines by status code:
            - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
            - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
            - format: `<status code>: <number>`
            - status codes should be printed in ascending order
*Warning:* In this sample, you will have random value - it’s normal to not have the same output as this one.
```

**Imports and Function Definition:**

- The code begins with importing the `sys` module, which provides access to system-specific parameters and functions.
- The print_stats function is defined, which takes two arguments: `file_size` and `status_codes`.
- This function is responsible for printing the statistics in a formatted manner.

**Main Execution:**

- The code enters the main execution block using `if __name__ == "__main__":`.

**Initializing Variables:**

- `status_codes` is a dictionary that will hold the counts of various status codes, initialized with zeros for each status code.
- `file_size` is initialized to keep track of the total file size.
- `count` is initialized to track the number of lines processed.

**Parsing Input:**

- The code enters a `try` block to handle reading input lines from the standard input (stdin).
- Inside a `for` loop, the code iterates through each line from the input.

**Updating Counts:**

- For each line, the `count` is incremented.
- The line is split into individual words using `data = line.split()`.
- The last element of `data` represents the file size, which is converted to an integer and added to `file_size`.
- The second-to-last element of `data` represents the status code, which is checked against the `status_codes` dictionary.
- If the status code is found in the dictionary, the count for that status code is incremented.

**Printing Stats:**

- After processing every 10 lines (`if count % 10 == 0:`), the `print_stats` function is called to print the accumulated statistics.
- The `file_size` and `status_codes` are passed as arguments to this function, and it prints the total file size and status code counts.
- The status codes are printed in ascending order using the `sorted` function.
- Only status codes with non-zero counts are printed.

**KeyboardInterrupt Handling:**

- The code is prepared to handle a keyboard interruption (Ctrl+C) using a `try-except` block for `KeyboardInterrupt`.
- If a keyboard interruption occurs, the code calls the `print_stats` function to print the current statistics and then raises the same exception to terminate the script.

**Final Statistics:**

- Finally, outside the loop, the `print_stats` function is called again to print the final statistics, including the accumulated file size and status code counts.

**Summary:**

- The code reads lines from the standard input, accumulates file sizes, and counts status codes while also printing statistics every 10 lines.
- If a keyboard interruption occurs, the script gracefully prints the accumulated statistics before terminating.
- It's a handy script for analyzing log files and summarizing important metrics.
