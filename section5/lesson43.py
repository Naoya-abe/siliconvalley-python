# for else文

for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:  # breakで抜けずに最後まで来たら実行される
    print('I ate all')
