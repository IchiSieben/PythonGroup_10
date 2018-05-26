class CuentaCorriente:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad < 0:
            print('No puedes depositar cantidades negativas')
            return
        self.saldo += cantidad

    def transferir(self, cuenta, cantidad):
        if cantidad > self.saldo:
            print('Fondos insuficientes')
            return

        self.saldo -= cantidad
        cuenta.depositar(cantidad)


keiko = CuentaCorriente(32847)
print(keiko.saldo) # 32847
keiko.depositar(10)
print(keiko.saldo) # 32857

AG = CuentaCorriente(100)
AG.transferir(keiko, 20)
print(AG.saldo) # disminuido
print(keiko.saldo) # aumentado
