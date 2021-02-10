def my_sum():
    tmp = False
    result_glob = 0
    while tmp == False:
        number = input('Enter numbers or Q(or q) for quit - ').split()
        result2 = 0
        for numb in number:
            if 'Q' or 'q' in numb:
                tmp == True
                break
            result2 = result2 + int(numb)
        result_glob = result_glob + result2
    return result_glob

