import pandas as pd

data = pd.DataFrame({
        "name":["priti","none","None"],
        "hobbies":["sketching","painting","writing"],
        "skills":["python","sql","dsa"],
        "techStacks":['nodejs','express js','postman'],
        "marks" :[10,30,50]
        })
print(data["name"])
print(data["hobbies"])
print(data["skills"])
print(data["techStacks"])
print(data["marks"] >20 )