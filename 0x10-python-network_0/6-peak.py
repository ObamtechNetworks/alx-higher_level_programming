#!/usr/bin/python3
"""finds the peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """finds the peak in a list of unsorted integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1] and \
                list_of_integers[mid] > list_of_integers[mid - 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return list_of_integers[left]
