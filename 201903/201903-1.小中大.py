if __name__ == "__main__":
    count = int(input())
    nums = input().split()
    for i in range(count):
        nums[i] = int(nums[i])
    n_min = min(nums)
    n_max = max(nums)
    if count % 2 == 1:
        median = nums[count//2]
    else:
        temp = nums[count//2] + nums[count//2-1]
        if temp % 2 == 1:
            median = temp/2
        else:
            median = temp//2
    print(n_max, median, n_min)
