Overview

The Collatz Conjecture Toolkit is a lightweight Python project for exploring the famous Collatz sequence (also known as the 3n + 1 problem).

It allows you to:

Generate the full Collatz sequence for any positive integer

Compute stopping time and total stopping time

Find the maximum value in the sequence

Display results as text or JSON

(Optionally) visualize the sequence using Matplotlib

The Collatz rule:

If n is even → divide by 2

If n is odd → multiply by 3 and add 1
The conjecture states that this process always eventually reaches 1.

 Features

Generate Collatz sequences for any positive integer

Compute key metrics (length, stopping time, max value)

Optional JSON output for programmatic use

Optional sequence plotting (--plot)

Simple CLI interface + reusable library

Tested and type-annotated
