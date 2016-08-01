# coding=utf8
import random
import math
color = ["1", "2", "3", "4", "5"]
category = ["dog", "beauty", "building", "dress", "photograph"]


def generate_candidates(num=50):
    sample_arr = []
    for i in range(num):
        color_index = random.randint(0, len(color)-1)
        category_index = random.randint(0, len(category)-1)
        sample_arr.append((color[color_index], category[category_index]))
    for i in range(8):
        sample_arr.append(("3", "dress"))
        sample_arr.append(("4", "dress"))
    return sample_arr


def get_key(item):
    return item[0]


def get_category(item):
    return item[1]


def get_sorted_arrs(elem_arr):
    ordered_one_arr = sorted(elem_arr, key=get_key)
    all_color_arrs = []
    temp_color = None
    same_color_arr = []
    for color_category_pair in ordered_one_arr:
        current_color = get_key(color_category_pair)
        if temp_color != current_color:
            if temp_color and len(same_color_arr) > 0:
                all_color_arrs.append(same_color_arr)
            temp_color = current_color
            same_color_arr = []
        same_color_arr.append(color_category_pair)
    if temp_color and len(same_color_arr) > 0:
        all_color_arrs.append(same_color_arr)
    return all_color_arrs

# def minimize_max_block(elem_list, last_block_num, category_info, threshold=8):
#     list_info = get_category_list(elem_list)


def construct_arr_info(input_arr):
    sort_color_arrs = get_sorted_arrs(input_arr)
    for sort_color_arr in sort_color_arrs:
        category_in_color_arrs = get_category_list(sort_color_arr)
        permute_in_category_list(category_in_color_arrs)


def permute_in_category_list(category_lists, pre_cate=None, pre_num = 0):
    result = []
    cate_index_map, key_list = get_permute_info_in_category_list(category_lists)
    max_average = get_permute_key_split(key_list)
    for key_elem in key_list:
        




def get_permute_key_split(key_list):
    if len(key_list) < 2:
        return key_list
    sum =0
    for i in range(1, len(key_list)):
        sum += key_list[i][1]
    max_average = int(math.ceil(float(key_list[0][1])/(sum+1)))
    return max_average


def get_permute_info_in_category_list(category_lists):
    cate_index_map = {}
    cate_num_items = []
    for index, cate_list in enumerate(category_lists):
        cate = get_category(cate_list[0])
        cate_index_map[cate] = index
        cate_num_items.append((cate, len(cate_list)))
    print cate_index_map
    return cate_index_map, sorted(cate_num_items, key=get_rate)


def get_rate(item):
    return 0 - int(item[1])


def get_category_list(elem_list):
    ordered_list = sorted(elem_list, key=get_category)
    result_arrs = []
    temp_color = None
    same_color_arr = []
    for color_category_pair in ordered_list:
        current_color = get_category(color_category_pair)
        if temp_color != current_color:
            if temp_color and len(same_color_arr) > 0:
                result_arrs.append(same_color_arr)
            temp_color = current_color
            same_color_arr = []
        same_color_arr.append(color_category_pair)
    if temp_color and len(same_color_arr) > 0:
        result_arrs.append(same_color_arr)
    return result_arrs


if __name__ == '__main__':
    arr_elems = generate_candidates()

    construct_arr_info(arr_elems)