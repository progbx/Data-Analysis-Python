def swap_list_elements(a):
    b = a[:]
    for i in range(0, len(a), 2):
        b[i], b[i+1] = b[i+1], b[i]
    return b