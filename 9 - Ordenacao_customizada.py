import array as arr
import numpy as np
from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering


def extrai_saldo(conta):
    return conta._saldo


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


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>> Código {} saldo {} <<]".format(self._codigo, self._saldo)


class MultiploSalario(ContaSalario):
    pass


# conta1 = ContaSalario(37)
# print(conta1)
#
# conta2 = ContaCorrente(37)
# print(conta2)

# conta1.deposita(1)

# print(conta1 == conta2)
#
# print(isinstance(ContaCorrente(34), ContaSalario))

idades = [15, 87, 32, 65, 56, 32, 49, 37]

# for i in range(len(idades)):
#     print(i, idades[i])
#
# print(enumerate(idades))  #lazy
#
# print(list(range(len(idades)))) #forcei a geração dos valores
#
# print(list(enumerate(idades))) #forcei a geração dos valores e o enumerate gera tuplas


# for indice, idade in enumerate(idades):
#     print(indice, idade)


usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

# for nome, _, _ in usuarios: #ignorar itens utilizando o _
#     print(nome)

# ordenar
# print(sorted(idades))

# retornar ao inverso
# print(list(reversed(idades)))

# ordenar do maior para o menor
# print(sorted(idades, reverse=True))

# inverter e ordenar
# print(list(reversed(sorted(idades))))
#
# print(idades)

# Ordena a lista
# idades.sort()
#
# print(idades)
#
# nomes = ['Guilherme', 'Daniela', 'Paulo']
#
# print(sorted(nomes))

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_do_daniela = ContaSalario(3)
conta_do_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_do_daniela, conta_do_paulo]

# for conta in contas:
#     print(conta)

# for conta in sorted(contas, key=extrai_saldo):
#     print(conta)

# for conta in sorted(contas, key=attrgetter("_saldo")):
#     print(conta)

# print(conta_do_guilherme > conta_do_daniela)
#
# for conta in sorted(contas):
#     print(conta)

# attrgetter pode utilizar mais de um atributo para comparar os itens
# for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
#     print(conta)


for conta in sorted(contas):
    print(conta)


print(conta_do_guilherme <= conta_do_daniela)
print(conta_do_guilherme > conta_do_paulo)
print(conta_do_guilherme < conta_do_guilherme)
print(conta_do_guilherme == conta_do_guilherme)