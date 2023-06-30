class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_do_qui = ContaCorrente(15)
print(conta_do_qui)

conta_da_dani = ContaCorrente(1000)
print(conta_da_dani)

contas = [conta_da_dani, conta_do_qui]
print(contas)

for conta in contas:
    print(conta)

# Duas referentas para o objeto da conta do qui
contas = [conta_do_qui, conta_da_dani, conta_do_qui]
print(contas[0])
print(contas[2])
