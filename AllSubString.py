def all_subsets(string):
    subsets = []
    set_size = len(string)
    total_subsets = 1 << set_size  # 2^set_size

    for i in range(total_subsets):
        subset = []
        for j in range(set_size):
            if (i & (1 << j)) > 0:
                subset.append(string[j])
        subsets.append(subset)

    return subsets

set = str(input("Enter string : "))
result = all_subsets(set)
for subset in result:
    print(''.join(subset))