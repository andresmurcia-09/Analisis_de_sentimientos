import tweepy
import mysql.connector
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # Importar VADER
from langdetect import detect
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de Twitter desde las variables de entorno
bearer_token = os.getenv("BEARER_TOKEN")

# Configuración de la API de Twitter (usando la API v2)
client = tweepy.Client(bearer_token=bearer_token)

# Obtener las credenciales de la base de datos desde las variables de entorno
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Conexión a MySQL
connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = connection.cursor()

# Función para guardar tweets en la base de datos
def guardar_tweet(user, text, sentiment, created_at):
    cursor.execute(
        "INSERT INTO tweets (user, text, sentiment, created_at) VALUES (%s, %s, %s, %s)",
        (user, text, sentiment, created_at)
    )
    connection.commit()

# Función de análisis de sentimientos usando VADER
def analizar_sentimiento(texto):
    try:
        analyzer = SentimentIntensityAnalyzer()  # Crear instancia del analizador VADER
        # Obtener los puntajes de polaridad
        score = analyzer.polarity_scores(texto)
        
        # VADER devuelve un diccionario con los puntajes 'neg', 'neu', 'pos', y 'compound'
        if score['compound'] > 0.05:
            return "Positivo"
        elif score['compound'] < -0.05:
            return "Negativo"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error en el análisis de sentimiento: {e}")
        return "Neutral"  # Devolver Neutral en caso de error

# Función para recolectar tweets de Twitter
def recolectar_tweets(keyword, cantidad=30):
    try:
        response = client.search_recent_tweets(query=keyword, max_results=cantidad, tweet_fields=["created_at", "text", "author_id"])
        
        for tweet in response.data:
            user = tweet.author_id
            text = tweet.text
            created_at = tweet.created_at
            sentiment = analizar_sentimiento(text)
            guardar_tweet(user, text, sentiment, created_at)
    except tweepy.TweepyException as e:
        print(f"Error en la API de Twitter: {e}")

# Ejecutar la recolección de tweets
if __name__ == "__main__":
    palabra_clave = input("Introduce la palabra clave para buscar tweets: ")
    recolectar_tweets(palabra_clave)
    print("Recolección completada.")
    connection.close()
