# Problema de classificação de vidros do Kaggle

Este é um problema retirado da base de dados do [Kaggle](https://www.kaggle.com/uciml/glass). Para resolver este problema foram utilizados códigos em Python e algoritmos de Machine Learning para obtenção de insights e criação de modelos preditivos. O código foi escrito em um Jupyter Notebook e para acessá-lo basta clicar  em [Data Analysis.ipynb](https://github.com/davi-santos/Glass-Classification/blob/main/Data%20Analysis.ipynb).

Esta página contém os seguintes tópicos resumidos:

1. Visão Geral
2. Algoritmos de Machine Learning
3. Resultados

A versão completa e mais detalhada está no Jyputer Notebook deste repositório, no arquivo [Data Analysis.ipynb](https://github.com/davi-santos/Glass-Classification/blob/main/Data%20Analysis.ipynb).

### 1. Visão Geral

Esta base de dados possui 214 amostras de vidro, 9 atributos e uma classe (que é o tipo do vidro). Os atributos são os seguintes:

* RI - Índice de Refração do vidro/
* Na - Sódio (unidade de medida: peso percentual, assim como o restante dos atributos a seguir)
* Mg - Magnésio
* Al - Alumínio
* Si -Silício
* K - Potássio
* Ca - Cálcio
* Ba - Bário
* Fe - Ferro

Os vidros podem ser classificados em: 
* 1 - construção de janelas flutuante processado
* 2 - building_windows_non_float_processed
* 3 - vehicle_windows_float_processed
* 4 - vehicle_windows_non_float_processed
* 5 - containers
* 6 - tableware
* 7 - headlamps

Nesta Figura é possível perceber que há mais amostras para os vidros 1 e 2. É possível observar também que não há amostra para a classe 4. A classe 6 é a classe em que há menos vidros.

![alt text](https://github.com/davi-santos/Glass-Classification/blob/main/figures/amostras.png)

A matriz a seguir é conhecida como matriz de correlação. É uma matriz com valores que variam de -1 a 1, tal que -1 indica correlação inversa e 1 indica correlação direta entre duas variáveis. Com essa matriz, é possível observar que os atributos RI e Ca são os atributos que possuem maior correlação nesta base de dados; ao passo que, os atributos RI e Si possuem a menor correlação na base de dados.

![alt text](https://github.com/davi-santos/Glass-Classification/blob/main/figures/matrix.png)

Para analisar melhor essa correlação, vamos plotar a figura dos elementos Ca e Si em relação à RI. 

![alt text](https://github.com/davi-santos/Glass-Classification/blob/main/figures/elementos_corr.png)

Aqui, é possível observar que de fato essas variáveis possuem algum grau de correlação com RI (sendo Ca correlação positiva e Si correlação inversa).

### 2. Algoritmos de Machine Learning

  Os algoritmos de Machine Learning treinados foram as Decision Trees, Random Forest e Logistic Regression. Primeiramente, a base foi separada em 70% para treinamento e 30% para teste.

#### 2.1 Decision Trees

  Para treinamento, foram testadas diferentes profundidades para este problema. A Decision Tree de profundidade 5 foi a que apresentou melhor *score* no treinamento e no teste. 

#### 2.2 Random Forest
  Para treinamento, foram testados diferentes números de estimadores e foi fixada a profundidade de 10 para as árvores. A Ranfom Forest de 10 estimadores foi a que apresentou melhores resultados nesta primeira investigação.


#### 2.3 Logistic Regression

  Para o treinamento, foram testados diferentes valores para a regularização C. Todos os valores de C apresentaram resultados semelhantes, então foi escolhido o maior valor de C=500.

### 3. Resultados

![alt text](https://github.com/davi-santos/Glass-Classification/blob/main/figures/acuracia_modelos.png)

Foram treinados alguns modelos de Machine Learning em Decision Trees, Random Forest e Logistic Regression. Ambos os modelos apresentaram acurácia média por volta dos 60%, com destaque para as Random Forests com 70% de acurácia. Contudo, todos os modelos falharam em classificar as amostras da classe 3. Para mais informações acesse o arquivo [Data Analysis.ipynb](https://github.com/davi-santos/Glass-Classification/blob/main/Data%20Analysis.ipynb).

