# def test_func(compute):
#     result = compute(1, 2)
#     print(f"compute的类型是：{type(compute)}")
#     print(f"计算结果为：{result}")
#
# def compute(x, y):
#     return x + y
#
# test_func(compute)

def test_func(compute):
    result = compute(1, 2)
    print(f"计算结果为：{result}")

test_func(lambda x, y : x * y)

