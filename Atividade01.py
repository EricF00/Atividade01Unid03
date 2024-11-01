# -*- coding: latin1 -*-

#Programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
dias = int(input("Digite sua idade em dias: "))
anos = dias // 365
dias = dias % 365
meses = dias // 30
dias = dias % 30
print(f"Sua idade expressa em ano(s), mes(es) e dia(s) é:")
print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s).")
