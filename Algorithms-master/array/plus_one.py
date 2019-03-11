# Given a non-negative number represented as an array of digits,
# plus one to the number.

# The digits are stored such that the most significant
# digit is at the head of the list.


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        sum = 0
        if i >= 0:
            sum += digits[i]
        if ten:
            sum += 1
        res.append(sum % 10)
        ten = sum / 10
        i -= 1
    return res[::-1]


def plus_one(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


def plus_1(num_arr):
    for idx, digit in reversed(list(enumerate(num_arr))):
        num_arr[idx] = (num_arr[idx] + 1) % 10
        if num_arr[idx]:
            return num_arr
    return [1] + num_arr
