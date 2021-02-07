import time as t
print('{:=^20}'.format('程序开始'))
for i in range(101):
    print('\r{:3}%'.format(i),end='')
    t.sleep(0.1)
print('\n')
print('程序结束'.center(20,'='))
