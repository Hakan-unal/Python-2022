# message="    bir berber bir berebere gel beraber bir berber dkkanı açalık demiş    "


# #https://www.w3schools.com/python/python_ref_string.asp

# sonuc=message.upper()
# sonuc=message.lower()
# sonuc=message.title()
# sonuc=message.capitalize()
# sonuc=message.islower()
# sonuc=message.isupper()
# sonuc=message.strip()
# sonuc=message.split()
# sonuc="-".join(sonuc)
# sonuc=message.replace("açalık","açalım").replace("dkkanı","dükkanı")


# print(sonuc)



#Uygulama

website="https://www.google.com"
name="bir Berber Bir berbere Gel beraber berber dükkanıı"
message=" Hello World "


print(message.strip())
print("www.google.com".strip("w.cm"))
print(name.lower())
print(name.count("a"))
print(website.startswith("www"))
print(website.endswith("com"))
print(website.find(".com"))
print(name.isalpha())
print(name.isdigit())
print("Contents".center(50,'*'))
print(name.replace(" ","-"))
print(message.replace("World","There"))
print(name.replace(" ",""))

print("Contents".ljust(50,'*'))
print("Contents".rjust(50,'*'))

