length = int(input())
string = input().split()
nums = [int(s) for s in string]
max_area = 0
for i in range(length):
    width = 1
    left, right = i-1, i+1
    while left >= 0:
        if nums[left] >= nums[i]:
            width += 1
            left -= 1
        else:    
            break
    while right < length:
        if nums[right] >= nums[i]:
            width += 1
            right += 1
        else:
            break
    area = width * nums[i]
    max_area = max_area if max_area > area else area
print(max_area)