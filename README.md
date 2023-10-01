# Componente sesión, Arquitecturas agiles, Experimento Seguridad.
​
En este servicio se van a utilizar las tácticas de autenticación y autorización, utilizando los jwt tokens para este fin.​

## Como configurar el ambiente
# clonar el repositorio de abc-jobs-gateway-seguridad
        https://github.com/tom-uniandes/abc-jobs-gateway-seguridad

    abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de evaluacion

### ejecutar el comando 
        docker network create abc-network-seguridad

### ejecutar el comando
         docker build -t gateway-seguridad .

### ejecutar el comando
        docker run --network=abc-network-seguridad --name gateway-seguridad -p 5005:5005 gateway-seguridad

### En otra consola de comandos ejecutar el siguiente comando
        docker start gateway-seguridad

# clonar el repositorio de abc-jobs-oferta
        https://github.com/leinaro/abc-jobs-oferta

### abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de abc-jobs-oferta
         docker build -t oferta .

### ejecutar el comando
        docker run --network=abc-network-seguridad --name oferta -p 5002:5002 oferta

### En otra consola de comandos ejecutar el siguiente comando
        docker start oferta

# clonar el repositorio de abc-sesion
        https://github.com/leinaro/abc-sesion

### abrir una consola de comandos en la carpeta y ubicarse en la que se descargó el repositorio de abc-sesion
         docker build -t sesion .

### ejecutar el comando
        docker run --network=abc-network-seguridad --name sesion -p 5003:5003 sesion

### En otra consola de comandos ejecutar el siguiente comando
        docker start sesion

## instalar k6 
    tutorial + instaladores para otros sistemas operativos
        https://k6.io/docs/es/empezando/instalacion/

  ###  instalador para windows
        https://dl.k6.io/msi/k6-latest-amd64.msi


## En otra consola de comandos ejecutar los siguientes comandos
### Escenario 1
     k6 run scriptExperimento2.js --out json=Experimento2.json --out csv=Experimento2.csv --log-output=file=Experimento2.log


### Escenario 2
     k6 run scriptCandidatoExperimento2.js --out json=Experimento2.json --out csv=Experimento2.csv --log-output=file=Experimento2.log


### Escenario 3
     k6 run scriptCandidatoTokenModificado.js --out json=Experimento2.json --out csv=Experimento2.csv --log-output=file=Experimento2.log
