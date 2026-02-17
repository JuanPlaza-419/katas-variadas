def sumatoria (numbers: str) -> int:
    if not numbers:
        return 0
    
    partes = numbers.split(",")
    return sum(int(n.strip()) for n in partes)