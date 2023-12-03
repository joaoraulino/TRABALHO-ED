class TrainCar:
    def __init__(self, num, carga):
        self.numero = num
        self.tipo_carga = carga
        self.next_carga = None
        self.previous_carga = None

class Train:
    def __init__(self):
        self.cabeca = None

    def cargaDupla(self, num):
        atual = self.cabeca
        while atual is not None:
            if atual.numero == num:
                return True  # Já existe um vagão com esse número
            atual = atual.next_carga
        return False

    def addCar(self, num, carga):
        if self.cargaDupla(num):
            print(f"Erro: Já existe um vagão com o número {num}.")
            return

        nova_carga = TrainCar(num, carga)
        if nova_carga is None:
            print("Erro: Falha ao alocar memória para o novo vagão.")
            return

        if self.cabeca is None:
            # Se for o primeiro vagão, o tornamos o primeiro e único na lista
            self.cabeca = nova_carga
        else:
            # Caso contrário, adicionamos ao final da lista
            atual = self.cabeca
            while atual.next_carga is not None:
                atual = atual.next_carga
            atual.next_carga = nova_carga
            nova_carga.previous_carga = atual

    def TrainInfo(self):
        atual = self.cabeca
        while atual is not None:
            print(f"Vagão #{atual.numero} - Tipo de Carga: {atual.tipo_carga}")
            atual = atual.next_carga

    def deletarTrain(self):
        atual = self.cabeca
        while atual is not None:
            next_carga = atual.next_carga
            del atual
            atual = next_carga
        self.cabeca = None


# Criando um trem e adicionando alguns vagões
myTrain = Train()
myTrain.addCar(1, "Feijão")
myTrain.addCar(2, "Arroz")
myTrain.addCar(3, "Produtos Químicos")

# Tentando adicionar um vagão com número duplicado
myTrain.addCar(1, "Metal")  # Isso deverá imprimir uma mensagem de erro

# Exibindo informações sobre os vagões no trem
print("Informações sobre os Vagões no Trem:")
myTrain.TrainInfo()

# Limpando a memória alocada pelos vagões
myTrain.deletarTrain()