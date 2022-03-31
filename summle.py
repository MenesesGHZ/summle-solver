operation = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "/": lambda a,b: a/b,
    "*": lambda a,b: a*b
}

def summle_solver(target: int, nums: list, solution_chain: str = "\n" , iteration = 0, max_iteration = 5):
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

                new_num = operation[operator](a, b)
                if new_num <= 0 or isinstance(new_num, float):
                    continue

                possible_solution_chain = f"{iteration}. {a}{operator}{b} = {new_num}\n"
                possible_solution_chain = solution_chain + possible_solution_chain

                if target - new_num == 0:
                    return (True, possible_solution_chain)
                
                new_nums = nums.copy()
                new_nums.remove(a)
                new_nums.remove(b)
                new_nums.insert(0, new_num)
                
                result = summle_solver(
                    target=target,
                    nums=new_nums,
                    solution_chain=possible_solution_chain,
                    iteration=iteration+1,
                    max_iteration=max_iteration
                )
                if result[0]:
                    return result
    return (False, None)



def interface(target: int, nums: list):
    # Maybe not the best optimal solution
    solution_chain = summle_solver(
        target=target,
        nums=nums,
    )
    print("\nSolution: ", solution_chain[1], sep="")





    if not solution_chain[0]:
        exit(0)

    # Searching for best optimal solution
    for i in range(1, 6):
        solution_chain = summle_solver(
            target=target,
            nums=nums,
            max_iteration=i
        )
        if solution_chain[0]:
            print("Best solution: ", solution_chain[1], sep="")
            break