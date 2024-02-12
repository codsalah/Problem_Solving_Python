if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
list_ = []
for i in arr:
    list_.append(i)
    list_.sort()
    new_list = list(set(list_))    
    
print(new_list[-2])