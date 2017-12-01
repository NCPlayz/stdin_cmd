def make_number(string):
    """Attempts to make an str into a float or int."""
    try:
        return float(string)
    except ValueError:
        return int(string)
