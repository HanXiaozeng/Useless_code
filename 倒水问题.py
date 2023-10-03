#han_xiaozeng
def pour(start, end, capacity):
    if start == capacity:
        print("水壶A倒满了！")
        return
    elif end == capacity:
        print("水壶B倒满了！")
        return
    
    if start == 0:
        print("水壶A为空！")
        pour(capacity, end, capacity)
        return
    elif end == 0:
        print("水壶B为空！")
        pour(start, capacity, capacity)
        return
    
    if start > 0 and end < capacity:
        pour(start-1, end+1, capacity)
        return
    elif start < capacity and end > 0:
        pour(start+1, end-1, capacity)
        return
capacity = int(input("请输入最终需要的容量："))
start = int(input("请输入水壶A的初始水量："))
end = int(input("请输入水壶B的初始水量："))
pour(start, end, capacity)