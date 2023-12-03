class TrainCar:
    def __init__(self, num, carga):
        self.numero = num
        self.tipo_carga = carga
        self.next_carga = None
        self.previous_carga = None

class Train:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def cargaDupla(self, num):
        atual = self.cabeca
        while atual is not None:
            if atual.numero == num:
                return True  # Já existe um vagão com esse número
            atual = atual.next_carga
        return False

    def addCar_inicio(self,num,carga):
        if self.cargaDupla(num):
            print(f"Erro: Já existe um vagão com o número {num}.")
            return

        nova_carga = TrainCar(num,carga)
        nova_carga.next_carga = self.cabeca

        if self.cabeca:
            self.cabeca.previous_carga = nova_carga
        else:
            self.cauda = nova_carga
        self.cabeca = nova_carga

    def addCar_meio(self,posicao,num,carga):
        if self.cargaDupla(num):
            print(f"Erro: Já existe um vagão com o número {num}.")
            return

        if posicao == 0:
            self.addCar_inicio(num,carga)
            return

        nova_carga = TrainCar(num,carga)
        atual = self.cabeca
        for i in range(posicao - 1):
            if atual is None:
                raise Exception("Posição inválida")
            atual = atual.next_carga
        nova_carga.next_carga = atual.next_carga
        atual.next_carga = nova_carga
        if atual.next_carga:
            atual.next_carga.previous_carga = nova_carga
        else:
            self.cauda = nova_carga
        atual.next_carga = nova_carga

    def addCar_final(self, num, carga):
        if self.cargaDupla(num):
            print(f"Erro: Já existe um vagão com o número {num}.")
            return

        nova_carga = TrainCar(num, carga)
        if nova_carga is None:
            print("Erro: Falha ao alocar memória para o novo vagão.")
            return

        if not self.cabeca:
            self.cabeca = nova_carga
            self.cauda = nova_carga
            return
        self.cauda.next_carga = nova_carga
        nova_carga.previous_carga = self.cauda
        self.cauda = nova_carga

    def buscar_Train(self,numero): #Busca
        atual = self.cabeca

        while atual is not None:
            if atual.numero == numero:
                print(f'O vagão {atual.numero} está no trem com a carga {atual.tipo_carga}')
                break
            atual = atual.next_carga

        return None

    def TrainInfo(self): #Travessia
        atual = self.cabeca
        while atual is not None:
            print(f"Vagão #{atual.numero} - Tipo de Carga: {atual.tipo_carga}")
            atual = atual.next_carga

    def deletarTrain(self,numero):
        atual = self.cabeca

        while atual:
            if atual.numero == numero:
                if atual.previous_carga:
                    atual.previous_carga.next_carga = atual.next_carga
                else:
                    self.cabeca = atual.next_carga

                if atual.next_carga:
                    atual.next_carga.previous_carga = atual.previous_carga
                else:
                    self.cauda = atual.previous_carga

                return True

            atual = atual.next_carga

        return False



# Criando um trem e adicionando alguns vagões
myTrain = Train()
myTrain.addCar_final(1, "Feijão")
myTrain.addCar_final(2, "Arroz")
myTrain.addCar_final(4, "Produtos Químicos")
myTrain.addCar_inicio(0,"Carvão")
myTrain.addCar_meio(3,3,"Petróleo")

# Tentando adicionar um vagão com número duplicado
myTrain.addCar_final(5, "Metal")  # Isso deverá imprimir uma mensagem de erro

# Exibindo informações sobre os vagões no trem
print("Informações sobre os Vagões no Trem:")
myTrain.TrainInfo()

# Busca de vagões pela número de identificação
myTrain.buscar_Train(3)

# Limpando a memória alocada pelos vagões
myTrain.deletarTrain(2)

# Exibindo informações sobre os vagões no trem depois da exclusão
print("Informações sobre os Vagões no Trem:")
myTrain.TrainInfo()
