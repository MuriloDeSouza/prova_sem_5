#!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from turtlesim.srv import Spawn, Kill, SetPen
# import time

# class TurtleController(Node):
#     def __init__(self):
#         super().__init__('turtle_controller')
#         self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

#     def move_turtle(self, linear, angular):
#         twist = Twist()
#         twist.linear.x = linear
#         twist.angular.z = angular
#         self.publisher.publish(twist)

# def desenho(controller):
#     # Movimentos para desenhar um quadrado
#     movements = [
#         (0.0, 0.0),    # Iniciar
#         (2.0, 0.0),    # Lado 1
#         (0.0, 1.56),    # Lado 2
#         (2.0, 0.0),   # Lado 3
#         (0.0, 1.56),   # Lado 4
#         (2.0, 0.0),     # Voltar para o início
#         (0.0, 1.56),     # Voltar para o início
#         (2.0, 0.0),
#         (0.0, 1.56)     # Voltar para o início
#     ]

#     # Executar os movimentos
#     for linear, angular in movements:
#         controller.move_turtle(linear, angular)
#         time.sleep(1)  # Pausa de 1 segundo entre os movimentos


# def main(args=None):
#     rclpy.init(args=args)
#     controller = TurtleController()
#     print("Desenhando um quadrado...")
#     set_pen_color(255,0,255)
#     desenho(controller)

#     # Criação de uma nova tartaruga
#     node = rclpy.create_node('spawn_turtle_client')
#     client = node.create_client(Spawn, '/spawn')

#     request = Spawn.Request()
#     request.x = 5.0
#     request.y = 5.0
#     request.theta = 0.0
#     request.name = 'my_turtle'

#     future = client.call_async(request)
#     rclpy.spin_until_future_complete(node, future)

#     if future.result() is not None:
#         print('Turtaruga nova com sucesso', future.result().name)
#     else:
#         print('Failed to spawn turtle')

#     time.sleep(2)

#     # Matar a tartaruga
#     kill_request = Kill.Request()
#     kill_request.name = 'my_turtle'
#     kill_client = node.create_client(Kill, 'kill')

#     future_kill = kill_client.call_async(kill_request)
#     rclpy.spin_until_future_complete(node, future_kill)

#     if future_kill.result() is not None:
#         print(1)
#         # print('Turtle killed successfully:', future_kill.result().name)
#     else:
#         print('Failed to kill turtle')

#     controller.destroy_node()
#     rclpy.shutdown()

# def set_pen_color(r, g, b):
#     node = rclpy.create_node('set_pen_color')
#     set_pen_client = node.create_client(SetPen, '/turtle1/set_pen')

#     while not set_pen_client.wait_for_service(timeout_sec=1.0):
#         print('Service not available, waiting again...')

#     request = SetPen.Request()
#     request.r = r
#     request.g = g
#     request.b = b
#     request.width = 8  # Mantém a largura da linha inalterada
#     request.off = 0    # Mantém a caneta ligada

#     future = set_pen_client.call_async(request)
#     rclpy.spin_until_future_complete(node, future)

# if __name__ == '__main__':
#     main()


#!/usr/bin/env python3
# import rclpy
# from geometry_msgs.msg import Twist
# import time
# from collections import deque
# import time

# class TurtleController:
#     def __init__(self):
#         rclpy.init()
#         self.node = rclpy.create_node('turtle_controller')
#         self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 4)

#     def move_turtle(self, linear, angular):
#         twist = Twist()
#         twist.linear.x = linear
#         twist.angular.z = angular
#         self.publisher.publish(twist)

#     def destroy(self):
#         self.node.destroy_node()
#         rclpy.shutdown()

#     def add_movement(self, linear, angular):
#         self.movements.append((linear, angular))

#     def process_movements(self):
#         while self.movements:
#             linear, angular = self.movements.popleft()
#             self.move_turtle(linear, angular)
#             time.sleep(1)  # Ajuste o tempo conforme necessário


# def main():
#     controller = TurtleController()

#     print("Controle da Tartaruga Turtlesim")
#     print ("Digite 'socorro' para parar a tartaruga")
#     print("Adicione as movimentações que vc quiser para ele fazer")
#     print("Digite 'frente', 'trás', 'esquerda', 'direita' ou 'sair' e pressione Enter para mover a tartaruga.")
    
#     while True:
#         command = input("Comando: ").lower()

#         if command == 'sair':
#             break
#         elif command == 'frente':
#             controller.move_turtle(2.0, 0.0)
#         elif command == 'trás':
#             controller.move_turtle(-2.0, 0.0)
#         elif command == 'esquerda':
#             controller.move_turtle(0.0, 1.56)
#         elif command == 'direita':
#             controller.move_turtle(0.0, -1.56)
#         elif command == 'socorro':
#             controller.move_turtle(0.0, 0.0)
#         else:
#             print("Comando inválido! Use 'frente', 'trás', 'esquerda', 'direita' ou 'sair'.")

#     controller.destroy()

# if __name__ == '__main__':
#     main()


# import rclpy
# from geometry_msgs.msg import Twist
# import time
# from collections import deque
# import argparse

# class TurtleController: #continua como o padao de vel 10 e chamando o publisher
#     def __init__(self):
#         rclpy.init()
#         self.node = rclpy.create_node('turtle_controller')
#         self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
#         self.movements = deque()

#     def move_turtle(self, vx, vy, vtheta, duration): #mudando como quer receber as mensagens e os valores das variáveis
#         twist = Twist()
#         twist.linear.x = vx #mudando para vx para satisfazer a condição
#         twist.linear.y = vy #mudando para vy para satisfazer a condição
#         twist.angular.z = vtheta # vtheta para a condição
#         self.publisher.publish(twist) 
#         time.sleep(duration / 1000.0) #duração de 1 segundo para rodar o processo
#         self.stop_turtle() #chamando a função para parar a tartaruga a ponto dela processar o outro movimento adicionado na lista

#     def stop_turtle(self):
#         twist = Twist()
#         self.publisher.publish(twist) #parando a tartaruga

#     def destroy(self): #destruindo a tarturiga e o nó do ROS para matar tudo
#         self.node.destroy_node() 
#         rclpy.shutdown() 

#     def add_movement(self, vx, vy, vtheta, duration):
#         self.movements.append((vx, vy, vtheta, duration)) #adicionando os movimentos na lista como mostra na documentação
#         print(f"Movimento adicionado: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")

#     def process_movements(self):
#         print("Processando movimentos...")
#         while self.movements:
#             vx, vy, vtheta, duration = self.movements.popleft() #faz o deslocamento da fila toda e vai consumindo os valores
#             print(f"Executando movimento: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms") 
#             self.move_turtle(vx, vy, vtheta, duration) #chamando a função para mover a tartaruga e vazendo todos os movimentos adicionados
#         print("Todos os movimentos foram processados.")

# def main():
#     parser = argparse.ArgumentParser(description="Controle da Tartaruga Turtlesim")
#     parser.add_argument('--vx', type=float, default=0.0, help='Velocidade linear em x')
#     parser.add_argument('--vy', type=float, default=0.0, help='Velocidade linear em y')
#     parser.add_argument('--vt', type=float, default=0.0, help='Velocidade angular em torno do eixo z')
#     parser.add_argument('-t', '--time', type=int, default=1000, help='Tempo em milissegundos para executar o comando')
#     args = parser.parse_args()

#     controller = TurtleController()
    
#     # Adicionar movimento da linha de comando
#     if any([args.vx, args.vy, args.vt, args.time != 1000]):
#         controller.add_movement(args.vx, args.vy, args.vt, args.time)
#         controller.process_movements()
    
#     print("Modo interativo. Digite os comandos no formato: vx vy vtheta tempo_em_ms")
#     print("Digite 'processar' para executar os movimentos ou 'sair' para encerrar.")

#     while True:
#         command = input("Comando: ").strip().lower()
        
#         if command == 'sair':
#             break
#         elif command == 'processar':
#             controller.process_movements()
#         else:
#             try:
#                 vx, vy, vtheta, duration = map(float, command.split())
#                 controller.add_movement(vx, vy, vtheta, int(duration))
#             except ValueError:
#                 print("Comando inválido! Use o formato: vx vy vtheta tempo_em_ms")

#     controller.destroy()

# if __name__ == '__main__':
#     main()


# import rclpy
# from geometry_msgs.msg import Twist
# import time
# from collections import deque
# import argparse

# class TurtleController:
#     def __init__(self):
#         rclpy.init()
#         self.node = rclpy.create_node('turtle_controller')
#         self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
#         self.movements = deque()

#     def move_turtle(self, vx, vy, vtheta, duration):
#         twist = Twist()
#         twist.linear.x = vx
#         twist.linear.y = vy
#         twist.angular.z = vtheta
#         self.publisher.publish(twist)
#         time.sleep(duration / 1000.0)
#         self.stop_turtle()

#     def stop_turtle(self):
#         self.publisher.publish(Twist())

#     def destroy(self):
#         self.node.destroy_node()
#         rclpy.shutdown()


#     #parte nova feita e consultando a documentação
#     def add_movement(self, vx, vy, vtheta, duration):
#         self.movements.append((vx, vy, vtheta, duration))
#         print(f"Movimento adicionado: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")

#     def process_movements(self):
#         print("Processando movimentos...")
#         while self.movements:
#             vx, vy, vtheta, duration = self.movements.popleft()
#             print(f"Executando movimento: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")
#             self.move_turtle(vx, vy, vtheta, duration)
#         print("Todos os movimentos foram processados.")

# def main():
#     # parser = argparse.ArgumentParser(description="Controle da Tartaruga Turtlesim")
#     # parser.add_argument('--vx', type=float, default=0.0, help='Velocidade linear em x')
#     # parser.add_argument('--vy', type=float, default=0.0, help='Velocidade linear em y')
#     # parser.add_argument('--vt', type=float, default=0.0, help='Velocidade angular em torno do eixo z')
#     # parser.add_argument('-t', '--time', type=int, default=1000, help='Tempo em milissegundos para executar o comando')
#     # args = parser.parse_args()

#     controller = TurtleController()
    
#     if any([vx, vy, vtheta, duration != 1000]):
#         controller.add_movement(vx, vy, vtheta, int(duration))
#         controller.process_movements()
    
#     print("Digite os comandos no formato: vx(0.0),  vy(0.0) vtheta(0.0) tempo_em_ms(0000)")
#     print("Digite 'vai' para executar os movimentos") 
#     print("Digite 'flw' para encerrar o processo.")

#     while True:
#         command = input("Comando: ").strip().lower()
        
#         if command == 'flw':
#             break
#         elif command == 'vai':
#             controller.process_movements()
#         else:
#             try:
#                 vx, vy, vtheta, duration = map(float, command.split())
#                 controller.add_movement(vx, vy, vtheta, int(duration))
#             except ValueError:
#                 print("Comando inválido! Use o formato: vx vy vtheta tempo_em_ms")

#     controller.destroy()

# if __name__ == '__main__':
#     main()

import rclpy
from geometry_msgs.msg import Twist
import time
from collections import deque

class TurtleController:
    def __init__(self):
        rclpy.init()
        self.node = rclpy.create_node('turtle_controller')
        self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.movements = deque()

    def move_turtle(self, vx, vy, vtheta, duration):
        twist = Twist()
        twist.linear.x = vx
        twist.linear.y = vy
        twist.angular.z = vtheta
        self.publisher.publish(twist)
        time.sleep(duration / 1000.0)
        self.stop_turtle()

    def stop_turtle(self):
        self.publisher.publish(Twist())

    def destroy(self):
        self.node.destroy_node()
        rclpy.shutdown()

    def add_movement(self, vx, vy, vtheta, duration):
        self.movements.append((vx, vy, vtheta, duration))
        print(f"Movimento adicionado: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")

    def process_movements(self):
        print("Processando movimentos...")
        while self.movements:
            vx, vy, vtheta, duration = self.movements.popleft()
            print(f"Executando movimento: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")
            self.move_turtle(vx, vy, vtheta, duration)
        print("Todos os movimentos foram processados.")

def main():
    controller = TurtleController()

    print("Modo interativo. Digite os comandos no formato: vx vy vtheta tempo_em_ms")
    print("Digite 'processar' para executar os movimentos ou 'sair' para encerrar.")

    while True:
        command = input("Comando: ").strip().lower()
        
        if command == 'sair':
            break
        elif command == 'processar':
            controller.process_movements()
        else:
            try:
                vx, vy, vtheta, duration = map(float, command.split())
                controller.add_movement(vx, vy, vtheta, int(duration))
            except ValueError:
                print("Comando inválido! Use o formato: vx vy vtheta tempo_em_ms")

    controller.destroy()

if __name__ == '__main__':
    main()



# import rclpy
# from geometry_msgs.msg import Twist
# import time
# from collections import deque

# class TurtleController:
#     def __init__(self):
#         rclpy.init()
#         self.node = rclpy.create_node('turtle_controller')
#         self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 4)
#         self.movements = deque()

#     def move_turtle(self, linear, angular):
#         twist = Twist()
#         twist.linear.x = linear
#         twist.angular.z = angular
#         self.publisher.publish(twist)

#     def destroy(self):
#         self.node.destroy_node()
#         rclpy.shutdown()

#     def add_movement(self, linear, angular):
#         self.movements.append((linear, angular))

#     def process_movements(self):
#         while self.movements:
#             linear, angular = self.movements.popleft()
#             self.move_turtle(linear, angular)
#             time.sleep(1)  # Ajuste o tempo conforme necessário

# def main():
#     controller = TurtleController()

#     print("Controle da Tartaruga Turtlesim")
#     print("Digite 'socorro' para parar a tartaruga")
#     print("Adicione as movimentações que você quiser para ele fazer")
#     print("Digite 'frente', 'trás', 'esquerda', 'direita', 'processar' ou 'sair' e pressione Enter para mover a tartaruga.")
    
#     while True:
#         command = input("Comando: ").lower()

#         if command == 'sair':
#             break
#         elif command == 'frente':
#             controller.add_movement(2.0, 0.0)
#         elif command == 'trás':
#             controller.add_movement(-2.0, 0.0)
#         elif command == 'esquerda':
#             controller.add_movement(0.0, 1.56)
#         elif command == 'direita':
#             controller.add_movement(0.0, -1.56)
#         elif command == 'socorro':
#             controller.add_movement(0.0, 0.0)
#         elif command == 'processar':
#             controller.process_movements()
#         else:
#             print("Comando inválido! Use 'frente', 'trás', 'esquerda', 'direita', 'processar' ou 'sair'.")

#     controller.destroy()

# if __name__ == '__main__':
#     main()


#!/usr/bin/env python3
# import rclpy
# from geometry_msgs.msg import Twist
# import time
# from inquirer import prompt

# class TurtleController:
#     def __init__(self):
#         rclpy.init()
#         self.node = rclpy.create_node('turtle_controller')
#         self.publisher = self.node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

#     def move_turtle(self, linear, angular):
#         twist = Twist()
#         twist.linear.x = linear
#         twist.angular.z = angular
#         self.publisher.publish(twist)

#     def destroy(self):
#         self.node.destroy_node()
#         rclpy.shutdown()

# def main():
#     controller = TurtleController()

#     print("Controle da Tartaruga Turtlesim")

#     while True:
#         questions = [
#             {
#                 'type': 'list',
#                 'name': 'command',
#                 'message': 'Selecione uma ação:',
#                 'choices': [
#                     'Frente',
#                     'Trás',
#                     'Esquerda',
#                     'Direita',
#                     'Sair'
#                 ]
#             }
#         ]

#         answer = prompt(questions, raise_keyboard_interrupt=True)  

#         command = answer['command'].lower()

#         if command == 'sair':
#             break
#         elif command == 'frente':
#             controller.move_turtle(2.0, 0.0)
#         elif command == 'trás':
#             controller.move_turtle(-2.0, 0.0)
#         elif command == 'esquerda':
#             controller.move_turtle(0.0, 1.56)
#         elif command == 'direita':
#             controller.move_turtle(0.0, -1.56)

#     controller.destroy()

# if __name__ == '__main__':
#     main()
