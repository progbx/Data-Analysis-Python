def make_progress_bar(x):
    num_hashes = x // 10
    num_spaces = 10 - num_hashes
    progress_bar = "|" + "#" * num_hashes + " " * num_spaces + "|" + str(x) + "%"
    return progress_bar