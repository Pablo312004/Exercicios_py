def nome_e_sobrenomem():
	nome= input("Digite seu primeiro nome, por favor:")
	nome_sem_espaco_e_em_maiusculo= nome.upper().replace(" ", " ")
	sobrenome= input("Digite seu sobrenome, por gentileza: ")
	sobrenome_em_minusculo_e_sem_espaco= sobrenome.lower().replace(" ", " ")
	print(" O seu primeiro Nome é: " , nome_sem_espaco_e_em_maiusculo , " e seu sobrenome é: " , sobrenome_em_minusculo_e_sem_espaco ) 