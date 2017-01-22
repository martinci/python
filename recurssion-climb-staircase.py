#climb_staircase takes 1 parameter:
#   size: int denoting the number of steps in the staircase.
# Return --> total number of ways to climb the stairs.
def climb_staircase(size):
    global memory
    if size not in memory:
        # recursively compute the options
        ## we can choose to take 1, 2 or 3 steps and
        ## face the same problem with smaller size.
        memory[size] = climb_staircase(size-1) + climb_staircase(size-2) + climb_staircase(size-3)
    return memory[size]
    
    
if __name__ == '__main__':
    #input from console
    ##total number of staircases
    s = int(input())
    memory = {0:0, 1:1, 2:2, 3:4}
    for _ in range(s):
        #size of each staircase
        size = int(input())
        print(climb_staircase(size))
