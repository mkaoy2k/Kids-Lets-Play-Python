""" 呼叫輸入函式 input(<提示字串>)，
Python 能印出一段提示字串，
然後等使用者輸入資訊，
按 enter 鍵後，
Python 再返回程式生成字串物件。
"""
greeting = '哈囉'

# 從鍵盤輸入，呼叫 input(<提示字串>)函式
name = input("請問你的名字叫: ")
if name == '':
    # 空白的話，用預設值
    name = '尤勇'   

# 螢幕上輸出
# 用法1：字串物件的 'format' 方法
print("用字串物件的 'format' 方法...")
message1 = '{}, {}. 歡迎!'.format(greeting, name)
print(message1)
print()

# 用法2： Python 版本3以後才有的 'f-字串指令')
print("用 Python 版本3以後才有的 'f-字串指令'...")
message2 = f'{greeting}, {name}. 歡迎!'
print(message2)