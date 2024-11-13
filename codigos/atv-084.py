def formato_12h_para_24h(hora_12h):
    hora, minuto_periodo = hora_12h.split(":")
    minuto, periodo = minuto_periodo[:2], minuto_periodo[3:]
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