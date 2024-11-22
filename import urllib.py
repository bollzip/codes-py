import urllib.parse
import urllib.request


url = 'https://pt.wikipedia.org/wiki/John_Lennon'
parsed_url = urllib.parse.urlparse(url)

print("Componentes da URL:")
print("Esquema:", parsed_url.scheme) 
print("Domínio:", parsed_url.netloc)  
print("Caminho:", parsed_url.path)    
print("Consulta:", parsed_url.query)  


response = urllib.request.urlopen(url)
content = response.read()


print("\nConteúdo da página (primeiros 5000 caracteres):")
print(content[:5000].decode())