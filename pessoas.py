class Pessoas:
    def __init__(self, nome, documento, tel):
        self.nome = nome
        self.documento = documento
        self.tel = tel


    def incluirNome(self):
        self.nome = entr_nome.get()
        self.documento = entr_documento.get()
        self.tel = entr_tel.get()


class dadosBanco:
    def __init__(self, banco, agencia, conta):
        self.banco = banco
        self.agencia = agencia
        self.conta = conta


    def incluirBanco(self):
        self.banco = entr_banco.get()
        self.agencia = entr_agencia.get()
        self.conta = entr_contCorrente.get()













