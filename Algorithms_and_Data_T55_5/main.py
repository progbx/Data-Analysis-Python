def pendulum_generator(sequence):
    """Iterates infinitely over the sequence back and forth."""
    while True:
        for item in sequence:
            yield item
        for item in reversed(sequence[1:-1]):  # Exclude first and last elements when reversing
            yield item
