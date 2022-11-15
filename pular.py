from crianca import Crianca


class PulaPula:

    def _init_(self, limiteMax):
        self.limite = limiteMax
        self.fila = []
        self.pulapula = []
        self.contaPendente = dict()
        self.caixa = 0

    def getFilaDeEspera(self):
        return self.fila

    def getCriancasPulando(self):
        return self.pulapula

    def getLimiteMax(self):
        return self.limite

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        test = self.contaPendente.get(nome, 'Erro')
        if test != 'Erro':
            return self.contaPendente[nome]
        else:
            print('Sem conta para pagar')
            return None

    def entrarNaFila(self, crianca: Crianca):
        for nome in self.fila:
            if crianca.getNome() == nome.nome:
                print('criança com o mesmo nome na fila')
                return False
        for nome in self.pulapula:
            if crianca.getNome() == nome.nome:
                print('criança com o mesmo nome no Pula-pula')
                return False
        self.fila.append(crianca)
        return True

    def entrar(self):
        if len(self.fila) > 0 and len(self.pulapula) < self.limite:
            self.pulapula.append(self.fila[0])
            if self.fila[0].nome in self.contaPendente:
                self.contaPendente.update({self.fila[0].nome: self.contaPendente[self.fila[0].nome]+2.50})
            else:
                self.contaPendente.update({self.fila[0].nome: 2.50})
            self.fila.pop(0)
            return True
        else:
            print('não tem criança na fila ou maximo alcançado')
            return False

    def sair(self):
        if len(self.pulapula) > 0:
            self.fila.append(self.pulapula[0])
            self.pulapula.pop(0)
            return True
        else:
            print('não tem crianças no Pula-pula')
            return False

    def papaiChegou(self, nome):
        achou = None
        for crianca in self.fila:
            if crianca.nome == nome:
                achou = crianca
        if achou == None:
            for crianca in self.pulapula:
                if crianca.nome == nome:
                    achou = crianca
            if achou == None:
                print('crianca nao existe')
                return False
            else:
                self.pulapula.remove(achou)
                self.caixa += self.contaPendente[nome]
                del self.contaPendente[nome]
                return True
        else:
            self.fila.remove(achou)
            test = self.contaPendente.get(nome, 'Erro')
            if test != 'Erro':
                self.caixa += self.contaPendente[nome]
                del self.contaPendente[nome]
            return True

    def fechar(self):
        for criancas in self.contaPendente.keys():
            self.caixa += self.contaPendente[criancas]
        self.fila.clear()
        self.pulapula.clear()
        self.contaPendente.clear()
        return self.caixa
