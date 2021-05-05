# Modelo Mercado Livre

Foi construido por mim um mapa de refêrencia no site https://www.google.com/search?q=mercado+de+investimento&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjd5PiF76jwAhUcJrkGHWdzD6wQ_AUoAXoECAEQAw&biw=1920&bih=976
cujo objetivo é entender qual site seguinte na busca, será o mais visualizado pelos usuários durante a navegação. E assim sucessivamente. 

Com os dados obtidos, foi treinado um modelo contra dados históricos.

Meu desafio será contar o número de referências (“aparições”) que encontramos de um link de outras fontes. 

1 - https://www.google.com/search?q=mercado+de+investimento&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjd5PiF76jwAhUcJrkGHWdzD6wQ_AUoAXoECAEQAw&biw=1920&bih=976
2 - https://www.infomoney.com.br/stock-pickers/por-que-as-acoes-do-mercado-livre-ainda-podem-subir-50-segundo-analista-da-encore/
3 - https://www.infomoney.com.br/tudo-sobre/mercadolivre/

First Part: Generation of Features 
Na primeira instância, o objetivo é construir um projeto que tenha a capacidade de rastrear os diferentes links de um conjunto base e persistir, para cada link, quantas referências diferentes (aparências) de páginas externas foram encontradas. 

Além disso, esta informação pode ser enriquecida para cada link com a informação que se considere necessária armazenar.

Uma vez finalizado o mapa, para cada elo do conjunto de base é necessário construir um vetor com pelo menos 10 características numéricas com base no referido mapa, utilizando a informação de enriquecimento previamente obtida.

Por fim, uma API REST será construída de forma a utilizar o armazenamento definido e permitir a obtenção do vetor de recursos associados a um link:
● Se o link estiver no banco de dados, responda o vetor pré-calculado.
● Se o link não for encontrado no banco de dados, os valores correspondentes ao vetor devem ser calculados, inseridos no banco de dados e depois devolvidos. Este vetor não terá o número de referências externas calculadas.
