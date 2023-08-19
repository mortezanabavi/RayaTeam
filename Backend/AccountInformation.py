data = {
    "name":"reza",
    "family":"rezaei",
    "social":{
        "instagram":{
            "fake":["ali123","peykan"],
            "real":["rezaei"]
        },
        "telegram":"rezaei_reza",
        "twitter":"loser_user"
    }
}


print("Instagram :",data["social"]["instagram"]["real"][0])
print("Real :", len(data["social"]["instagram"]["real"]), "Fake :", len(data["social"]["instagram"]["fake"]))
print("Telegram :",data["social"]["telegram"])
print("Twitter :",data["social"]["twitter"])