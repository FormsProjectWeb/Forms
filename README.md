# Forms
## Navegación
### Página Principal
```console
/
```
Contiene el apartado para preguntar a la inteligencia artifical o a una persona que esté en el apartado de respuesta
### Respuesta Manual
```console
/Answer/
```
Contiene el apartado para responder las preguntas publicadas a través de FastMessage (https://f-mssg.web.app/)
### Referencias
```console
/Reference/
```
Contiene el apartado para configurar las referencias (materia y temas) de los cuales se va a preguntar
## Instrucciones de despliegue
### Requisitos previos
1. [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) instalado y configurado con la cuenta de Google.
2. Permisos adecuados en el proyecto de GCP para crear instancias y reglas de firewall.
3. Una terminal de Cloud Shell (GCP)
### Pasos para el despliegue
#### 1. Clonar el repositorio
```console
git clone https://github.com/FormsProjectWeb/Forms.git
```
#### 2. Cambiar al directorio del proyecto
```console
cd Forms
```
#### 3. Permisos de despliegue
```console
sudo chmod +x Deployment/deployment.sh
```
#### 4. Ejecutar Script de despliegue
```console
Deployment/deployment.sh
```
### Eliminar proyecto
```console
gcloud deployment-manager deployments delete form-deployment
```
### Ver procesos en segundo plano
```console
ps -ef | grep python
```
### Quitar procesos en segundo plano
```console
sudo kill 
```
seguido del id del proceso

## Error por permisos de la base de datos
Estando en el directorio de la aplicación, se deben ejecutar los siguientes comandos
```console
sudo chmod +w db.sqlite3
sudo chmod +w .
sudo chmod 666 .
```
Despues se debe reiniciar el servidor, para eso se necesita quitar el proceso de runserver de segundo plano (sección anterior) y ejecutar nuevamente el comando
```console
sudo python3 manage.py runserver 0.0.0.0:8000
```
