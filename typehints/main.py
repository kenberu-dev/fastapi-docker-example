def add(num1: int, num2: int) -> str:
    result:str = '足し算結果=>'
    return result + str(num1 + num2)

def greet(name:str)-> str:
    return f"おはよう!{name}!"

def divide(divided: float, divisor: float)-> float:
    return divided / divisor

def process_items(items: list[str])-> None:
    for item in items:
        print(item)
        
def count_characters(word_list: list[str])-> dict[str, int]:
    count_map: dict[str, int] = {}
    for word in word_list:
        count_map[word] = len(word)
    return count_map

resulet_add = add(10, 20)
print(resulet_add)

greeting = greet("タロウ")
print(greeting)

resulet_divide = divide(10.0, 20.0)
print("割り算の結果=>", resulet_divide)

process_items(["リンゴ", "ゴリラ", "ラッパ"])

character_counts = count_characters(["apple", "amazon", "google"])
print("文字に対する文字数は=>", character_counts)