def gaps(values, tolerance=3):
    print('gaps')
    first, rest = values[0], values[1:]
    pairs = []
    a, b = None, None
    last = first
    # Mark indexes where values change
    for i, v in enumerate(rest, 1):
        if (not v == last):
            pairs.append(i)
        last = v

    # return zip(pairs[::2], pairs[1::2])
    # Tolerate gaps
    if not(len(pairs) > 2):
        return zip(pairs[::2], pairs[1::2])
    prev, val = pairs[0], None
    result = [prev]
    skip = False
    for prev, val in zip(pairs[1::1], pairs[2::1]):
        if skip:
            skip = False
            continue
        if abs(prev - val) < tolerance:
            skip = True
            continue
        result.append(prev)
    result.append(val)

    print(pairs[:10])
    print(result[:10])
    return zip(result[::2], result[1::2])

