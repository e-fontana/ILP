reads, max_capacity = map(int, input().split())
has_over_capacity = 'N'
people_inside = 0
for x in range(reads):
    entered, exited = map(int, input().split())
    people_inside += exited - entered
    if people_inside > max_capacity:
        has_over_capacity = 'S'
print(has_over_capacity)