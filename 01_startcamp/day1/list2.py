team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]
t1 = list(team[2:4])
print(t1, type(t1))
t2 = list(team[2:3])
print(t2, type(t2))

new_member = ['js', 10]
team = team + new_member
print(team)

nums = [1,2,3,4]
print(nums)
nums += [5]
print(nums)

del(team[2:4])
print(team)

del(nums[2])
print(nums)