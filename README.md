# Workshop3-BD2

## Integrantes
### Juan Pablo Muñoz
### Raúl Gonzalez
### Jason Jossa
### Moisés Salcedo

Durante el desarrollo del proyecto decidimos hacer uso de pythoon y de algunas librerias como datetime, pymongo, redis y json. De forma que era mucho más fácil para nosotros crear los endpoints y las conexiones.

Durante el desarrollo de nuestro trabajo hemos creado lo siguiente:
### 1. Un API el cual era la encargada de recibir la información del json de Postman con la información requerida en el punto 1.
![image](https://user-images.githubusercontent.com/53981601/137246771-12dad20c-2cc0-482b-951c-267198f704d2.png)

![image](https://user-images.githubusercontent.com/53981601/137246728-3e98495d-a998-4bfa-b909-bee60ce39425.png)



### 2. Un método adicional donde se toma la información del json recibido y esto me llama a una función que se conecta a redis y guarda en redis la información de latitud y longitud

![image](https://user-images.githubusercontent.com/53981601/137246798-1009f3be-09d3-4272-a849-b90f6d4583a0.png)



### 3. Un método para mostrar las temperaturas que estén por fuera d erango para un animal dado

![image](https://user-images.githubusercontent.com/53981601/137246832-422e366f-5c83-4fe0-b20d-89af509a07b7.png)

 ![image](https://user-images.githubusercontent.com/53981601/137246686-4abc91aa-855f-491c-834a-c6145d12ac11.png)
