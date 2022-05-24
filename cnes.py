import csv
import pymongo

client = pymongo.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.f0tqt.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client["dbname"]

#for x in db.users.find():
#    print(x)

key_list = ["cnes","uf","ibge","nome","logradouro","bairro","latitude","longitude"]



filename = 'cadastro_estabelecimentos_cnes.csv'
x = 0
with open(filename) as f:
 csv = csv.reader(f, delimiter=";", quotechar='"')
 next(csv)
 for row in csv:
    x = x + 1
    dict_from_list = dict(zip(key_list, row))
    print(f"{x}\r", end = "")
    db.users.insert_one(dict_from_list)
    #if x > 1:
    #  break

