# Introducción
La agencia espacial te ha encargado el software de navegación del nuevo Rover. En esta fase, el objetivo es establecer la comunicación básica: que el robot entienda dónde está y cómo girar o avanzar.

# Iteracion 1
## Entidades Iniciales
Para esta primera iteración, trabajarás principalmente con dos conceptos:
### El Rover: Un objeto que mantiene su estado (X, Y, Dirección).
### Los Comandos: Una secuencia de letras que el Rover debe procesar.
Movimiento y Rotación en Plano Infinito
En esta etapa, Marte es un plano infinito (sin bordes). El Rover debe procesar comandos simples: f (adelante), b (atrás), l (izquierda) y r (derecha).

Posicion inicial va a ser 0,0,N


## Tests
### test1: Variar dirección 
    cuando reciba l o r no se mueva de casilla si no que solo gire 90º ej:
    instrucción:  "l"
    posición final: 0,0,W
### test2: Comandos invalidos
    Cuando reciba un comando que no esta permitido que devuelva una excepción.
    Comandos validos: "f (adelante), b (atrás), l (izquierda) y r (derecha)."
### test3: Posición inicial
    Cuando inicias este siempre en la posicion 0,0,N
### test4: Comando f mueve posicion adelante
    cuando reciba f se mueva una casilla adelante:
    posicion inicial: 0,0,N
    instrucción:  "f"
    posición final: 0,1,N
### test5: Comando b mueve posicion atras
    cuando reciba b se mueva una casilla atras:
    posicion inicial: 0,1,N
    instrucción:  "b"
    posición final: 0,0,N