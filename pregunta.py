import json
class Pregunta():
    def __init__(self,nivel,categoria,enunciado,opt1,opt2,opt3,opt4,correcta):
        self.nivel=nivel
        self.categoria=categoria
        self.enunciado=enunciado
        self.opt1=opt1
        self.opt2=opt2
        self.opt3=opt3
        self.opt4=opt4
        self.correcta=correcta  
   
    def __str__(self):
        ver= self.enunciado
        return ver



#preguntas={
#    "nivel1":{ 
#        "Ciencia":[
#            {"pregunta":"Numero atomico del hidrogeno","opt1":'1',"opt2":"2","opt3":"3","opt4":"4","respuesta":"opt1"}
#        ],
#        "Arte":[
#
#        ],
#        "Geografia":[
#
#        ],
#        "Deporte":[
#
#        ],
#        "Historia":[
#
#        ]
#    
#    }


#}
