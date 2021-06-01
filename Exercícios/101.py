from datetime import date


def voto(ano):
    data = date.today().year
    idade = data - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))
