from pymongo import MongoClient

# Substitua pelos dados reais do seu cluster MongoDB Atlas
MONGO_URL = "mongodb+srv://silvaisadora2504:<db_password>@cluster0.1ciz6fp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URL)
db = client["adocao_pets"]
