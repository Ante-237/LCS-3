#!/usr/bin/python3
def num_sort(num, target):
    num.sort()
    if not num:
        return 0
    if target > num[-1]:
        return len(num)
    if target < num[0]:
        return 0
    for i in range(len(num)):
        if num[i] >= target:
