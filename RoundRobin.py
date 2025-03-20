class RoundRobinScheduler:
    def __init__(self, quantum):
        self.fila_processos = []
        self.quantum = quantum
        
    def add_processo(self, pid, tempo_exec):
        self.fila_processos.append((pid, tempo_exec))
        
    def remove_processo(self):
        if self.fila_processos:
            return self.fila_processos.pop(0)
        else:
            print("Nenhum processo para ser removido.")
            return None
    
    def round_robin_scheduling(self):
        tempo_atual = 0
        tempos_espera = {}
        tempos_retorno = {}
        execucoes = {}
        processos_restantes = self.fila_processos.copy
        
        for pid, _ in processos_restantes:
            tempos_espera[pid] = 0
            execucoes[pid] = 0

        print(f"\nExecução dos processos na ordem Round Robin (Quantum: {self.quantum}):\n")
        
        while processos_restantes:
            pid, tempo_exec = processos_restantes.pop(0)
            execucoes[pid] += 1
            
            if tempo_exec > self.quantum:

                print(f"Processo {pid} executando... (Tempo: {tempo_atual} → {tempo_atual + self.quantum})")
                tempo_atual += self.quantum
                processos_restantes.append((pid, tempo_exec - self.quantum))
                
                for p_pid, _ in processos_restantes[:-1]:
                    if p_pid != pid:
                        tempos_espera[p_pid] += self.quantum
            else:
                print(f"Processo {pid} executando... (Tempo: {tempo_atual} → {tempo_atual + tempo_exec})")
                print(f"Processo {pid} finalizado!")
                tempo_atual += tempo_exec
                tempos_retorno[pid] = tempo_atual
                
                for p_pid, _ in processos_restantes:
                    tempos_espera[p_pid] += tempo_exec

        print("\nResumo do escalonamento:")
        print("PID | Tempo de Espera | Tempo de Retorno | Execuções")
        for pid in tempos_espera:
            print(f"{pid:^3} | {tempos_espera[pid]:^15} | {tempos_retorno[pid]:^14} | {execucoes[pid]:^9}")

        round_robin_scheduler = RoundRobinScheduler(2)
        round_robin_scheduler.add_processo(1, 9)
        round_robin_scheduler.add_processo(2, 12)
        round_robin_scheduler.add_processo(3, 33)
        round_robin_scheduler.add_processo(4, 14)
        round_robin_scheduler.round_robin_scheduling()