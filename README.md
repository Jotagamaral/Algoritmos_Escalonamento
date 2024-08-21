# Escalonamento de Processos

Este repositório contém um script Python que implementa diferentes algoritmos de escalonamento de processos. O objetivo é demonstrar como diferentes métodos podem ser aplicados para gerenciar a execução de processos com base em diferentes critérios.

## Algoritmos Implementados

O código inclui quatro algoritmos principais de escalonamento:

1. **FIFO (First-In-First-Out)**: Processos são atendidos na ordem em que chegam.
2. **Round Robin**: Processos são atendidos por um intervalo de tempo fixo (quantum), sendo retornados à fila se não completarem durante o quantum.
3. **Prioridade**: Processos são atendidos com base em sua prioridade, onde processos com menor valor de prioridade são atendidos primeiro.
4. **SJF (Shortest Job First)**: Processos são atendidos com base no tempo de execução mais curto primeiro.

## Dependências

O script usa a biblioteca padrão do Python e não possui dependências externas adicionais. As bibliotecas utilizadas são:

- **`copy`**: Fornece funções para criar cópias profundas de objetos.
- **`time`**: Fornece funções relacionadas ao tempo (não utilizado diretamente neste código, mas incluído por boas práticas).

## Código

O código contém quatro funções principais para implementar os algoritmos de escalonamento:

### 1. FIFO (First-In-First-Out)

A função `fifo` realiza o escalonamento FIFO:

```python
def fifo(processos):
    print('-----ESCALONAMENTO FIFO-----')
    processos_ordenados = sorted(processos, key=lambda p: p["arrival_time"])

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:
        ordem_atendimento.append(processo['processo'])
        tempos_resposta.append(tempo_total - processo['arrival_time'])
        tempo_total += overhead + processo['tempo_processo']
        tempos_retorno.append(tempo_total - processo['arrival_time'])

    media_retorno = sum(tempos_retorno) / len(tempos_retorno)
    media_resposta = sum(tempos_resposta) / len(tempos_resposta)

    print('Ordem de Atendimento:', ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO FIFO COMPLETO-----')

```

### 2. Round Robin

A função `round_robin` realiza o escalonamento Round Robin:

```python
def round_robin(processos, quantum):
    print('-----ESCALONAMENTO ROUND ROBIN-----')
    processos_ordenados = sorted(processos, key=lambda p: p["arrival_time"])
    fila = copy.deepcopy(processos_ordenados)
    
    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    while fila:
        processo = fila.pop(0)
        if processo['tempo_processo'] > 0:
            ordem_atendimento.append(processo['processo'])
            if len(tempos_resposta) < len(processos):
                tempos_resposta.append(tempo_total - processo['arrival_time'])
            tempo_exec = min(processo['tempo_processo'], quantum)
            processo['tempo_processo'] -= tempo_exec
            tempo_total += tempo_exec + overhead
            if processo['tempo_processo'] > 0:
                fila.append(processo)
            else:
                tempos_retorno.append(tempo_total - processo['arrival_time'])

    media_retorno = sum(tempos_retorno) / len(tempos_retorno)
    media_resposta = sum(tempos_resposta) / len(tempos_resposta)

    print('Ordem de Atendimento:', ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO ROUND ROBIN COMPLETO-----')

```

### 3. Prioridade

A função `prioridade` realiza o escalonamento Prioridade:

```python
def prioridade(processos):
    print('-----ESCALONAMENTO PRIORIDADE-----')
    processos_ordenados = sorted(processos, key=lambda p: p["priority"])

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:
        ordem_atendimento.append(processo['processo'])
        tempos_resposta.append(tempo_total - processo['arrival_time'])
        tempo_total += overhead + processo['tempo_processo']
        tempos_retorno.append(tempo_total - processo['arrival_time'])

    media_retorno = sum(tempos_retorno) / len(tempos_retorno)
    media_resposta = sum(tempos_resposta) / len(tempos_resposta)

    print('Ordem de Atendimento:', ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO PRIORIDADE COMPLETO-----')

```
### 4. SJF (Shortest Job First)

A função `sjf` realiza o escalonamento SJF:

```python
def sjf(processos):
    print('-----ESCALONAMENTO SJF-----')
    processos_ordenados = sorted(processos, key=lambda p: p["tempo_processo"], reverse=True)

    overhead = 0.5
    tempo_total = 0
    tempos_resposta = []
    tempos_retorno = []
    ordem_atendimento = []

    for processo in processos_ordenados:
        ordem_atendimento.append(processo['processo'])
        tempos_resposta.append(tempo_total - processo['arrival_time'])
        tempo_total += overhead + processo['tempo_processo']
        tempos_retorno.append(tempo_total - processo['arrival_time'])

    media_retorno = sum(tempos_retorno) / len(tempos_retorno)
    media_resposta = sum(tempos_resposta) / len(tempos_resposta)

    print('Ordem de Atendimento:', ordem_atendimento)
    print('Tempo de Resposta:', tempos_resposta)
    print('Tempo de Retorno:', tempos_retorno)
    print('Média do tempo de Retorno:', media_retorno)
    print('Média do tempo de Resposta:', media_resposta)
    print('-----ESCALONAMENTO SJF COMPLETO-----')


```

