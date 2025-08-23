club = {"Music Club":{(100 , "Rachel"), (101 , "Pheobe") , (201, "Chandler")}, "Dance Club" : {(200, "Joy"),  (201, "Chandler"), (100 , "Rachel")} , "Sports Club":{(300, "Rose"), (301, "Gunther")}}
print(club)
club["Arts Club"] = {(400, "Miya"), (401 , "Maya")}
print(club)
club["Dance Club"].remove((200, "Joy"))
print("AFTER REMOVED A STUDENT FROM CLUB",club)
club["Dance Club"].add((203, "Emma"))
print("AFTER ADD STUDENT FROM CLUB",club)
Common_members = club["Music Club"].intersection(club["Dance Club"])
print(Common_members)
unique_members = club["Music Club"].symmetric_difference(club["Dance Club"])
print(unique_members)
print("Club names and their Member Count")
for clubname , members in club.items():
    print(clubname ,":", len(members))
    print("Thats all ")
    club = [
    ("Acting_club" , {(101, "Mohanlal"), (102, "Mammotty"), (103, "PrithviRaj")}),
    ("Direct_club", {(101, "Mohanlal"), (102, "Laljose"), (103, "PrithviRaj")}),
    ("Singing_club" , {(301, "K.J. Yesudas"), (302 , "K.S. Chithra")})
]

print(club)

club = dict(club)


club["Acting_club"].add((104, "Fahad"))

print(club["Acting_club"])

club["Acting_club"].remove((104, "Fahad"))
print(club["Acting_club"])


club["Dance_club"] = {(401, "Prabhu Deva"), (402, "Remo D'Souza")}

print(club)

common_members = club["Acting_club"] & club["Direct_club"]
print(common_members)


unique_members = club["Acting_club"] ^ club["Direct_club"]
print(unique_members)


print("All clubs and their member counts:")
for cname, members in club.items():
    print(f"{cname}: {len(members)} ")