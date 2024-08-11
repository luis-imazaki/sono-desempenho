class Node:
    def __init__(self, curso, rga, semestre, materia, dia, inicio, fim):
        self.curso =  curso
        self.rga = rga
        self.semestre = semestre
        self.materia = materia
        self.dia = dia
        self.inicio = inicio
        self.fim  = fim
        self.next = None
