
def print_lo1(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lo1(each_item)
        else:
            print(each_item)
