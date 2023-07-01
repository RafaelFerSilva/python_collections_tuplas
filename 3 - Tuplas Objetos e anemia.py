def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_do_qui = ContaCorrente(15)
conta_do_qui.deposita(900)
print(conta_do_qui)

conta_da_dani = ContaCorrente(1000)
conta_da_dani.deposita(300)
print(conta_da_dani)

contas = [conta_do_qui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

