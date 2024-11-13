def media_notas(dicionario):
    total_notas = sum(dicionario.values())  
    quantidade_alunos = len(dicionario)     
    if quantidade_alunos == 0:              
        return 0
    media = total_notas / quantidade_alunos  
    return media
notas_alunos = {
    "Mariah": 8.5,
    "Wescley": 7.0,
    "Carlos": 9.0,
    "Camila": 6.5
}
print(media_notas(notas_alunos))  