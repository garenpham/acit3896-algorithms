# Pham Minh Tan A01215507

# Problem 1: squashNested


def squashNested(val):
    """
    Recursively eliminates nested lists, and always returns a list exactly one layer deep, containing all the elements.

    >>> squashNested(2)
    [2]
    >>> squashNested([2])
    [2]
    >>> squashNested([[2]])
    [2]
    >>> squashNested([[[2]]])
    [2]
    >>> squashNested([[1, 2], 3])
    [1, 2, 3]
    >>> squashNested([[[1, [2]]], 3])
    [1, 2, 3]
    """
    # Return val because there is no list to work on
    if type(val) is not list:
        return [val]
    # Return final value when val becomes a layer deep
    if val == []:
        return val
    # Perform recursion when found element in val is a list
    if isinstance(val[0], list):
        return squashNested(val[0]) + squashNested(val[1:])
    # Perform recursion on next element in the nested list val
    return val[:1] + squashNested(val[1:])


# Problem 2: sumNested


def sumNested(val):
    """
    Recursively finds numbers in nested lists, returning the sum of all the nested numbers.

    >>> sumNested(2)
    2
    >>> sumNested([2])
    2
    >>> sumNested([[2]])
    2
    >>> sumNested([[[2]]])
    2
    >>> sumNested([[1, 2], 3])
    6
    >>> sumNested([[[1, [2]]], 3])
    6
    """
    # Return val because there is no list to work on
    if type(val) is not list:
        return val

    # Initiate output sum
    oSum = 0

    # Loop through elements in list
    for item in val:
        # Perform recursion when element inside val is identified as list
        if isinstance(item, list):
            oSum += sumNested(item)
        else:
            # Add value found inside nested list
            oSum += item
    return oSum


# Problem 3: binarySearch

def performBinarySearch(haystack, needle, lo, hi):
    # Condition to perform
    if hi >= lo:
        # Main index for finding needle
        centre = lo + (hi - lo)//2

        # When find at mid, return index of the found element
        if haystack[centre] == needle:
            return centre

        # Recursively search the left half
        elif haystack[centre] > needle:
            return performBinarySearch(haystack, needle, lo, centre-1)

        # Recursively search the right half
        else:
            return performBinarySearch(haystack, needle, centre + 1, hi)
    # Return None when lo exceeds hi but still cannot find value
    else:
        return None


def binarySearch(haystack, needle):
    """
    Recursively finds the needle in the haystack, using binary search.

    Haystack is a sorted list of numbers.  Needle is a number.

    If the needle found, returns the index of the found element.
    If multiple copies of the needle are found, may return any correct index.
    If the needle is not found, return None.

    >>> binarySearch([5, 7, 9], 5)
    0
    >>> binarySearch([5, 7, 9], 7)
    1
    >>> binarySearch([5, 7, 9], 9)
    2
    >>> binarySearch([5, 7, 9], 3) == None
    True
    """
    # Require low and high value in order to perform recursion binary search
    return performBinarySearch(haystack, needle, 0, len(haystack)-1)


# Problem 4: calculator


def calc_helper(str, start):
    # Here's a hint, this is the parameters for the helper function I wrote to do 90% of the work
    return -1, 0


def do_operator(operator, left, right):
    # There are fancier ways to do this, but I thought this would be nice and simple
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        return left // right
    return None


def calculator(str):
    """
    Recursively parses a valid string as a compound term (see below)

    Returns the arithmetic value of evaluating the expression.

    If the input is not a valid compound term, raise a SyntaxError.

    In the explanation below, the following are valid "digits":  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    In the explanation below, the following are valid "operators": + - * /

    Note that "/" should be interpreted as the integer division operator, "//".  Just so it's all integers.

    A term may contain spaces, which should be ignored.  Other than spaces, a term will be either:
        * a single digit, or
        * a compound term

    A compound term contains exactly 5 parts:
        1. an open parethesis, "("
        2. a term
        3. an operator
        4. a term
        5.  a close parenthesis, ")"

    So here are some valid examples:
        5                       # valid because digit.  would return 5.
        (5 + 5)                 # single compound term containing two digit terms.  would return 10.
        (5 + (1 * (6 - 1)))     # a compound term which contains a compound term which contains a compound term.  would return 10.
        ((1+1)*(1+1))           # compound terms on both sides, and no whitespace because it was optional.  would return 4.

    The following are not valid examples, and should raise SyntaxError:
        5 + 5                   # compound terms must have parentheses
        (5 + 5 + 5)             # compound terms always have one operator (unless they have nested compound terms)
        -5                      # negative numbers can only be made with compound terms like (0 - 5)
        5 5                     # where is the operator?  where are the parentheses?  what is this?  neither 55 nor 10 is correct.

    The following are not your problem
        \t                      # I will not use tabs or other whitespace, only spaces

    >>> calculator("5")
    5
    >>> calculator("(2 + 3)")
    5
    >>> calculator("(17 / 3)")
    5
    >>> calculator("(2 + (6 / 2))")
    5
    >>> calculator("((6 + (2 * (5 - 4))) / 2) ")
    4
    """

    # NOTE: you may change the code here if you wish.  But this is exactly the code from my solution, so it may help.
    str = str.replace(" ", "")
    val, found_len = calc_helper(str, 0)
    if found_len == len(str):
        return val
    else:
        raise SyntaxError(f"leftover data: {str[found_len:]}")


# Problem 5: makeWeight

def calcWeightBasic(target, weights, temp, tracking, start):
    # Only return first solution as a list
    if len(tracking) == 0:
        # Found answer
        if (target == 0):
            # Store answer
            tracking.append(list(temp))
            print(temp)

        # Loop from index start to len(weights) - 1
        for i in range(start, len(weights)):

            # if target does not become negative
            if (target - weights[i]) >= 0:

                # adding potential element which can contribute to target

                temp.append(i)
                # Perform recursion on the next element located at i+1
                calcWeightBasic(target-weights[i], weights, temp,
                                tracking, i+1)

                # removing ineligible element in temp (backtracking)
                temp.remove(i)


def makeWeight(target, weights):
    """
    Recursively calculates a combination of weights that adds up to the target.

    Returns an array showing the count of how many of each weight was used.

    If no solution is possible, return None.

    If more than one solution is possible, it must return the solution that favours the weights earlier in the list of options.

    Each weight may be used once, or not used at all (so the return array is all zeroes and ones).

    This problem is a simplified version of #6.

    >>> makeWeight(5, [2, 3, 4])                # 2 + 3 == 5
    [1, 1, 0]
    >>> makeWeight(7, [2, 3, 4])                # 3 + 4 == 7
    [0, 1, 1]
    >>> makeWeight(5, [1, 2, 3, 4])             # the 1 is first, so it wins, in combination with the 4
    [1, 0, 0, 1]
    >>> makeWeight(5, [2, 3, 4, 1])             # if we rearrange the weights in the list, the 2 and 3 are now earlier, so they win
    [1, 1, 0, 0]
    >>> makeWeight(8, [2, 3, 4]) is None        # no solution without using duplicate weights
    True
    >>> makeWeight(0, [2, 3, 4])                # it's very simple to add up to zero
    [0, 0, 0]
    >>> makeWeight(7, []) is None                     # no weights? no solution!
    True
    """
    # Initiate tracking
    tracking = []
    # Fill output with 0
    output = [0 for i in weights]
    # Need additional value of temp, tracking, start for recursion method
    calcWeightBasic(target, weights, [], tracking, 0)

    if len(tracking) == 0:
        return None

    tracking = squashNested(tracking)

    for idx in tracking:
        output[idx] += 1

    return output


# Problem 6: makeWeightMulti

def calcWeight(target, weights, temp, tracking, start):
    if len(tracking) == 0:
        # Found answer
        if (target == 0):
            # Store answer
            tracking.append(list(temp))
            print(temp)

        # Loop from index start to len(weights) - 1
        for i in range(start, len(weights)):

            # if target does not become negative
            if (target - weights[i]) >= 0:

                # adding potential element which can contribute to target

                temp.append(i)
                # Perform recursion on the next element located at i
                calcWeight(target-weights[i], weights, temp, tracking, i)

                # removing ineligible element from temp (backtracking)
                temp.remove(i)


def makeWeightMulti(target, weights):
    """
    Recursively calculates a combination of weights that adds up to the target.

    Returns an array showing the count of how many of each weight was used.

    If no solution is possible, return None.

    If more than one solution is possible, it must return the solution that favours the weights earlier in the list of weights.

    Each weight may be used any integer number of times (no partial weights, though).

    This problem is a more difficult version of #5.

    >>> makeWeightMulti(5, [2, 3, 4])    # 2 + 3 == 5
    [1, 1, 0]
    >>> makeWeightMulti(7, [4, 3, 2])    # 4 + 3 == 7
    [1, 1, 0]
    >>> makeWeightMulti(7, [2, 3, 4])    # this now solves differently from makeWeight
    [2, 1, 0]
    >>> makeWeightMulti(0, [2, 3, 4])     # it's very simple to add up to zero
    [0, 0, 0]
    >>> makeWeightMulti(7, []) is None   # no weights? no solution!
    True
    >>> makeWeightMulti(8, [2, 3, 4])    # it's now possible to solve this one
    [4, 0, 0]
    >>> makeWeightMulti(8, [4, 3, 2])      # changing the order of the weights might change the result
    [2, 0, 0]
    """
    tracking = []

    output = [0 for i in weights]

    calcWeight(target, weights, [], tracking, 0)

    if len(tracking) == 0:
        return None

    tracking = squashNested(tracking)

    for idx in tracking:
        output[idx] += 1

    return output


if __name__ == "__main__":
    import doctest

    doctest.testmod()
