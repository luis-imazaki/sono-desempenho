from raw.Node import Node

class LinkedLis:
    def __init__(self):
        self.head = None    #inicia a cabeça apontando para nada
        self._size = 0
    
    def append(self, curso, rga, semestre, materia, dia ,inicio, fim):
        if self.head:
            pointer = self.head
            while(pointer.next): #percorre a lista até chegar no Node que aponta para vazio
                pointer = pointer.next
            pointer.next = Node(curso, rga, semestre, materia, dia, inicio, fim)
        else:
            #primeira inserção
            self.head = Node(curso, rga, semestre, materia, dia, inicio, fim)
        self._size = self._size + 1
    
    def __len__(self): #sobrecarga do operador len
        return self._size 
    
    def __getitem__(self, indice):
        # a = lista[5]
        pointer = self.head
        for i in range(indice):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            print("Curso:", pointer.curso, "RGA:", pointer.rga, "Semestre", pointer.semestre, "Dia:", pointer.dia, "Inicio:", pointer.inicio, "Fim:", pointer.fim)
            return 
        return IndexError("list index out of range")