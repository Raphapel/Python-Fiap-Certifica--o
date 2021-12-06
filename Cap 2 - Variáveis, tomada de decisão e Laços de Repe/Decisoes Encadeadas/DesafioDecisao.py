# elaborar o code para resolver a seguinte situação: o seu módulo solicitara o nivel de acesso de uma pessoa que pode ser:  ADM, USR ou GUEST e o genero dessa pessoa, caso o nivel for USR, deverá exibir "ola usuario" para os homens ou "ola usuaria" para as mulhers. se o nivel for GUEST, a mensagem devera ser "ola visitante". E se o nivel digitador for diferente de ADM, USR ou GUEST, devera exibir a mensagem ola "desconhecido"

# aperte alt + z (VSCODE)

nivelAcesso = input("Informe o nivel de acesso (ADM, USR ou GUEST): ").upper()
sexo = input("informe o sexo M ou F: ").upper()

if nivelAcesso == "USR":
    if sexo == "M":
        print("Olá usuário.")
    else:
        print("Olá usuária.")

elif nivelAcesso == "GUEST":
    print("Olá visitante")

elif nivelAcesso == "ADM":
    if sexo == "M":
        print("Olá Administrador.")
    else:
        print("Ola Administradora.")

else:
    print("Olá desconhecido(a).")
