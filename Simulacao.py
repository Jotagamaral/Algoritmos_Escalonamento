import copy
import time

processos = [
    {"processo": "P1", "arrival_time": 0, "tempo_processo": 10, "priority": 3},
    {"processo": "P2", "arrival_time": 0, "tempo_processo": 6, "priority": 5},
    {"processo": "P3", "arrival_time": 0, "tempo_processo": 2, "priority": 2},
    {"processo": "P4", "arrival_time": 0, "tempo_processo": 4, "priority": 1},
    {"processo": "P5", "arrival_time": 0, "tempo_processo": 8, "priority": 4},
]


def fifo(processos):
    print('-----ESCALONAMENTO FIFO-----')
    # Ordena os processos por ordem de chegada
    processos_ordenados = sorted(processos, key=lambda p: p["arrival_time"])

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:

        ordem_atendimento.append(processo['processo']) # Adiciona em ordem os processos
        tempos_resposta.append(tempo_total - processo['arrival_time']) # Calcula o tempo de resposta
        tempo_total = tempo_total + overhead + processo['tempo_processo'] # Calcula o tempo total do processo
        tempos_retorno.append(tempo_total - processo['arrival_time']) # Calcula o tempo de retorno

    media_retorno = sum(tempos_retorno)/len(tempos_retorno)
    media_resposta = sum(tempos_resposta)/len(tempos_resposta)

    print('Ordem de Atendimento:',ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO FIFO COMPLETO-----')

def round_robin(processos, quantum):
    print('-----ESCALONAMENTO ROUND ROBIN-----')
   # Ordena os processos por ordem de chegada
    processos_ordenados = sorted(processos, key=lambda p: p["arrival_time"])
    fila = copy.deepcopy(processos_ordenados)
    
    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []
    processos_completos = []

    while fila:
        processo = fila.pop(0)
        if processo['tempo_processo'] > 0:
            ordem_atendimento.append(processo['processo'])

            if len(tempos_resposta) < len(processos): tempos_resposta.append(tempo_total - processo['arrival_time'])

            tempo_exec = min(processo['tempo_processo'], quantum)
            processo['tempo_processo'] -= tempo_exec
            tempo_total += tempo_exec + overhead

            if processo['tempo_processo'] > 0:
                fila.append(processo)
            else:
                tempos_retorno.append(tempo_total - processo['arrival_time'])

    media_retorno = sum(tempos_retorno)/len(tempos_retorno)
    media_resposta = sum(tempos_resposta)/len(tempos_resposta)


    print('Ordem de Atendimento:',ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO ROUND ROBIN COMPLETO-----')

def prioridade(processos):
    print('-----ESCALONAMENTO PRIORIDADE-----')
    # Ordena os processos por ordem de prioridade
    processos_ordenados = sorted(processos, key=lambda p: p["priority"])

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:

        ordem_atendimento.append(processo['processo']) # Adiciona em ordem os processos
        tempos_resposta.append(tempo_total - processo['arrival_time']) # Calcula o tempo de resposta
        tempo_total = tempo_total + overhead + processo['tempo_processo'] # Calcula o tempo total do processo
        tempos_retorno.append(tempo_total - processo['arrival_time']) # Calcula o tempo de retorno

    media_retorno = sum(tempos_retorno)/len(tempos_retorno)
    media_resposta = sum(tempos_resposta)/len(tempos_resposta)

    print('Ordem de Atendimento:',ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO PRIORIDADE COMPLETO-----')

def sjf(processos):
    print('-----ESCALONAMENTO SJF-----')
    # Ordena os processos por ordem de prioridade
    processos_ordenados = sorted(processos, key=lambda p: p["tempo_processo"], reverse=True)

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:

        ordem_atendimento.append(processo['processo']) # Adiciona em ordem os processos
        tempos_resposta.append(tempo_total - processo['arrival_time']) # Calcula o tempo de resposta
        tempo_total = tempo_total + overhead + processo['tempo_processo'] # Calcula o tempo total do processo
        tempos_retorno.append(tempo_total - processo['arrival_time']) # Calcula o tempo de retorno

    media_retorno = sum(tempos_retorno)/len(tempos_retorno)
    media_resposta = sum(tempos_resposta)/len(tempos_resposta)

    print('Ordem de Atendimento:',ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO SJF COMPLETO-----')

round_robin(processos, 2)
prioridade(processos)
fifo(processos)
sjf(processos)
round_robin(processos, 4)