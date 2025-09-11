def ordenar_batallas(tiempos, importancias):
    n = len(tiempos)
    batallas = []
    
    for i in range(n):
        ratio = importancias[i] / tiempos[i]
        batallas.append((i + 1, tiempos[i], importancias[i], ratio))
    
    batallas.sort(key=lambda x: x[3], reverse=True)
    return batallas

# print(ordenar_batallas([3, 1, 2], [5, 10, 15]))
