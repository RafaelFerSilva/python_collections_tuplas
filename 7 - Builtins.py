import array as arr
import numpy as np
from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>> Código {} saldo {} <<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Código {} saldo {} <<]".format(self._codigo, self._saldo)


class MultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaCorrente(37)
print(conta2)

# conta1.deposita(1)

print(conta1 == conta2)

print(isinstance(ContaCorrente(34), ContaSalario))

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

print(enumerate(idades))  #lazy

print(list(range(len(idades)))) #forcei a geração dos valores

print(list(enumerate(idades))) #forcei a geração dos valores e o enumerate gera tuplas


for indice, idade in enumerate(idades):
    print(indice, idade)


usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, _, _ in usuarios: #ignorar itens utilizando o _
    print(nome)
