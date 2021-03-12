def capitalizing(row):
    new_list = row.split(".")
    result = ""
    for i in range(len(new_list)):
        new_list[i] = new_list[i].strip().lower()
        if len(new_list[i]) > 1:
            sentence = new_list[i][0].upper() + new_list[i][1:] + ". "
            result += sentence
        elif len(new_list[i]) == 1:
            sentence = new_list[i][0].upper() + ". "
            result += sentence
        else:
            continue

    return result
