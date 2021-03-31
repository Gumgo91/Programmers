def calc(numbers, target, index, sum):
    if index == len(numbers)-1:
        return ((sum+numbers[index])==target)*1 + ((sum-numbers[index])==target)*1
    else:
        return calc(numbers, target, index+1, sum+numbers[index]) + calc(numbers, target, index+1, sum-numbers[index])

def solution(numbers, target):
    answer = calc(numbers, target, 0, 0)
    return answer