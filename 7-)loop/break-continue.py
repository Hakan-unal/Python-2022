name="ali veli"

for char in name:
    if(char=="v"):
        print(char)
    if(char=="a"):continue
    if(char=="e"):break

    print(char)


index=0
result=0

while(index<100):
    if(index%2==0):result+=index
    index+=1

print(result)