s = "01#张三#20-02#李四#30-03#王五#40-04#赵六#50-05#老王#60-06#老李#70"
items = s.split('-')
total = 0
count = 0
for item in items:
    parts = item.split('#')
    num = parts[0]
    name = parts[1]
    score = int(parts[2])
    print(f"{num} {name} {score}")
    total += score
    count += 1
avg = total / count
print(f"平均分: {avg:.2f}")