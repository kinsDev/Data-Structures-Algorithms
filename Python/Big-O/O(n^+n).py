# O(n^2) + O(n) = O(n^2 + n)

def item_list(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)
item_list(10)

# O(n^2) + O(n) = O(n^2 + n) = O(n^2) is the dominant one because the n^2 is the most important one
# for example, if n = 100, n^2 = 10000, n = 100, so the n^2 is the most important one, because it has a bigger impact on the code due to the larger number of operations