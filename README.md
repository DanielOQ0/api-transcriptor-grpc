
# API TRANSCRIPTOR GRPC
La siguiente api permite la transmision de datos de audio desde un cliente para consumir el microservicio de whisper.



## API Referencia

#### Envio de fragmento de datos de audio en chunk de bytes

```http
  GRPC rpc RouteStreamAudio
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `usuario` | `string` | **Requerido**. Nombre del usuario que realiza la conexion |
| `audio_chunk` | `bytes` | **Requerido**. Chunk de bytes del audio |
| `frecuencia` | `number` | **Requerido**. Frecuencia de muestreo del audio |



## Instalacion

Tener instalado al menos python 3.10.12

Clonar el proyecto con 

```bash
  git clone https://danielorozco@172.16.19.36/proyectosespeciales/api-transcriptor-grpc.git
  cd api-transcriptor-grpc
```
Si desea instalar en entorno virtual
```bash
  python -m venv nombre_env
  .\nombre_env\Scripts\activate
  python -m pip install grpcio grpcio-tools
```
En caso contrario instalar librerias solamente
```bash
  python -m pip install grpcio grpcio-tools
```
## Despliegue

Para desplegar este proyecto ejecute

```bash
  python index.py
```