
This file contains a list of errors.  I believe I have fixed all of these problems in the current version of the assignment, but the original assignment screwed these things up.



## makeWeightMulti vs makeWeightMany

The solution.py names the function for #6 as `makeWeightMany`, but the tests call it `makeWeightMulti`.  Let's go with `makeWeightMulti`.  So you will need to rename your function, including the recursive calls.  My apologies.


## binarySearch : error in the doctest

There was an error in the doctest for `binarySearch`, there was an `8` where there should have been a `9`.


## calculator : total clarification

#### grading change

For the reasons listed below, I have decided to make the calculator a bonus question.  So now this assignment is out of 5.


#### documentation was missing

Apparently I missed publishing a big chunk of the explanation I wrote for this question.  I had a long explanation in my README, but I moved it to the solution.py, but apparently that version of the solution.py is not what I published.  My bad.  Solution.py has been updated with much more detail.


#### multi-digit clarification

One particular aspect which has been brought to my attention: your solution to #4 calculator should NOT handle multi-digit numbers, although it should handle 0.

For example, this input, although it looks good to us humans, should result in a `SyntaxError`:

```python
calculator("(55 + 5)")
```

I will not deliberately test for this either way, so you can probably get away with either, but single-digits-only is what you should do.


#### division clarification

Also, I want to explicitly highlight something that was already implicit in `do_operator`, but was probably not clear enough.  As I've now spelled out, let `/` act like Python's `//` operator.  I've added a doctest and a unittest to make this more explicit.

