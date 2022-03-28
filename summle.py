nums = [2, 10, 10, 12, 12, 25]
target = 624
operation = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "/": lambda a,b: a/b,
    "*": lambda a,b: a*b
}
max_iteration = 5

def summle_solver(target: int, nums: list, solution_chain: str = "\n" , iteration = 0):
    if not nums or iteration > max_iteration - 1:
        return (False, None)  

    nums_length = len(nums)
    for i in range(nums_length):
        a = nums[i]
        for j in range(nums_length):
            if i == j:
                continue
            for operator in operation:
                b = nums[j]
                if operator in ["/", "*"] and 0 in [a, b]:
                    continue

                new_num = operation[operator](a, b)
                if new_num < 0 or new_num > target or isinstance(new_num, float):
                    continue

                new_nums = nums.copy()
                new_nums.remove(a)
                new_nums.remove(b)

                possible_solution_chain = f"{iteration}. {a}{operator}{b} = {new_num}\n"
                possible_solution_chain = solution_chain + possible_solution_chain

                if target - new_num == 0:
                    return (True, possible_solution_chain)

                result = summle_solver(
                    target=target,
                    nums=new_nums + [new_num],
                    solution_chain=possible_solution_chain,
                    iteration=iteration+1
                )
                if result[0]:
                    return result
    return (False, None)




for i in range(1, 5):
    max_iteration = i
    solution_chain = summle_solver(
        target=target,
        nums=nums,
    )
    if solution_chain[0]:
        print(solution_chain[1])
        break
