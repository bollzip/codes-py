class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def celsius_para_fahrenheit(self):
       
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit


temperatura = Temperatura(25)  


fahrenheit = temperatura.celsius_para_fahrenheit()
print(f"{temperatura.celsius}°C é igual a {fahrenheit}°F")
