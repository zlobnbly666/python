x = 'xxxxxxxx'
def task(x):
    return "YES" if x == x[::-1] else "NO"
print(task(input("> ").replace(" ", "").lower()))
