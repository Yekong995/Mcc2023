def min_steps_to_target(init, target, numbers: list):
    if init >= target:
        return 0

    numbers.sort(reverse=True)
    steps = 0

    while init <= target:
        # print(numbers)
        if init == target:
            return steps
        for i in range(len(numbers)):
            if numbers[i] < init:
                init += numbers[i]
                steps += 1
                numbers.remove(numbers[i])
                break
        else:
            return -1

    return steps

# 2
# 5 3 10
# 4 3 4 1 2
# 3 20 100
# 70 86 19
output = []
k = int(input())
for i in range(k):
    # 输入
    n, initial, target = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    if (sum(nums) + initial) < target:
        output.append(-1)
        continue
    elif (sum(nums) + initial) == target:
        output.append(len(nums))
        continue

    # 计算并输出最少次数
    result = min_steps_to_target(initial, target, nums)
    output.append(result)

print("\n".join(map(str, output)))

# # 输入
# n, initial, target = map(int, input().split(" "))
# nums = list(map(int, input().split(" ")))

# # 计算并输出最少次数
# result = min_steps_to_target(initial, target, nums)
# print(result)
