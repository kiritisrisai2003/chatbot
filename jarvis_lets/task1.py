import requests
import socket
from config import key

def get_ip(host):
    try :
        result=socket.getaddrinfo("google.com",None)
    except Exception as e :
        print(e)
        result= f"error in find the IP,{e}"
    return result


def temp_room(room):
    result="temp =20, humidity 70"
    return result


def temp_city(city):
    url="https://yahoo-weather5.p.rapidapi.com/weather"
    querystring= {"location":city,"format":"json","u":"f"}
    headers={
        "X-RapidAPI-Key":"c32615b66cmsh4f1642869fcc6cbp11ddc9jsn5a9290a4ba18",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }
    response=requests.get(url,headers=headers,params=querystring)
    d1=response.json()
    #print(d1)
    d1=d1.get("current_observation")
    hum=d1.get('atmosphere').get("humidity")
    temp=d1.get('condition').get("temperature")
    temp=round((temp-32)*5/9,2)
    return (f"humidity:{hum},Temp in C:{temp}")
 
def chat1(chat):
    messages=[]
    
    system_message= f"Your are an AI bot,your name is jarvis.find the content related to query"
    message={"role" :"user", "parts" :[{"text":system_message+" "+chat}] }
    messages.append(message)
    data={"contents":messages}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response=requests.post(url,json=data)
    t1=response.json()
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")

    print(t2)
    return t2



definitions=[

           {
           "name":"chat1",
           "description":"hi hello ",
           "parameters":
              {
           "type":"object",
           "properties": {
               "chat":  {
                   "type":"string",
                   "description":"full query asked by user"
                   }
                       }
                }



            },













        
           {
           "name":"temp_city",
           "description":"find weather,temperature of a city",
           "parameters":
              {
           "type":"object",
           "properties": {
               "city":  {
                   "type":"string",
                   "description":"city to find weather"
                   }
                       }
                }



            },

              {
           "name":"temp_room",
           "description":"find weather,temperature of a city",
           "parameters":
           {
           "type":"object",
           "properties": {
               "room":  {
                   "type":"string",
                   "description":"room or home"
                   }
                       }
                }



            },
            
               
              
              {
           "name":"get_ip",
           "description":"find ip address of given url or domain name",
           "parameters":
           {
           "type":"object",
           "properties": {
               "host":  {
                   "type":"string",
                   "description":"get url or Domain name"
                   }
                       }
                }



            }   
              
            
             ]
 



if __name__=="__main__":
    print(temp_city("vijayawada"))
    