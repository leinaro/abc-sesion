# Componente sesión, Arquitecturas agiles, Experimento Seguridad.
​
En este servicio se van a utilizar las tácticas de autenticación y autorización, utilizando los jwt tokens para este fin.​

## Configuracion de Docker
1. Crear la network para los dos microservicios del experimento (correr solo una vez)

    ```bash
    docker network create abc-network-seguridad
    ```
2. Construir la imagen de docker 
    ```bash
     docker build -t sesion .
    ```
3. Crear y iniciar el container (correr solo una vez)
    ```bash
    docker run --network=abc-network-seguridad --name sesion -p 5003:5003 sesion
    ```
4. Iniciar el container de nuevo:
    ```bash
    docker start sesion
    ```
