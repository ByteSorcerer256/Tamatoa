from typing import List
import requests, json

#Class representing repositories
class Repo():
    
    #Constructor defines:
    #url: URL to repo
    #name: repo name
    #descripton: repo desc
    #owner: repo owner
    def __init__(self, url:str, name:str, description:str, owner:str):
        self.__url=url
        self.__name=name
        self.__description=description
        self.__owner=owner

    #Getters for url, name, description, owner  
    def get_url(self)->str:
        return self.__url

    def get_name(self)->str:
        return self.__name

    def get_description(self)->str:
        return self.__description

    def get_owner(self)->str:
        return self.__owner

#Class representing remote repositories storages
class Storage():

    #A method that searches for repositories that satisfy a query 
    def search(self, query:str)->List[Repo]:
        pass

#############SPECIFIC STORAGES#############

#Class representing Github storage
class Github(Storage):

    #Formattable Github search URL string
    __search_api_url = "https://api.github.com/search/repositories?q={query}"

    #Search method overriding
    #GET(url) and parsing JSON to Repo arr
    #Can return None
    def search(self, query:str)->List[Repo]:
        repos=[]
        url = self. __search_api_url.format(query=query)
        
        request = requests.get(url)
        json_response = json.loads(request.text)
        
        if (json_response["total_count"]==0):
            return None
        
        first_repos = json_response["items"][:5]
        for repo in first_repos:
            repos.append(Repo(repo["html_url"],
                              repo["name"],
                              repo["description"],
                              repo["owner"]["login"]))
        return repos
        
