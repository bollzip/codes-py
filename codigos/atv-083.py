def formato_12h_para_24h(hora_12h):
    hora, minuto, periodo = hora_12h[:-5], hora_12h[3:5], hora_12h[5:]
    hora = int(hora)
    minuto = int(minuto)
    if periodo == "AM":
        if hora == 12:
            hora = 0 
    elif periodo == "PM":
        if hora != 12:
            hora += 12 
    return f"{hora:02d}:{minuto:02d}"
hora_12h = "02:30 PM"
print(formato_12h_para_24h(hora_12h))  