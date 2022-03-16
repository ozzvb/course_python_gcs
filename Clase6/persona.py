class Persona :
    color_pelo = "negro"
    color_ojos = "negro"
    
print( type(Persona) )

osvaldo=Persona();
osvaldo.color_ojos="cafe"
osvaldo.color_pelo="castaño"

print( osvaldo.color_pelo )


#////////////////////////////////////////////////////////////////

class Persona2 :
    def __init__( self, color_pelo= "rubio", color_ojos = "azul" ) :
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos
        
mario=Persona2("rubio","cafe");
luciana=Persona2("negro","verdes");

class Persona3 :
    def __init__( self, color_pelo= "negro", color_ojos="negro") :
        self.color_pelo = color_pelo
        self.color_ojos = color_ojos
    def __repr__( self ) :
        return("Ojos: "+self.color_ojos+" ,Perlo: "+self.color_ojos)
    
carlos=Persona3("azul","azul")

print(carlos)

#////////////////////////////////////////////////////////////////

