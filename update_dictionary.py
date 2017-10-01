def update_dictionary(d, key, value):
    if key not in d:
        if 2*key not in d:
            d[2*key] = [value]
        else:
            d[2*key] += [value]
    else:
        d[key] += [value]

d = {0:[1]}
print(update_dictionary(d, 1, -1))  # None
                         # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)
update_dictionary(d, 0, 5)
print(d)