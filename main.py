# Plastyne | Anarchy Ghost
# Fallow me on Twitter: 
# Donate-me BITCOIN: 3CmG7qeQEWteUPRBb3dopBnGDC26qws8pk
# A.C.A.B | FUCK ALL COPS
# // 1 - Separador de DB email e senhas no formato emaildofulano@gmail.com|minhasenha
# // 2 - O script em si carrega um arquivo dentro do código chamado lista.txt esse lista tem de conter as informações no formato acima Email|senha na mesma pasta do script
# // 3 - Após a execução do mesmo, dois arquivos irão ser gerados, o senhas.txt e o emails.txt, um poderá ser utilizado para wordlist, e outro para spam no SMTP 'provedores de email em caixas de entradas'
############################################################################################################################################################################################################
def run():
    with open("lista.txt", "r", encoding="utf8") as r:
        db = r.read()
        r.close()

    emails = []
    senhas = []
    for line in db.split("\n"):
        s = line.split(":")
        try:
            email = s[0]
            senha = s[1]
            emails.append(email)
            senhas.append(senha)
        except IndexError as e:
            print(e)

    print(f'finish emails->{len(emails)};senhas->{len(senhas)}')

    with open("emails.txt", "a", encoding="utf8") as w:
        for email in emails:
            w.write(email + "\n")
        w.close()

    with open("senhas.txt", "a", encoding="utf8") as w:
        for senha in senhas:
            w.write(senha + "\n")
        w.close()

    print('Finish')


if __name__ == '__main__':
    run()