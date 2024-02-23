def filter_list(lst):
    filtered_list = []
    for item in lst:
        if not isinstance(item, str):
            filtered_list.append(item)
    return filtered_list