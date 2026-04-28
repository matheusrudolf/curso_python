# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
