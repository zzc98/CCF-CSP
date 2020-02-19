def main():
    n = int(input())
    string = input().split()
    price = [int(s) for s in string]
    ans = []
    t0 = (price[0]+price[1])//2
    ans.append(t0)
    if n == 2:
        ans.append(t0)
        return ans
    for i in range(1, n-1):
        t = (price[i-1]+price[i]+price[i+1])//3
        ans.append(t)
    t1 = (price[-2]+price[-1])//2
    ans.append(t1)
    return ans


if __name__ == "__main__":
   ans =  main()
   for i in ans:
       print(i, end=' ')
