# kmeans

Esse projeto é uma simples implementação do algoritmo kmeans utilizando apenas numpy.
A idéia aqui é mostrar para iniciantes o funcionamento do algoritmo e como seria uma implementação bem básica em python, sem o uso de bibliotecas que trazem o algorimto já pronto.


## Requisitos

Você vai precisar instalar as bibliotecas que estão no requirements.txt. Para isso, data pasta do projeto, faça:

`pip3 install -r requirements.txt`

##  Como rodar?

Para rodar, basta executar o script kmeans.py que se encontra na raiz do projeto.

`python3 kmeans.py`

Durante a execução, uma janela com o dataset e os centroids plotados deve mostrar a evolução do algoritmo.

![kmeans.py](https://i.imgur.com/8YEXrrz.png)


## Como colocar uma nova distância?

Para adicionar uma nova distância, basta adicionar uma função no arquivo distance.py, tal qual a distância euclidiana que já se encontra neste mesmo arquivo.

Feito isso, no arquivo kmeans.py, na chamada para a função kmeans, passe a distância que você adicionou.

Ex.:
Em um exemplo que você dicionou a distancia `mynewdistance` no arquivo distance.py

Você precisa alterar a função execute como abaixo:

```
def execute():
    dataset = load_dataset('flame.txt')
    centroids, history_centroids, belongs_to = kmeans(2, dataset, distance=mynewdistance)
    plot(dataset, history_centroids, belongs_to)

```
## Como colocar um novo dataset?

Para colocar um dataset novo, basta colocar dentro da pasta `data`. Para que tudo funcione corretamente, você precisa garantir que o dataset seja em formato `.txt` e que as características sejam separadas por tab.  Basta olhar os exemplos que já estão no projeto para ter uma noção.

Uma vez que o dataset foi adicionado,  você precisa mudar a atribuição do dataset dentro da função execute.

Ex.:
Imagine que você adicionou na pasta data o dataset `mynewdataset.txt`. Para executar o algoritmo, seria:

```
def execute():
    dataset = load_dataset('mynewdataset.txt')
    centroids, history_centroids, belongs_to = kmeans(2, dataset, distance=mynewdistance)
    plot(dataset, history_centroids, belongs_to)

```

### ### ALERTA!!! ####
Não versione arquivos de datasets grandes. Os arquivos da pasta `data` estão versionados nesse projeto, apenas para fins educativos. Normalmente, arquivos de bases de dados NÂO devem ser adicionados ao github.


## Como funciona esse algoritmo?

Há uma explicação do funcionamento básico do algoritmo kmeans no arquivo `kmeans.py.ipnb`. É um jupyter notebook. Se tiver duvida de como abrir um jupyter notebook, abrindo o arquivo no github, é possível ver o conteúdo renderizado.



Espero que esse projeto seja útil.


