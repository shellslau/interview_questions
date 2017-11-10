"""
I was supposed to write code that would find the rectangle within a given square that would give the largest sum
I tried making it look at the whole rectangle and subtracting the side that was the most negative until all sides
gave a positive sum/impact to the sum.
This did not work properly and idk what is wrong. Could be that the inside of the rectangle was the problem? but
idk how to fix that and I ran out of time.
"""
a = int(raw_input())
city = []
for i in range(0, a):
    city.append(raw_input().split())

def find_max_num(city):
    max_num = -101
    for i in range(len(city)):
        line = city[i]
        for j in range(len(line)):
            dist = line[j]
            if dist > max_num:
                max_num = dist
                coord = (i,j)
    return max_num, cooord

def find_sum_across(line):
    sum = 0
    for dist in line:
        sum += int(dist)
    return sum

def find_sum_down(grid, side):
    sum = 0
    if side == "front":
        for dist in range(len(grid) - 1):
            sum += int(grid[dist][0])
    elif side == "back":
        for dist in range(len(grid) - 1):
            sum += int(grid[dist][len(grid[dist]) - 1])
    return sum

def find_max_rect(city):
    grid = city
    bottom = find_sum_across(grid[len(grid) - 1])
    top = find_sum_across(grid[0])
    front = find_sum_down(grid, "front")
    back = find_sum_down(grid, "back")
    while (bottom < 0) or (top < 0) or (front < 0) or (back < 0):
        minimum = min(bottom, top, front, back)
        if minimum == bottom:
            grid = grid[:len(grid) - 1]
            bottom = find_sum_across(grid[len(grid) - 1])
        elif minimum == top:
            grid = grid[1:]
            top = find_sum_across(grid[0])
        elif minimum == front:
            for i in range(len(grid) - 1):
                grid[i] = grid[i][1:]
            front = find_sum_down(grid, "front")
        elif minimum == back:
            for i in range(len(grid) - 1):
                grid[i] = grid[i][:len(grid) - 1]
            back = find_sum_down(grid, "back")
        else:
            print "error"
            return
    return grid
    
grid = find_max_rect(city)
max_sum = 0
for line in grid:
    max_sum += find_sum_across(line)
print max_sum
