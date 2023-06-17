
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_qui = ContaCorrente(15)
print(conta_qui)
conta_qui.deposita(500)
print(conta_qui)

conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)
print(conta_dani)

contas = [conta_qui, conta_dani]
print(contas)

