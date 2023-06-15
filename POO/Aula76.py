# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractclassmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractclassmethod
    def enviar(self) -> bool:
        ...
        
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('E-SMS: enviando - ', self.mensagem)
        return False

n = NotificacaoEmail('Testando...')
n.enviar()

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Não enviada :(')

notificacao_Email = NotificacaoEmail('TESTANDO E-MAIL')
notificar(notificacao_Email)

notificacao_sms = NotificacaoSMS('TESTANDO SMS')
notificar(notificacao_sms)