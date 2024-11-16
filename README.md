# Análisis de Sentimientos de Tweets

Este proyecto permite recolectar tweets de Twitter en tiempo real, analizarlos para determinar el sentimiento (positivo, negativo o neutral) utilizando `TextBlob`, y almacenarlos en una base de datos MySQL. Posteriormente, se visualizan los datos recopilados en una aplicación web interactiva desarrollada con Dash, que muestra los resultados de los sentimientos a través de gráficos dinámicos.

## Descripción

Este repositorio contiene dos partes principales:
1. **Recolección de Tweets**: Utiliza la API de Twitter v2 para buscar tweets basados en una palabra clave, realiza un análisis de sentimientos sobre cada tweet utilizando `TextBlob`, y almacena los resultados en una base de datos MySQL.
2. **Visualización de Sentimientos**: Una aplicación web construida con Dash que se conecta a la base de datos MySQL para mostrar un análisis visual de los sentimientos a través de gráficos interactivos.

## Requisitos

Antes de ejecutar este proyecto, asegurar tener instalado lo siguiente:

- **MySQL** (o cualquier otro gestor de base de datos compatible con MySQL)
- **Bibliotecas de Python**: Puedes instalar las dependencias necesarias 
  pip install -r requirements.txt

Las bibliotecas necesarias son:

    - tweepy para interactuar con la API de Twitter
    - textblob para el análisis de sentimientos
    - mysql-connector-python para la conexión a MySQL
    - dash para crear la aplicación web interactiva
    - pandas para manipulación de datos
    - plotly para la visualización de los gráficos
    - dotenv para cargar las credenciales de manera segura

## Instalación

    Configurar entorno:
        Crear un archivo .env en la raíz del proyecto y agregar las siguientes variables de entorno:

    API_KEY=KEY
    API_SECRET_KEY=SECRET_KEY
    BEARER_TOKEN=BEARER_TOKEN
    ACCESS_TOKEN=TOKEN
    ACCESS_TOKEN_SECRET=TOKEN_SECRET
    DB_HOST=localhost
    DB_USER=nombre de usuario
    DB_PASSWORD=contraseña de MySQL
    DB_NAME=nombre de la base de datos

    Nota: Asegurnos de reemplazar los valores con los credenciales reales de Twitter y MySQL.

- Crear la base de datos y la tabla de tweets: Conectarnos a la base de datos MySQL y creat la siguiente tabla para almacenar los tweets:

CREATE TABLE tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255),
    text TEXT,
    sentiment VARCHAR(50),
    created_at DATETIME
);

- Ejecutar el script para recolectar tweets: Ejecutar recoleccion.py para comenzar a recolectar tweets con la palabra clave que seleccionemos y almacenarlos en la base de datos:

    - El script pedirá una palabra clave para buscar tweets en Twitter. Los tweets recolectados serán analizados para determinar su sentimiento y luego almacenados en la base de datos.

- Ejecutar la aplicación Dash: Una vez que se hayan recolectado algunos tweets, ejecutar la aplicación web de Dash para visualizar los resultados:

    1. La aplicación se abrirá en el navegador y mostrará dos gráficos:
        - Distribución de Sentimientos: Un gráfico de pastel que muestra la proporción de tweets positivos, negativos y neutrales.
        - Sentimientos a lo largo del tiempo: Un histograma que muestra cómo han cambiado los sentimientos de los tweets a lo largo del tiempo.

    Además, se pueden filtrar los resultados por un rango de fechas utilizando el selector de fechas en la parte superior de la página.

## Uso

1. Recolectar Tweets: Ejecutar recoleccion.py con la palabra clave deseada. Este script recolectará hasta 30 tweets relacionados con esa palabra clave.
2. Visualizar Resultados: Ejecutar app.py para visualizar los resultados en la aplicación web de Dash.

## Estructura del Proyecto

.
├── app.py               # Aplicación web con Dash para visualización de los resultados
├── recoleccion.py       # Script para recolectar tweets y analizarlos
├── .env                 # Archivos de configuración para las credenciales de Twitter y base de datos
├── requirements.txt     # Lista de dependencias de Python
└── .gitignore           # Archivos y carpetas a ignorar por Git (incluye .env)



### Explicación del contenido:

- **Descripción**: Un resumen claro de lo que hace el proyecto.
- **Requisitos**: Lista de los requisitos para ejecutar el proyecto.
- **Instalación**: Explicación paso a paso de cómo instalar y configurar el entorno de trabajo, incluyendo las credenciales necesarias.
- **Uso**: Explicación de cómo ejecutar y utilizar los scripts.
- **Estructura del proyecto**: Una visión general de la estructura de los archivos y lo que contiene cada uno.