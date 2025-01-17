# Sentinela
  O Projeto Sentinela consiste em uma Inteligência Artificial capaz de detecção 4 gestos de mão: 
  - Paz 
  - Joinha 
  - Rock 
  - Saudação vulcana.

## DataSet
  O DataSet possui todos os dados, fotos dos gestos, que foram coletados no início do projeto. Esse DataSet possui 456 imagens no total, sendo dividida para 4 classes de gestos. Cada gesto contém cerca de 114 imagens cada um.

## Parâmetros de Treinamentos
   
- Épocas Utilizadas: 50
- Tamanho da Imagem: 640px

## Validação Cruzada
  Os dados do dataset foram divididos em:
  - 20% Validação
  - 80% treinamento
    
  Sendo assim, o dataset foi divido em 5 pedaços, cada um contendo um conjunto de imagens em específico para cada propósito(1 para validação e 4 para treinamento). Dessa forma foram testadas todas as combinações e selecionado o modelo que obteve o melhor resultado.

## Execução
  - Primeiro é necessário a instalação do Python, das bibliotecas listadas em requirements.txt e uma webcam.
  - Para executar o projeto basta o arquivo detect.py e o modelo treinado TheChosenOne.pt
  - Por fim deve-se modificar a variável path_modelo com o caminho que o mesmo se encontra
