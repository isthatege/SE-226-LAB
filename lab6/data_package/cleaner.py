def remove_duplicates(data_list):
    seen = set()
    result = []
    for item in data_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]
