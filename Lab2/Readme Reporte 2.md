# Lab_2

Este reporte documenta toda la seria

## 1. Inicialización de roscore:

Se inicia el master de ROS, `roscore`, en una terminal.  Este proceso es fundamental para la comunicación entre los nodos ROS, también es importante destacar que gracias a pasos previos en otras sesiones de laboratorio, se pudo generar un workspace con las dependencias de rospy, roscpp y srd_msgs. Al mismo tiempo, el proceso de bash ya no es necesario, pues se editó en el mismo laboratorio para poder evadir este paso.

## 2. Colocar archivos listener.py y talker.py

Para la parte básica de este reporte, es necesario colocar los archivos listener y talker para que se comunicen dos nodos distintos de ros, para ello, después de la creación de los paquetes respectivos, se siguen las siguientes líneas de código (figura 1):

![Figura 1. Listener_talker_code](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/creating_listener_and_talker.png)

Después de haber creado estos dos archivos de python, se ejecuta primero el archivo Python de nombre `talker.py` y en una tercera terminal `listener.py` de forma que ambos nodos ahora se encuentran comunicándose entre ellos (figura 2):

![Figura 2. Listener and talker communicating](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/listener_chatter_functioning.png)

Es posible con el comando `rqt_graph` poder identificar de una forma visual y gráfica la comunicación entre ambos nodos:

![Figura 3. rqt graph](https://github.com/LeonardoCarreraAngeles/Lab_LRT4102/blob/main/Lab2/Images/rqtgraph.png)





