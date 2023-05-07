def has_more(orig_list: list) -> bool:
    if len(orig_list) > 1:
        return True
    if len(orig_list) == 1:
        return orig_list[0] != '\n'
    return False
