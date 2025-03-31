# Lab_2

Este reporte documenta toda la seria

## 1. Inicialización de roscore:

Se inicia el master de ROS, `roscore`, en una terminal.  Este proceso es fundamental para la comunicación entre los nodos ROS, también es importante destacar que gracias a pasos previos en otras sesiones de laboratorio, se pudo generar un workspace con las dependencias de rospy, roscpp y srd_msgs. Al mismo tiempo, el proceso de bash ya no es necesario, pues se editó en el mismo laboratorio para poder evadir este paso.

## 2.  Archivos listener.py y talker.py

Para la parte básica de este reporte, es necesario colocar los archivos listener y talker para que se comunicen dos nodos distintos de ros, para ello, después de la creación de los paquetes respectivos, se siguen las siguientes líneas de código (figura 1):

![Figura 1. Listener_talker_code](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/creating_listener_and_talker.png)

Después de haber creado estos dos archivos de python, se ejecuta primero el archivo Python de nombre `talker.py` y en una tercera terminal `listener.py` de forma que ambos nodos ahora se encuentran comunicándose entre ellos (figura 2):

![Figura 2. Listener and talker communicating](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/listener_chatter_functioning.png)

Es posible con el comando `rqt_graph` poder identificar de una forma visual y gráfica la comunicación entre ambos nodos:

![Figura 3. rqt graph](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/rqtgraph.png)

A través de este ejercicio simple e introductorio, podemos concluir que el funcionamiento de estos elementos es aquel de comunicar dos nodos distintos de ROS, y si bien era información aleatoria la que se transmitiía con el `talker`, será conocimiento esencial para que distintos nodos de robots y proyectos futuros

# 3. Turtlesim (control por teclado)

Teniendo en cuenta el conocimiento adquirido de los nodos y la comunicación que puede existir entre estos, para la siguiente sección requeriremos de `turtlesim` con sus bibliotecas y comandos. Comenzando con el primer paso mencionado anteriormente, el cuál es inicializar `roscore` en una terminal y abrir otras tres terminales, una para inicializar la tortuga con `rosrun turtlesim turtlesim_node`, otra para poder controlar la tortuga con el teclado con el comando `rosrun turtlesim turtlesim_teleop_key`, y una última terminal para poder visualizar las coordenadas de la tortuga, las siguientes dos figuras muestran las terminales utilizadas y la gráfica de la tortuga respectivamente:

![Figura 4. Consola de turtlesim](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/turtlesimkey.png)
![Figura 5. Tortuga](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/turtleshowing.png)

# 4. Creación de dibujos con turtlesim

Una vez se entendió el funcionamiento de las distintas terminales para turtlesim, es posible generar un código que permita a la tortuga generar dos figuras distintas, en el caso de este laboratorio se exigió hacer un cuadrado y un triángulo equilátero sin hacer uso del controlador de teclado de la sección pasada. Esto se podrá conseguir con un código de Python sencillo que mueva la tortuga a las coordenadas deseadas, dichos códigos pueden ser consultados en la carpeta `src` de esta práctica. Sin embargo, una explicación básica es la de hacer uso de las bibliotecas de turtlesim, en la que usamos la función `t.goto(x,y)` y en los paréntesis se incluyen las coordenadas deseadas a dónde la tortuga debe llegar para formar las figuras, asimismo, se presentan los resultados de ambos códigos:









