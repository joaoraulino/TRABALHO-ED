# TRABALHO-ED

**Participantes:**
**<li>João Victor de Souza Raulino [@joaoraulino](https://github.com/joaoraulino) </li>**
**<li>Yan Ferreira Rocha [@Yanfr086](https://github.com/Yanfr086) </li>**
**<li>Caio de Barros Miranda [@dynamzz](https://github.com/dynamzz) </li>**

**Descrição do Projeto: Simulação de Trem de Carga com Lista Duplamente Encadeada em Python**

  Em resumo, sobre o sistema de gerenciamento de vagões em uma estação ferroviária é projetado para acompanhar e organizar os vagões de trem, suas características, a ordem em que estão acoplados e seus números de indentificação. A lista duplamente encadeada garante que a conexão entre os vagões seja eficiente e permita a navegação em ambas as direções, seja para remover, adicionar ou buscar um vagão entre o trem. Nesse sistema tem importância nas operações ferroviárias, pois ajuda a otimizar o transporte de carga e passageiros, garantindo um funcionamento seguro e eficaz da estação ferroviária.
  
Este projeto implementa uma estrutura de dados de lista encadeada para representar um trem de vagões. Cada vagão é representado por uma classe `TrainCar`, que contém o número do vagão e o tipo de carga. A classe `Train` representa o trem e possui métodos para adicionar, remover e buscar vagões.

**Funcionalidades Implementadas:**

**<ul>Inclusão de Vagões:</ul>**

<li>Através da função de inclusão, novos vagões de carga podem ser adicionados à composição do trem, no início, meio e fim. Cada vagão é representado como um nó na lista duplamente encadeada, contendo informações relevantes, como carga transportada e número de identificação.</li>

**<ul>Exclusão de Vagões:</ul>**

<li>A exclusão de vagões permite a remoção de unidades específicas da composição do trem. Isso é útil para reorganizar a carga ou ajustar a estrutura do trem conforme necessário.</li>

**<ul>Identificação de Vagões:</ul>**

<li>A função de identificação possibilita a busca e recuperação de informações sobre vagões específicos. Os vagões podem ser identificados pelo número atribuído, facilitando a localização de dados específicos.</li>


**Instruções de Uso**

As seguintes operações podem ser realizadas com o trem de vagões:

* Adicionar um vagão:

<pre>
myTrain.addCar_inicio(0, "Carvão")
myTrain.addCar_meio(1, 1, "Combustível")
myTrain.addCar_final(2, "Petróleo") 
</pre>


* Remover um vagão:

<pre>myTrain.deletarTrain(0)</pre>

* Buscar um vagão:

<pre>myTrain.buscar_Train(3)</pre>


**<p>Exibição da Composição do Trem:</p>**

A aplicação permite a visualização da composição atual do trem, exibindo detalhes sobre cada vagão presente na lista duplamente encadeada. Isso proporciona uma visão clara da estrutura do trem de carga.
Como Utilizar:

O código Python disponibilizado implementa classes e métodos para a criação e manipulação da estrutura de lista duplamente encadeada. Siga as instruções no código para utilizar as funcionalidades de inclusão, exclusão, identificação e exibição de vagões.

**Referências**
<li>[ed-cic-2023-2 (Reposítorio da professora Geovana Ramos)]([URL_do_Link](https://github.com/GeovanaRamos/ed-cic-2023-2))</li>
<li>[Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python](https://panda.ime.usp.br/pythonds/static/pythonds_pt/index.html)</li>
<li>KARUMANCHI, Narasimha. Data Structure and Algorithmic Thinking with Python</li>
