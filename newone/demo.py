def main():
    print('hello')
    print('welcome user')
if __name__=="__main__":
    main()

a=10
def s():
    global a
    a=15
    print('inside',a)
s()
print('out',a)


b=10
print(id(b))
def l():
    b=9
    x=globals()['b']
    print(id(x))
    print('ins',b)
    globals()['b'] = 20
l()
print(b)