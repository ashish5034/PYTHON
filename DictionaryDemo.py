batches = {"PPA": 18500, "Python":18700,"LB":19000,"Angular":19200,"LSP":18200,"C#":21000}

print(batches)

print(type(batches))

print(len(batches))

print(batches["Python"])

for value in batches:
    print(value)
    
for value in batches:
    print(batches[value])
    
for value in batches:
    print(value,batches[value])