# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da liguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar error no final)
# Levantando(raise) / Lançando (Throw) exceções
# Relançando exceções 
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    ...


class OutroError(Exception):
    ...
 

def levantar():
        exception_ = MeuError('A','B','C')
        exception_.add_note('Olha a nota1') # Anotações de error.
        raise exception_

try:
    levantar()

except (MeuError, ZeroDivisionError) as error:
    print(error)
    print(error.__class__.__name__)
    print()
    exception_ = OutroError('A','B','C')
    raise exception_ from error