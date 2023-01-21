

## Introduction

There are 6 problems involving recursion.

There is a separate test file for each problem.  If you find an error in the test file, please let me know.

You may run all test files with `python -m unittest` (or `python3`, depending on your seupt), or individual test files with lines such as `python -m unittest test_01_squashNested`.

Note that there will be additional tests for grading which I have not shared with you, although I have not deliberately left any tricks hidden.

## Dates

This assignment was published (late) on the night of October 5th.

~~It is due at 11:59pm on the night of Friday October 14th, which is one week and two days.~~

It is due at 11:59pm on the night of Saturday October 15th, which is one week and two days.

## Grading

~~Each problem is worth 1 mark (that is, all 6 problems have equal weight).~~

Each problem is worth 1 mark.  Problem 4, the calculator, is considered a "bonus mark", so the whole assignment is out of 5.

Problems solved without recursion will be worth zero marks.

In general, expect for each problem to be graded either correct (1 mark) or incorrect (0 marks).  Expect partial marks only if I think the error is my fault.

## Solo work

Please remember that this assignment is solo work.  Do not share your work with others, nor use the work of other students, nor get help from others.

However, you may use what you can find on the internet, assuming that it was published before I handed out this assignment.  Remember that if you use more than a line or two from a source you found on the internet, too much citation (in comments or in a separate CREDITS.md file) is safer and better than too little.

## Submitting your work

~~I will release submission instructions soon, which will probably involve git.  I need to do some testing.  Stay tuned.  But I won't add problems or make the problems harder.~~

To submit your work you will need to

* create a new repo via Github Classroom
    * The link is https://classroom.github.com/a/ffYyj5j_ (yes, including that last underscore, dammit).
* click through some stuff until you see the repository made just for you
    * the URL will start with 
* modify the `solution.py` file
* modify the `studentid.txt` file, doing ONE of the following two things:
    * a) put your A00 number in that file, so that I can associate your github work with your D2L account
        * note that this would mean sending PII to a US company, so instead you may do (b) if you prefer
    * b) write the word "EMAIL" in that file, and then send me an email at my BCIT email address
        * the email should have this in the subject line:   [D2L/GITHUB LINK]
        * the body of the email should contain your name as seen in D2L, your A00* student number, and your github account name
            * in the past I have received wrong github account names.  you can get it right!
    * the file should have exactly one line it in when you submit
* as many times as necessary, `git commit` and `git push`

You can check the auto-grading status in the repo it creates for you.  See more in the video I added to the Resources section of the D2L course website.


## Notes / Hints

### Problems 1 and 2

I don't know what to say to simplify these.  They are about recursively processing nested lists.

### Problem 3

Surprise, it's binary search.

You may slice, and personally I think this way is slightly easier.

Alternately, you can just use indices, which is overall probably harder, but it does avoid one tricky catch that happens with the slicing.

### Problem 4

THIS QUESTION IS NOW A BONUS QUESTION.

This is a parsing problem.  In one way it's a bit harder than the one I did in class, and in another way it's a bit easier.

I supplied a bunch of the support code, to let you focus on the difficult part.

Note that, when you raise SyntaxErrors, my tests do not check what message you give, so I guess you could leave the message blank, but you might want to just write a half-decent message in there just for yourself.  If you haven't previously raised your own exceptions, there's an example in the provided stub code.

This is probably the problem with the longest code required.

### Problem 5

In this problem, you must find a combination of weights that adds up to a target.

One catch is that, in many cases, there might be more than one valid combination, but you must give a particular one of the combinations.  See the examples.

Here's a very straightforward hint: in my solution, there are two base cases (one success, one fail), and both are tested in the testing file.

Here is a more complicated hint, that I hope helps:  For each weight in the list of `weights`, there are two possible paths that could work out: either use the weight, or don't use it.  So that's two recursive calls!  (But there's no point in using a weight if it's too heavy to meet the target!)

Also, I think it's easier if you always let the better weights go first, so that as soon as you find a solution, it's automatically the correct one.  But you don't have to do it that way.

Fun fact, in terms of asymptotic complexit analysis, this problem has a very bad running time.  Don't let it bother you, we'll just run it for small inputs!

### Problem 6

This is a harder version of Problem 5.  What's harder is that the number of possible recursive calls is now variable.  You will not be able to hard-code the recursive calls, which is scary and weird.

Again, in terms of big-Oh running time, the solution to the problem is pretty bad.  Again, we'll just keep to running it for small inputs (say less than 10 weights).
