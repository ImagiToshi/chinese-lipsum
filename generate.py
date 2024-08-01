import random

def Lipsum(length, gen_punc, punc_min_gap, punc_max_gap):
    lipsum_list = []
    for _ in range(length):
        character = random.randint(0x4e00, 0x9fa5)
        lipsum_list.append(chr(character))

    if gen_punc:
        i = 0
        lipsum_list_new = []
        while i < len(lipsum_list):
            gap = random.randint(punc_min_gap, punc_max_gap)
            lipsum_list_new.extend(lipsum_list[i:i + gap])
            i += gap
            
            if i < len(lipsum_list):
                punc = random.choice('，。？！') # 随机选择一个标点符号插入
                lipsum_list_new.append(punc)
        
        lipsum_list_new.append('。') # 结尾添加一个句号，这样更好看（？
        
    else:
        lipsum_list_new = lipsum_list

    lipsum_str = ''.join(lipsum_list_new)
    return lipsum_str