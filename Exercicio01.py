def substitutiva(palavra):
	palavra_a_ser_substituida= ""
	vogais= "AEIOUaeiou"
	for letra in palavra:
		if letra in vogais:
			palavra_a_ser_substituida += "*"
		else
		palavra_a_ser_substituida += letra
		return palavra_a_ser_substituida

palavra= input(" Digite uma palavra por favor ")
palavra_a_ser_substituida = substitutiva(palavra):
print(" A palavra substituída é: ", palavra_a_ser_substituida);