#!/uar/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    modified_tuple = ()
    _tuple_a = tuple_a + (0, 0)
    _tuple_b = tuple_b + (0, 0)
    modified_tuple = _tuple_a[0] + _tuple_b[0], _tuple_a[1] + _tuple_b[1]
    return modified_tuple
