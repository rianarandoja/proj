

def parseInput(raw_input, l_delim, r_delim):
    """
    Divides raw_input into lists representing strings given inside and outside of l_delim to r_delim.
    If raw_input contains delimiters, returns 2-tuple of lists where first component is a list
      of strings between l_delim and r_delim and second component is a list of strings not between
      the delimiters.
    If raw_input contains no delimiters and is non-empty, returns 2-tuple of lists where first component
      is a list containing raw_input as its only element and second component is an empty list.
    If raw_input is empty, returns None.
    If there is an unequal number of l_delim and r_delim, returns -1.
    :param l_delim: string, left-side delimiter
    :param r_delim: string, right-side delimiter
    :param raw_input: string
    :return: 2-tuple of lists or None
    """
    in_delim_list = []
    out_delim_list = []

    l_delim_count = raw_input.count(l_delim)
    r_delim_count = raw_input.count(r_delim)

    if not raw_input:
        # If raw_input is empty
        return None
    elif l_delim_count != r_delim_count:
        # If the number of l_delim characters and r_delim characters is not the same.
        return -1
    elif not l_delim_count:
        # if there are no delimiters, ensures that first list of 2-tuple is non-empty.
        return ([raw_input], [])

    caret_pos = -1
    l_delim_pos = 0
    r_delim_pos = -1
    for char in raw_input:
        caret_pos += 1
        if char == l_delim:
            out_delim_list.append(raw_input[r_delim_pos+1 : caret_pos])
            l_delim_pos = caret_pos
        elif char == r_delim:
            r_delim_pos = caret_pos
            in_delim_list.append(raw_input[l_delim_pos+1 : r_delim_pos])

    if r_delim_pos != caret_pos:
        out_delim_list.append(raw_input[r_delim_pos+1 : caret_pos+1])

    return (in_delim_list, out_delim_list)
