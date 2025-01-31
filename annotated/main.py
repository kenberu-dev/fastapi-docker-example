from typing import Annotated

def process_value(
    value: Annotated[int, "範囲は0から100まで"]
)-> None:
    if 0 <= value <= 100:
        print(f"受け取った値は範囲内です:{value}")
    else:
        raise ValueError(f"範囲外の値です。受け取った値：{value}")
    
process_value(50)

try:
    process_value(150)
except ValueError as e:
    print(e)