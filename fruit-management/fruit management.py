name = []
price = []
    
def first():
    print('Write down the fruit name:')
    x = input()
    print('Write down the price:')
    y = int(input())
    
    name.append(x)
    price.append(y)
    
def second():
    print(name)
    print(price)
    
def third():
    print('Write down the fruit name to remove:')
    x = input()
    idx = name.index(x)
    if x in name:
        name.remove(x)
        del price[idx]
    
def forth():
    print('Write down the replace price:')
    x = input()
    y = int(input())
    idx = name.index(x)
    price[idx]=y

while True:
    print('Choose the menu:')
    func = int(input())
    if func == 1:
        first()
    elif func == 2:
        second()
    elif func == 3:
        third()
    elif func == 4:
        forth()
    elif func == 5:
        break

