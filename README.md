# prova_sem_5

Este é um programa Python para controlar uma tartaruga no Turtlesim usando o ROS (Robot Operating System). O programa vai funcionar com uma fila e ai vai consumindo da esquerda para a direita os movimentos que a pessoa coloca

## Pré-requisitos

Certifique-se de ter o ROS instalado no seu sistema. Além disso, é necessário preparar a área de trabalho para trabalhar com o ROS. 

1. Instale o ROS seguindo as instruções no site oficial: [ROS Installation](http://wiki.ros.org/Installation).

2. Rode esses comando para poder preparar a área do seu pc para funcionar:
```cmd
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
rosdep install -i --from-path src --rosdistro humble -y
```

3. Prepare a área de trabalho executando os seguintes comandos no terminal:

```bash
colcon build
source install/local_setup.bash
```

4. Para poder baixar todas as dependências usamos o código:
```bash
python3 -m pip install -r requirements.txt
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

O objetivo do projeto é criar uma aplicação que permitam as pessoas que vão usar o código, enviar comandos de movimento para a tartaruga no Turtlesim ( em um formato de vx(0.0), vy(0.0) vtheta(0.0) e time(1000)). Esses comandos estão sendo enfileirados e são executados sequencialmente, garantindo que cada comando seja concluído antes que o próximo seja iniciado com o uso do deque que fica presente no collections que ja vem com o python. Dessa forma, podemos proporcionar uma experiência de uso fluida para os operadores.

## Autor

Este projeto foi desenvolvido por mim, Murilo de Souza Prianti Silva.
