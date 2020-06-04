import socketio
import random
import time 

# standard Python
sio = socketio.Client()
@sio.event
def connect():
    sio.emit('signin', {
    'user_name': 'Major Tom (Alexander Trujillo)',
    'tournament_id': 142857,
    'user_role': 'player'})
    print('connection established')

e = 0
@sio.on('ready')
def ready(server):
    movement = []
    game_id = server['game_id']
    player_turn_id = server['player_turn_id']
    game_finished = False
    typeLine = -1
    position = 0
    depth = 3

    def minimax(typeLine, position, depth):
        N = 6
        EMPTY = 99
        alpha= -1 #Valor para saber si se encuentra una situacion alpha
        beta = 1 #Valor para saber si se encuentra una situacion beta
        
        def max_(typeLine, position, alpha, depth):
            EMPTY = 99
            alpha= -1 #Valor para saber si se encuentra una situacion alpha
            beta = 1 #Valor para saber si se encuentra una situacion beta

            #cuando encuentra una linea 
            resultMAX2 = 0
            typeMAX2 = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMAX2 = 0
                        resultMAX2 = i + 1
                        alpha = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY:
                        typeMAX2 = 1
                        resultMAX2 = contador + acumulador
                        alpha = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMAX2 = 0
                        resultMAX2 = i
                        alpha = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMAX2 = 1
                        resultMAX2 = contador + acumulador + 1
                        alpha = 1
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0

            #cuando encuentra dos lineas juntas
            resultMAX = 0
            typeMAX = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != 99 and server['board'][1][contador + acumulador] != 99 and (server['board'][0][i + 1] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i > 23:
                            typeMAX = 0
                            resultMAX = i - 6
                        else:
                            typeMAX = 0
                            resultMAX = i + 6
                            alpha = 2
                    elif server['board'][0][i] != 99 and server['board'][1][contador + acumulador + 1] != 99 and (server['board'][0][i + 1] == 99 and server['board'][1][contador + acumulador] == 99):
                        if i > 23:
                            typeMAX = 0
                            resultMAX = i - 6
                        else:
                            typeMAX = 0
                            resultMAX = i + 6
                            alpha = 2
                    elif server['board'][1][contador + acumulador + 1] != 99 and server['board'][0][i + 1] != 99 and (server['board'][0][i] == 99 and server['board'][1][contador + acumulador] == 99):
                        if i < 6:
                            typeMAX = 0
                            resultMAX = i + 6
                        else:
                            typeMAX = 0
                            resultMAX = i - 6
                            alpha = 2
                    elif server['board'][0][i + 1] != 99 and server['board'][1][contador + acumulador] != 99 and (server['board'][0][i] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i < 6:
                            typeMAX = 0
                            resultMAX = i + 6
                        else:
                            typeMAX = 0
                            resultMAX = i - 6
                            alpha = 2
                    elif server['board'][0][i] != 99 and server['board'][0][i+1] != 99 and (server['board'][1][contador + acumulador] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i > 23:
                            typeMAX = 0
                            resultMAX = i - 6
                        else:
                            typeMAX = 0
                            resultMAX = i + 6
                            alpha = 2
                    elif server['board'][1][contador + acumulador] != 99 and server['board'][1][contador + acumulador+1] != 99 and (server['board'][0][i] == 99 and server['board'][0][i + 1] == 99):
                        if i > 23:
                            typeMIN = 0
                            resultMIN = i - 6
                        else:
                            typeMIN = 0
                            resultMIN = i + 6
                            beta = 2
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0
            
            #cuando encuentra tres lineas seguidas para llenas un cuadrado 
            resultMAX3 = 0
            resultMAXC3 = -1
            typeMAX3 = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMAX3 = 1
                        resultMAX3 = contador + acumulador + 1
                        alpha= 3
                    elif server['board'][0][i] != EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][0][i+1] == EMPTY:
                        typeMAX3 = 0
                        resultMAX3 = i + 1
                        alpha= 3
                    elif server['board'][0][i] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][1][contador + acumulador] == EMPTY:
                        typeMAX3 = 1
                        resultMAXC3 = contador + acumulador
                        alpha= 3
                    elif server['board'][1][contador + acumulador] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][0][i] == EMPTY:
                        typeMAX3 = 0
                        resultMAX3 = i
                        alpha= 3
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0

            #alpha tomara el valor mas alto para continuar su camino
            if alpha == 2:
                typeLine = typeMAX
                position = resultMAX
            elif alpha == 1:
                typeLine = typeMAX2
                position = resultMAX2
            elif alpha == 3:
                typeLine = typeMAX3
                position = resultMAX3
                if resultMAXC3 > 0:
                    position = resultMAXC3
            else:
                typeLine = random.randint(0,1)
                position = random.randint(0,29)
            #Ya que el tablero esta vacio vamos a poner una linea al azar

                
            depth -= 1   
            return typeLine, position, alpha ,depth 

        player = []
        #Aqui comienza min 
        def min_(typeLine, position, beta, depth, player):
            EMPTY = 99
            alpha= -1 #Valor para saber si se encuentra una situacion alpha
            beta = 1 #Valor para saber si se encuentra una situacion beta
            
            #cuando encuentra una linea 
            resultMIN2 = 0
            typeMIN2 = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMIN2 = 0
                        resultMIN2 = i + 1
                        beta = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY:
                        typeMIN2 = 1
                        resultMIN2 = contador + acumulador
                        beta = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador] == EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMIN2 = 0
                        resultMIN2 = i
                        beta = 1
                    elif server['board'][0][i] == EMPTY and server['board'][0][i + 1] == EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMIN2 = 1
                        resultMIN2 = contador + acumulador + 1
                        beta = 1
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0

            #cuando encuentra dos lineas juntas
            resultMIN = 0
            typeMIN = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != 99 and server['board'][1][contador + acumulador] != 99 and (server['board'][0][i + 1] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i > 23:
                            typeMIN = 0
                            resultMIN = i - 6
                        else:
                            typeMIN = 0
                            resultMIN = i + 6
                            beta = 2
                    elif server['board'][0][i] != 99 and server['board'][1][contador + acumulador + 1] != 99 and (server['board'][0][i + 1] == 99 and server['board'][1][contador + acumulador] == 99):
                        if i > 23:
                            typeMIN = 0
                            resultMIN = i - 6
                        else:
                            typeMIN = 0
                            resultMIN = i + 6
                            beta = 2
                    elif server['board'][1][contador + acumulador + 1] != 99 and server['board'][0][i + 1] != 99 and (server['board'][0][i] == 99 and server['board'][1][contador + acumulador] == 99):
                        if i < 6:
                            typeMIN = 0
                            resultMIN = i + 6
                        else:
                            typeMIN = 0
                            resultMIN = i - 6
                            beta = 2
                    elif server['board'][0][i + 1] != 99 and server['board'][1][contador + acumulador] != 99 and (server['board'][0][i] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i < 6:
                            typeMIN = 0
                            resultMIN = i + 6
                        else:
                            typeMIN = 0
                            resultMIN = i - 6
                            beta = 2
                    elif server['board'][0][i] != 99 and server['board'][0][i+1] != 99 and (server['board'][1][contador + acumulador] == 99 and server['board'][1][contador + acumulador + 1] == 99):
                        if i > 23:
                            typeMIN = 0
                            resultMIN = i - 6
                        else:
                            typeMIN = 0
                            resultMIN = i + 6
                            beta = 2
                    elif server['board'][1][contador + acumulador] != 99 and server['board'][1][contador + acumulador+1] != 99 and (server['board'][0][i] == 99 and server['board'][0][i + 1] == 99):
                        if i > 23:
                            typeMIN = 0
                            resultMIN = i - 6
                        else:
                            typeMIN = 0
                            resultMIN = i + 6
                            beta = 2
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0
            
            #cuando encuentra tres lineas seguidas para llenas un cuadrado 
            resultMIN3 = 0
            resultMINC3 = -1
            typeMIN3 = 0
            contador = 0
            acumulador = 0
            N = 6
            i = 0
            for i in range(len(server['board'][0])):
                if ((i + 1) % N) != 0:
                    if server['board'][0][i] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] == EMPTY:
                        typeMIN3 = 1
                        resultMIN3 = contador + acumulador + 1
                        beta= 3
                    elif server['board'][0][i] != EMPTY and server['board'][1][contador + acumulador] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][0][i + 1] == EMPTY:
                        typeMIN3 = 0
                        resultMIN3 = i + 1
                        beta= 3
                    elif server['board'][0][i] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][1][contador + acumulador] == EMPTY:
                        typeMIN3 = 1
                        resultMINC3 = contador + acumulador
                        beta= 3
                    elif server['board'][1][contador + acumulador] != EMPTY and server['board'][0][i + 1] != EMPTY and server['board'][1][contador + acumulador + 1] != EMPTY and server['board'][0][i] == EMPTY:
                        typeMIN3 = 0
                        resultMIN3 = i
                        beta= 3
                    acumulador = acumulador + N
                else:
                    contador = contador + 1
                    acumulador = 0

            #beta tomara el valor mas alto para continuar su camino
            if beta == 2:
                typeLine = typeMIN
                position = resultMIN
            elif beta == 1:
                typeLine = typeMIN2
                position = resultMIN2
            elif beta == 3:
                typeLine = typeMIN3
                position = resultMIN3
                if resultMINC3 > 0:
                    position = resultMINC3

            depth -= 1
            return typeLine, position, beta, depth, player 

        typeLineMIN = 0
        positionMIN = 0
        typeLine, position, alpha, depth = max_(typeLine, position, alpha, depth)
        player = [typeLine, position]
        typeLineMIN, positionMIN, beta, depth, player = min_(typeLine, position, alpha, depth, player)
        
        while depth >0:
            if alpha >= beta:
                typeLine, position, alpha, depth = max_(typeLine, position, alpha, depth)
                print('break beta')
            elif beta >= alpha:
                typeLineMIN, positionMIN, alpha, depth, player = min_(typeLine, position, alpha, depth, player)
                print('break alpha')

        #Esto solo se pone en el caso que algo salga mal 
        while server['board'][typeLine][position] != 99:
            typeLine = random.randint(0,1)
            position = random.randint(0,29)

        return typeLine, position, depth 
    
    typeLine, position, depth = minimax(typeLine, position, depth)
    movement = [typeLine, position]
    print(movement)

    sio.emit('play',{
        'player_turn_id':server['player_turn_id'],
        'tournament_id': 142857,
        'game_id': server['game_id'],
        'movement': movement
    })

@sio.on('finish')
def on_finish(server):
    print('The game', server['game_id'], 'has finished.')

    #restart()

    if server['player_turn_id'] == server['winner_turn_id']:
        print("Ganaste :D")
    else:
        print("Perdiste :(")

    sio.emit('player_ready', {
        'tournament_id': 142857,
        'game_id': server['game_id'],
        'player_turn_id': server['player_turn_id']
    })

sio.connect('http://3.12.129.126:4000')
sio.wait()
