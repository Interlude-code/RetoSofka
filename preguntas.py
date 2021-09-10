import json

preguntas={
    "nivel1":{ 
        "Ciencia":[
            {"pregunta":"Numero atomico del hidrogeno","opt1":'1',"opt2":"2","opt3":"3","opt4":"4","respuesta":"opt1"}
        ],
        "Arte":[

        ],
        "Geografia":[

        ],
        "Deporte":[

        ],
        "Historia":[

        ]
    
    }


}
with open('preguntas.json','w')as jsonFile:
    json.dump(preguntas,jsonFile)
    jsonFile.close()