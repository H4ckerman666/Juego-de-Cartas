def tell_me_my_letter(list_huffman):
    checklist = [
        [0,0,0,0,0,0,0],
        [0,0,0,1,1,0,1],
        [0,0,1,0,0,1,1],
        [0,0,1,1,1,1,0],
        [0,1,0,0,1,1,0],
        [0,1,0,1,0,1,1],
        [0,1,1,0,1,0,1],
        [0,1,1,1,0,0,0],
        [1,0,0,0,1,1,1],
        [1,0,0,1,0,1,0],
        [1,0,1,0,1,0,0],
        [1,0,1,1,0,0,1],
        [1,1,0,0,0,0,1],
        [1,1,0,1,1,0,0],
        [1,1,1,0,0,1,0],
        [1,1,1,1,1,1,1]
    ]
    dic_name = {'0':'10C','1':'9C','2':'2C','3':'1C','4':'10P','5':'9P','6':'2P','7':'1P',
                '8':'10R','9':'9R','10':'2R','11':'1R','12':'10T','13':'9T','14':'2T','15':'1T'}
    error_list = []
    error_list_bit = []
    error = 0
    for check in checklist:
        error_bit = []
        for idy,number in enumerate(check):
            if list_huffman[idy] == number:
                continue
            else:
                error += 1
                error_bit.append(idy)
        error_list.append(error)
        error_list_bit.append(tuple(error_bit))
        error_bit.clear()
        error = 0
        
    distancia_minima = min(error_list)
    print(distancia_minima)
    letter_correct = 0
    for i,valor in enumerate(error_list):
        if distancia_minima == valor:
            letter_correct = i
    print(error_list_bit)        
    for x in error_list_bit:
        #print(len(error_list_bit))
        if len(x) == distancia_minima:
            if len(x) == 0 :
                number_bit = 0
            else:
                number_bit = x[0] + 1

    
        
    print("tu carta es ",dic_name[str(letter_correct)])
    return dic_name[str(letter_correct)],number_bit

a,s = tell_me_my_letter([1,1,1,1,0,1,0])