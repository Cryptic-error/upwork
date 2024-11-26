import requests

# expression for values in iterable and if condition 

def fetchjson(url):
    response = requests.get(url)
    return response.json()


def extracttitle(url):
    data = fetchjson(url)

    tittle = [item["title"] for item in data if isinstance(item.get("title"),str) and "qui" in item["title"]]
    print(f"these are tittle :{tittle}")

    for tittlee in tittle:
        if tittlee == int:
            print(f"{tittle} is interger ")
        
        print("no integers")
        










url = "https://jsonplaceholder.typicode.com/todos"
# print(fetchjson(url))
print(extracttitle(url))