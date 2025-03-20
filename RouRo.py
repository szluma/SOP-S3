class RoundRobinScheudler:
    def __init__(self, quantum):
        self.fila_processos = []
        self.quantum = quantum
        
    def adicionar_processo(self, pid, tempo_exec):
        self.fila_processos.append((pid, tempo_exec))
        
    def remover_processo(self):
        if self.fila_processos:
            return self.fila_processos.pop(0)
        else:
            print("Nenhum processo para remover.")
            return None
    
    def round_robin_scheduling(self):
        tempo_atual = 0
        tempos_espera = {}
        tempos_retorno = {}
        execucoes = {}
        processos_restantes = self.fila_processos.copy
        
