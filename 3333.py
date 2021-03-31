# def list_mp(array):
#     len_arr = len(array)
#     for i in range(1, len_arr):
#         for j in range(len_arr - i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
#
# test_arr = [1, 4, 2, 6, 3]
# c = list_mp(test_arr)
# print(c)

#
test_arr = [1, 4, 2, 6, 3]
# for i in range(len(test_arr) - 1):
#     for j in range(len(test_arr) - 1 - i):
#         if test_arr[j] > test_arr[j + 1]:
#             test_arr[j], test_arr[j + 1] = test_arr[j + 1], test_arr[j]
#
# print(test_arr)


for i in range(1, len(test_arr)):
    for j in range(len(test_arr) - i):
        if test_arr[j] > test_arr[j + 1]:
            test_arr[j], test_arr[j + 1] = test_arr[j + 1], test_arr[j]

print(test_arr)

arr = [1, 2, 5, 7, 3, 6, 15, 12, 31, 4]


def sort_charru(arr=None):
    if not arr:
        arr = [1, 2, 5, 7, 3, 6, 15, 12, 31, 4]
    for i in range(0, len(arr)):
        # 记录前一个元素的索引
        pre_index = i - 1
        # 记录当前元素的值便于循环进行处理
        current_data = arr[i]
        # 开始循环
        while pre_index >= 0 and current_data < arr[pre_index]:
            # 当前比较的元素调换位置(大的放后面)
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current_data


def sort_xuanze(arr=None):
    if not arr:
        arr = [1, 4, 3, 5, 2]
    # 算法原理
    # 1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    # 2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
    # 3.重复第二步，直到所有元素均排序完毕
    for i in range(0, len(arr) - 1):
        # 初始化最小值索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            # 将两个数字换位置
            arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


arr = [1, 2, 5, 7, 3, 6, 15, 12, 31, 4]

# 插入
# 把一堆无序的数字分为 第一个有序 和其他的无序
# 在其他的无序中去挨个比较，遇到自己比前面的小就换位置
for i in range(len(arr)):
    # 定义前一个索引
    pre_index = i - 1
    current_data = arr[i]
    # 定义当前值
    # 准备循环
    while pre_index >= 0 and current_data < arr[pre_index]:
        # 就把值大的放后面
        arr[pre_index + 1] = arr[pre_index]
        pre_index -= 1
    arr[pre_index + 1] = current_data
print(arr)

# 插入
for i in range(len(arr)):
    # 获取当前值
    current_data = arr[i]
    # 获取前一个值的索引
    pre_index = i - 1
    # 开始进行循环
    while pre_index >= 0 and current_data < arr[pre_index]:
        # 将大的值放在后面
        arr[pre_index + 1] = arr[pre_index]
        pre_index -= 1
    arr[pre_index + 1] = current_data

print(arr)

arr = [1, 2, 5, 7, 3, 6, 15, 12, 31, 4, 100]


