### Created by Ben Collingridge.

# What is Collatz Conjecture?
>Collatz Conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1.  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture] - Wikipedia article_

## What are the two simple arithmetic operations?
- If positive integer _n_ is even, do _n / 2_.
- If positive integer _n_ is odd, do _3n + 1_.
> With enough repetition, do all positive integers converge to 1?  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture]_

## Some basic history.
- Named after the mathematician Lothar Collatz.
- Introduced the idea in 1937, two years after receiving his doctorate.
> The sequence of numbers is sometimes referred to as the hailstone sequence, hailstone numbers, or hailstone numerals (because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers.  

_From [https://en.wikipedia.org/wiki/Collatz_conjecture]_

# How do I run the program?
- Install **matplotlib** if not already installed. This can be done (but not limited to) using:
> pip install matplotlib  

**OR**  

> py -m pip install matplotlib  

- Choose the plot mode.
  - Set _mode_ to "d" to run the program for a definite amount of steps (default is 200).
  - Set mode to "i" to run the program until _n_ converges to 1 (indefinite).
  - Set mode to "b" to plot both definite and indefinite modes starting at the same number.
- Choose the starting number (defined by _start_) for _n_.
  - By default, this is a random positive integer between 1 and 100, although this can be set to a definite positive integer, or the maximum random value can be increased or decreased.
- Choose the number of definite steps (_definite_steps_) if you are running in mode "d" or "b".
  - As mentioned previously, this is defaulted to 200 steps.