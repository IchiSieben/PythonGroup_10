class MiExcepcion(Exception):
    pass


try:
    d = {'a': 1}
    # haces código peligroso, y deseas
    # levantar una excepción:
    raise MiExcepcion
    # d['b']
    # 1 + 'a'
except NameError as e:
    print('se ha producido una excepcion')
except KeyError:
    print('Estamos ante un KeyError')
except MiExcepcion:
    print('Se ha producido mi excepción')
else:
    print('No hubo ningún problema')
finally:
    print('Terminamos el try')
