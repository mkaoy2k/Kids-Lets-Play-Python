# 打招呼函式

def input_name(name=None):
    """ 呼叫輸入函式 input(<提示字串>)，
    Python 能印出一段提示字串，然後等使用者輸入資訊，按 enter 鍵後，返回名字字串。

    用法：
        input_name('<你的名字>')

    1. <你的名字>忽略時，會要求輸入。
    2. 輸入空白時，預設值是'尤勇'
    """

    if name == None:
        # <你的名字>忽略時，呼叫 input(<提示字串>)函式
        name = input("請問你的名字叫: ")
    else:
        if name == '':
            name = '尤勇'   # 輸入空白時，用預設值
    return name


def print_hello1(name,
                 greeting='哈囉',
                 welcome='歡迎'
                 ):
    """
    以字串物件的 'format' 方法列印

    用法：
        print_hello1(greeting, name)
    """
    message1 = '{}, {}. {}!'.format(
        greeting,
        name,
        welcome)
    print(message1)


def print_hello2(name,
                 greeting='哈囉',
                 welcome='歡迎'
                 ):
    """
    Python 版本3以後才有的以'f-字串指令'列印

    用法：
        print_hello2(greeting, name)
    """
    message2 = f'{greeting}, {name}. {welcome}!'
    print(message2)

if __name__ == '__main__':
    print(input_name())
    print(input_name(name=''))
    print(input_name(name='Michael'))

    print_hello1(name='Michael 1')
    print_hello2(name='Michael 2')