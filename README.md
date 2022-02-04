# Problema da classificação de vidros

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

### 3. Resultados

Foram treinados alguns modelos de Machine Learning em Decision Trees e Logistic Regression. Ambos os modelos apresentaram boa performance no geral, classificando bem quase todas as classes. A classe com pior predição foi a classe 3. Para mais informações acesse o arquivo [Data Analysis.ipynb](https://github.com/davi-santos/Glass-Classification/blob/main/Data%20Analysis.ipynb).

