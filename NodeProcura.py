from MapProblem_24151_24664 import * 
from libskmaps import *
from collections import deque
import time

class NodeProcura:
    
    def __init__(self, estado, pai=None, acao=None, custo=0, nivel=0):
        self.estado = estado
        self.pai = pai            
        self.acao = acao        
        self.custo = custo       
        self.nivel = 0 if pai is None else pai.nivel + 1 
        self.f = 0

    def BFS(P):
        Node=NodeProcura(P)
        visited = []        
        queue= []

        if P.isFinal():
            return Node
        
        visited.append(Node)
        queue.append(Node)
        

        while queue:
            s=queue.pop(0)
            print(s,end=" ")
           

            visited.append(s)
            print("A visitar:", s.estado.PosPlayer)

            for (succ, act, c) in s.estado.succ():
                print("  Sucessor gerado:", succ.PosPlayer)
                Child = NodeProcura(succ, s, act, s.custo + c,nivel=c+1)

                if succ.isFinal():
                    return Child

                if not any(n.estado.isEqual(succ) for n in visited + queue):
                    queue.append(Child)
        
        return None  
    
    def AStar(P):

        Node = NodeProcura(P)
        Node.f = Node.custo + P.heuristic()

        visited = []
        Pqueue = [Node]
       

        while Pqueue:
           
            Curr = Pqueue.pop(0)
           
            print("A visitar:", Curr.estado.PosPlayer)

            if Curr.estado.isFinal():
                return Curr

            visited.append(Curr)

            for (succ, act, c) in Curr.estado.succ():
                Child = NodeProcura(succ, Curr, act, Curr.custo + c)
                Child.f = Child.custo + succ.heuristic()

                if not any(n.estado.isEqual(succ) for n in visited + Pqueue):
                    inserted = False
                    for i in range(len(Pqueue)):
                        if Child.f < Pqueue[i].f:
                            Pqueue.insert(i, Child)                                     #inserimos o filho antes. <-
                            inserted = True
                            break
                    if not inserted:
                        Pqueue.append(Child)
        return None
    
    def BFS(P):
        raiz = NodeProcura(P)
        if P.isFinal():
            return raiz

        visited = []
        queue = [raiz]

        while queue:
            atual = queue.pop(0)
          
            visited.append(atual)

            for succ, act, c in atual.estado.succ():
              
                filho = NodeProcura(succ, atual, act, atual.custo + c, nivel=atual.nivel + 1)

                if succ.isFinal():
                    return filho

                if not any(n.estado.isEqual(succ) for n in visited + queue):
                    queue.append(filho)

        return None
    
    def AStar(P):
        Node = NodeProcura(P)
        Node.f = Node.custo + P.heuristic()

        visited = []
        Pqueue = [Node]

        while Pqueue:
            # Seleciona e remove o nó com menor f
            Curr = min(Pqueue, key=lambda n: n.f)
            Pqueue.remove(Curr)

       

            if Curr.estado.isFinal():
                return Curr

            visited.append(Curr)

            for (succ, act, c) in Curr.estado.succ():
                Child = NodeProcura(succ, Curr, act, Curr.custo + c)
                Child.f = Child.custo + succ.heuristic()

                if not any(n.estado.isEqual(succ) for n in visited + Pqueue):
                    Pqueue.append(Child)

        return None
    

    def solution(solucao): ##IMPLEMENTAMOS ESTA FUNÇÕES COM FINS DE DEBUG PARA PODER PERCEBER MELHOR COMO SE COMPORTAVA O ALGORITMO.
        caminho = []
        node = solucao
        while node is not None:
            caminho.append(node)
            node = node.pai
        caminho.reverse()
        acoes = []
        for passo, node in enumerate(caminho):
            print(f"Passo {passo}:")
            print(node.estado)
            acoes.append(node.acao)
            time.sleep(0.5) 
        print("Sequência de ações:", [a for a in acoes if a is not None])
        print(f"Custo total: {solucao.custo}")
        print(f"Nível do nó: {solucao.nivel}")
        return acoes
    
    def path(solucao):
        caminho = []
        node = solucao
        while node is not None:
            caminho.append(node)
            node = node.pai
        caminho.reverse()
        acoes = []
        for passo, node in enumerate(caminho):
            print(f"Passo {passo}:")
            print(node.estado)
            acoes.append(node.acao)  
        print("Sequência de ações:",acoes)
        print(f"Custo total: {solucao.custo}")
        print(f"Nível do nó: {solucao.nivel}")
        return acoes

        
if __name__ == "__main__":

    problema = MapProblem("./Mapas/begoon59b.txt")

    resultado = NodeProcura.AStar(problema)
    print("Objetivo:", problema.goal)
    print()
    
    acoes = NodeProcura.path(resultado)
    if resultado is None:
        print("Objetivo:", problema.goal)
        print()
        NodeProcura.solution(resultado)
        #printSkMap(problema)
       
        print("Nenhuma solução encontrada.")
    else:
        print("Número de ações:", len(acoes))
        print("Solução encontrada!")
        #printSkMap(problema)
        print(f"Custo total: {resultado.custo}")
        print(f"Nível do nó: {resultado.nivel}")







