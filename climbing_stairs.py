#distinct ways to climb to the top. Can climb one or two steps

#keep track of ways to reach goal from end
def climbing_stairs(n):
    one, two = 1, 1  # for last two steps

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp

    return one


print(climbing_stairs(5))

