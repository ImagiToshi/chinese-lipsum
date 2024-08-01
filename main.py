import generate as g

# Lipsum(汉字数量, 是否生成标点符号, 标点符号最小间隔（默认5）, 标点符号最大间隔（默认10）)
# print(g.Lipsum(20, True, 3, 7))

input_length = input("文本中汉字个数: ")
if input_length.isdigit():
    length = int(input_length)
else:
    print("格式错误")
    exit()

input_gen_punc = input("是否生成标点符号 (y/N): ")
if input_gen_punc in ["Y", "y"]:
    gen_punc = True

    input_punc_min_gap = input("标点符号间最小间隔: ")
    if input_punc_min_gap.isdigit():
        punc_min_gap = int(input_punc_min_gap)
    else:
        print("格式错误")
        exit()

    input_punc_max_gap = input("标点符号间最大间隔: ")
    if input_punc_max_gap.isdigit():
        if int(input_punc_max_gap) >= punc_min_gap:
            punc_max_gap = int(input_punc_max_gap)
        else:
            print("最大间隔不能小于最小间隔")
            exit()
    else:
        print("格式错误")
        exit()

elif input_gen_punc in ["N", "n", ""]:
    gen_punc = False
    punc_min_gap = 0
    punc_max_gap = 0
else:
    print("格式错误")
    exit()


result = g.Lipsum(length, gen_punc, punc_min_gap, punc_max_gap)
print("生成完毕\n")
print(result)