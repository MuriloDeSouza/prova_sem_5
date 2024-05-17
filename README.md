# prova_sem_5

Este é um programa Python para controlar uma tartaruga no Turtlesim usando o ROS (Robot Operating System). O programa desenha um quadrado e permite aprender os comandos básicos para controlar o robô, aplicando-os em um projeto simples.

## Pré-requisitos

Certifique-se de ter o ROS instalado no seu sistema. Além disso, é necessário preparar a área de trabalho para trabalhar com o ROS. 

1. Instale o ROS seguindo as instruções no site oficial: [ROS Installation](http://wiki.ros.org/Installation).
2. Prepare a área de trabalho executando os seguintes comandos no terminal:

```bash
colcon build
source install/local_setup.bash
```

## Intalação do Turtlesim

Para usar o Turtlesim, é necessário preparar o ambiente executando os seguintes comandos:

1. Abra o Turtlesim em um terminal:

```bash
ros2 run turtlesim turtlesim.node
```

## Executando o Programa

Após preparar o ambiente, você pode executar o programa para controlar a tartaruga no Turtlesim. Execute o seguinte comando no terminal:

```bash
ros2 run ponderada_semana_2 ponderada_2
```

## Detalhes do Projeto

O intuito deste projeto é aprender os comandos básicos para controlar um robô no ambiente do ROS. O desenho de um quadrado foi escolhido como exemplo, pois é uma tarefa simples que envolve movimentos básicos (avançar, girar) e é útil para entender como controlar a tartaruga no Turtlesim.

É importante preparar o arquivo setup.py para configurar o ambiente de trabalho e tornar possível a execução do projeto do Turtlesim. Este arquivo contém informações sobre as dependências e configurações do projeto.

## Autor

Este projeto foi desenvolvido por mim, Murilo de Souza Prianti Silva.

## Link do vídeo de funcionamento

Segue o link do drive com o vídeo do funcionamento:
https://drive.google.com/file/d/1dP__wFe3IbzYHuusS36EPy-NuadEqemV/view?usp=sharing