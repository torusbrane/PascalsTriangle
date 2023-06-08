row_count = int(input("Enter a number for the Pascal Triangle: "))

def pascal_triangle():
    global row_count
    start_row_count = 0
    for i in range(row_count):
        first_num = 1
        row_count -= 1
        wht_spc = str(' ' * row_count)
        start_row_count += 2
        wht_spc2 = str(start_row_count)
        new_start_row = start_row_count - 1
        # wht_spc3 = str(' ' * new_start_row)
        wht_spc4 = str(new_start_row + first_num)
        if i < 1:
            print(wht_spc + str(first_num) + wht_spc2 + str(first_num))
        # else:
        #     print(wht_spc + str(first_num) + wht_spc3 + str(first_num))
        else:
            print(wht_spc + str(first_num) + wht_spc4 + str(first_num))

init_wht_spc = str(' ' * row_count)

print(init_wht_spc + "1")     
pascal_triangle()

#ADDED WHITE SPACE 4 AND USED THAT INSTEAD OF WHITE SPACE 3