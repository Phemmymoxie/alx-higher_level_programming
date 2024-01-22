#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list)

    if idx < 0:
        return my_list
    if idx > list_len:
        return my_list
    my_list[idx] = element
    return my_list


# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     new_element = 9
#     new_list = replace_in_list(my_list, idx, new_element)
#     print(new_list)
#     print(my_list)
