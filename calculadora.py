def sumatoria(numbers: str) -> int:
    if not numbers:
        return 0
    
    data = numbers.replace("\n", ",").replace("\\n", ",")
    
    partes = data.split(",")
    
    return sum(int(n.strip()) for n in partes if n.strip())