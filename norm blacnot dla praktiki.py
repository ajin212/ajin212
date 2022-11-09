a, b, c = map(int, input().split())
x = "до" if a or b or c == 1 else ""
e = "ре" if a or b or c == 2 else ""
print(x + e)