import argparse


def leetspeak(input_string: str, model: int):
    # 定义替换规则，可以根据需要自定义
    rules = [('A', '4'), ('B', '8'), ('C', '['), ('E', '3'), ('I', '|'), ('J', ']'),
             ('O', 'o'), ('S', '$'), ('T', '7'), ('Z', '2'), ('o', '0'), ('l', '1'),
             ('t', '+'), ('s', '5'), ('a', '@'), ('b', '6'), ('g', '9')]
    if model == 0:
        for rule in rules:
            input_string = input_string.replace(rule[0], rule[1])
    elif model == 1:
        for rule in rules:
            input_string = input_string.replace(rule[1], rule[0])
    return input_string
def help():
    print("Usage: leetspeak.py [-h | --help] [-m | --mode] [-i | --input]")
    print("eg: leetspeak.exe -m 0 -i 'leetspeak Applet' ")
    print("  -h, --help          Displays this help message")
    print("  -m, --mode        Selects mode 0 or 1 ; 0-encryption 1-decrypt")
    print("  -i, --input             Optional input text")


def main():
    parser = argparse.ArgumentParser(description="LeetSpeak Program")
    parser.add_argument("-m", "--mode", help="Selects mode 0 or 1")
    parser.add_argument("-i","--input", type=str, help="Input text")

    args = parser.parse_args()

    if args.mode is None or args.input is None:
        help()
    else:
        if int(args.mode) == 0:
            if args.input:
                a = leetspeak(args.input, 0)
                print(a)
            else:
                print("Error: No input text provided.")
        elif int(args.mode) == 1:
            if args.input:
                a = leetspeak(args.input, 1)
                print(a)
            else:
                print("Error: No input text provided.")
        else:
            # 显示帮助文档
            help()


if __name__ == "__main__":
    main()


# a = input("亲，请输入编译/转义的字符串：")
# b = int(input("亲，请选择编译/转义的模式，0-编译，1-转义:"))
# print(leetspeak(a,b))

