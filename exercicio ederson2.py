class Quadrado:
    def __init__(self, lado):
       
        self.lado = lado

    def mostrar_area(self):
    
        area = self.lado ** 2
        return area

    def mudar_valor_lado(self, novo_lado):
        
        self.lado = novo_lado
        return self.lado, self.mostrar_area()


quadrado = Quadrado(4) 
print(f"Área inicial: {quadrado.mostrar_area()}") 


lado, area = quadrado.mudar_valor_lado(6)
print(f"Novo lado: {lado}, Nova área: {area}")
