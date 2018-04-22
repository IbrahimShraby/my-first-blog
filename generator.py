"""Contains generator functions"""


def take(count, iterable):
    """Take items from front of an Iterable
    Args:
        count: the number of items to be returned.
        iterable: the source of items.
    Returns:
        only the first 'count' items form the Iterable object.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return  # terminate the stream of yielded values
        counter += 1
        yield item


def distinct(iterable):
    """Return unique items by removing duplicts
    Args:
        iterable: the source of items.
    Yields:
        the unique item.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        import pdb
        pdb.set_trace()
        yield item
        seen.add(item)


def run_take():
    """Run the take() generator function,
    since generators are lazy, and produce the next item on demand.
    """
    items = [1, 2, 3, 4, 5, 6]
    for item in take(3, items):
        print(item)


def run_distinct():
    """Execute the distinct() generator function"""
    items = [1, 2, 2, 2, 3, 4, 5, 6, 6]
    import pdb
    pdb.set_trace()
    for item in distinct(items):
        print(item)


def run_pipeline():
    """Run a pipeline of generator function generators."""
    items = [1, 2, 3, 3, 6, 4]
    for item in take(3, list(distinct(items))):
        print(item)


def lucas():
    """Define the lucas series."""
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a+b


"""if __name__ == '__main__':
    run_distinct()"""