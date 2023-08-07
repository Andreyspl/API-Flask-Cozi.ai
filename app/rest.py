# try:
#     a = 1
#     b = 123

#     if (type(a) or type(b)) != int:
#         raise TypeError({"Não pode somar string e int"})

#     print(a + b)

# except Exception as e:
#     print(str(e))
#     # print(int(a) + int(b))


# # raise TypeError(f" unsupported operand type(s) for +: {type(a) and {type(b)}}")


import requests

res = requests.get("http://127.0.0.1:5000/v1/products")
print(res.text)
