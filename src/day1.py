with open('src/input/day1_input.txt', 'r') as file:
    lines = file.readlines()

left = []
right = []

for line in lines:
    sp = line.split('   ')
    left.append(int(sp[0]))
    right.append(int(sp[1]))

left.sort()
right.sort()

difference = 0

for i in range(len(left)):
    difference += abs(left[i] - right[i])

print(difference)
# Output: 1834060 ✅