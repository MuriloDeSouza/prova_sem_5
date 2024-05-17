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

    def move_turtle(self, vx, vy, vtheta, duration): #colocando as variáveis para o movimento como foi pedido
        twist = Twist()
        twist.linear.x = vx 
        twist.linear.y = vy
        twist.angular.z = vtheta
        self.publisher.publish(twist)
        time.sleep(duration / 1000.0)
        self.stop_turtle()

    def stop_turtle(self): # aquui é para parar o movimento da tarturiga
        self.publisher.publish(Twist())

    def destroy(self): # para encerrar o nó e matar mesmo a tarturiga
        self.node.destroy_node()
        rclpy.shutdown()

    def add_movement(self, vx, vy, vtheta, duration): #adicionando movimento para poder fazer a tarturiga se mover
        self.movements.append((vx, vy, vtheta, duration))
        print(f"Movimento adicionado: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")

    def process_movements(self): #acumula os movimentos e ai vai percorrendo a fila
        print("Processando movimentos...")
        while self.movements:
            vx, vy, vtheta, duration = self.movements.popleft()
            print(f"Executando movimento: vx={vx}, vy={vy}, vtheta={vtheta}, duração={duration}ms")
            self.move_turtle(vx, vy, vtheta, duration)
        print("Todos os movimentos foram processados.")

def main():
    controller = TurtleController()

    print("Digite os comandos no formato: vx(0.0) vy(0.0) vtheta(0.0) tempo_em_ms(1000)")
    print("Digite 'vai' para executar os movimentos")
    print("Digite 'sair' para encerrrar tudo")

    while True:
        command = input("Comando: ").strip().lower()
        
        if command == 'sair':
            break
        elif command == 'vai':
            controller.process_movements()
        else: #validando o comando se ta da maneira correta como foi pedido
            try:
                vx, vy, vtheta, duration = map(float, command.split())
                controller.add_movement(vx, vy, vtheta, int(duration))
            except ValueError:
                print("Comando inválido! Use o formato: vx vy vtheta tempo_em_ms")

    controller.destroy()

if __name__ == '__main__':
    main()



