# -*- coding: utf-8 -*-
# @Author: 滑稽(WuDiHuajiJun)
# b站主页：https://space.bilibili.com/520028744?spm_id_from=333.788.0.0
def unicode_to_str(unicode_str):
    return unicode_str.encode().decode('unicode_escape')


def str_to_unicode(string):
    new_str = ''
    for ch in string:
        if '一' <= ch <= '鿿':
            new_str += hex(ord(ch)).replace('0x', '\\u')
        else:
            print("Error：本转码器无法转码非中文内容")
            input("按下任意键退出")
            exit()
    return new_str


def main():
    print("本工具由滑稽制作")
    number = input("请输入功能序号\n1.加密\n2.解密\n")
    if number == "1":
        print(str_to_unicode(input("请输入加密内容（仅支持中文）：")))
        input("按下任意键退出")
    elif number == "2":
        print(unicode_to_str(input("请输入解密内容：")))
        input("按下任意键退出")
    else:
        print("您没有输入或者输入不正确的功能序号")
        input("按下任意键退出")


if __name__ == '__main__':
    main()
