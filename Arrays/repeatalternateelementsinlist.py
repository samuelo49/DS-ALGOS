"""
Python – Repeat Alternate Elements in list
test_list = [4, 5, 6]
K = 3
"""
def repeatAlternateElements(lst, k):
    return [ele for idx, ele in enumerate(lst) for i in range(k) if idx % 2 == 0]
test_list = [4, 5, 6]
K = 3
print(repeatAlternateElements(test_list,k=K))