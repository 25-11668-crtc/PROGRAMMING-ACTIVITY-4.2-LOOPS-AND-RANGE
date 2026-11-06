num_students=int(input("Students: "))

total=0
highest=float("-inf")

for i in range(1,num_students+1):
	score=int(input(f"Score{i}: "))
	total+=score
	if score>highest:
		highest=score
		
average=total / num_students if num_students > 0 else 0

print(f"Total: {total}  Avg: {average:.2f}")
print(f"Highest: {highest}")