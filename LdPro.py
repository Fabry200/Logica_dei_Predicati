#autore fabrizio verace I.A 2024
from itertools import product

class Nodo:
  def __init__(self,name,parent=None):
    self.name=name
    self.left=None
    self.right=None
    self.parent=parent

  def stampa(self, livello=0): #funzione di stampa, suggerita dal prof
    spazio=" "*livello+self.name+"\n"

    if self.left:
      spazio+=self.left.stampa(livello+1)

    if self.right:
      spazio+=self.right.stampa(livello+1)
    return spazio

  def __repr__(self):
   return self.stampa()

  def values(self,dizionario): #funzione values che valuta il VdV di una proposizione attraverso un dizionario

    #ho avuto dei problemi col comando replace,per rimpiazzare gli atomi coi valori booleani
    #essendo la stringa non modificabile in place senza replace l'ho convertita in lista di caratteri e ho sostituito i caratteri, per ricomporla poi con join
    self.iter = [x for x in self.name]
    for x in range(len(self.iter)):
      if self.iter[x] in dizionario:
        self.iter[x] = str(dizionario[self.iter[x]])
    self.stringa=''.join(self.iter)

    return eval(self.stringa)

  def tabella(self, n, scrittura=True): #se gli do scrittura come parametro a false, non scrive la tabella ma solo i valori di verita, utile per le altre funzioni
    self.p=product(['True','False'],repeat=n)
    self.p=list(self.p)

    if n==1:
      self.tabella_verita=[[] for x in range(n*n+1)] #se la proposizione contiene un atomo, la tabella contiene due righe
    else:
      self.tabella_verita=[[] for x in range(n*n)] #senno' contiene n per n righe
    self.valori_verita=[]

    lista_atomi=['s','p','q','r']

    lista_atomi_presenti=set([x for x in self.name if x in lista_atomi]) #prima converto in set cosi elimino le ripetizioni di elementi poi in lista, cosi lavoro agevolmente
    lista_atomi_presenti=list(lista_atomi_presenti)

    dictb={'A': ' and ', 'O': ' or ', 'N': 'not '}
    counter=0
    for x in range(len(self.p)):  
      for j in range(len(self.p[0])):
         dictb[lista_atomi_presenti[counter]]=self.p[x][j]  #itero attraverso il prodotto cartesiano e assegno a dictb[atomo] il valore associato al prodotto cartesiano eseguito
         self.tabella_verita[x].append(self.p[x][j])
         counter+=1

      self.valori_verita.append(self.values(dictb))
      self.tabella_verita[x].append(self.values(dictb))
      #print(dictb, self.values(dictb))
      if counter == n: #resetto il counter, perche questo contatore deve andare da 0 a n sempre, cosi itero attraverso atomi_presenti[counter]
        counter=0

    if scrittura==True:
      for rows in self.tabella_verita:
        print(rows)
      print('\n')
      return self.valori_verita
    else:
      return self.valori_verita

  def is_tautologia(self,n): 
    for x in self.tabella(n): 
      if x == False: #tutti true
        return False
    return True
   
  def is_soddisfacibile(self,n):
    if self.tabella(n,False).count(True) != 0 : #almeno un true
      return True
    else:
      return False
  def is_falsificabile(self,n):
    for x in self.tabella(n): #almeno un false
      if x == False:
        return True
    return False

  def is_notsoddisfacibile(self,n):
    if self.tabella(n,False).count(False) == len(self.tabella(n)): #tutti false
      return True
    else:
      return False

  def calcola_equivalente(self):

    def distribuitiva(): 
      atomi=['p', 'q', 'r', 's']
      lista_duplicati=[]
      preposizione=None
      button=False
      for x in range(len(self.name)):
        if self.name[x] in atomi:
          elem=self.name[x]
          preposizione=self.name[x+1] #perche usiamo la notazione tokenizzata, quindi l'atomo  viene dopo la preposizione (solo perche abbiamo scelto di usare distribuitiva)

          for j in range(x+1, len(self.name)): #itero attraverso un ciclo che va dopo l' atomo trovato e ne cerca un altro uguale
            if elem == self.name[j]:
              lista_duplicati.append(elem)
              button=True
              break
        if button == True:
          break

      if lista_duplicati==[]:
        print('nessun duplicato trovato, impossibile usare la distribuzione')
        return False

      lista_atomi_presenti=[x for x in self.name if x in atomi and x not in lista_duplicati]

      #print(preposizione)
      #print(lista_atomi_presenti,lista_duplicati)
      stringa='('+lista_duplicati[0]+preposizione+'('

      if preposizione=='A':
        preposizione='O'
      elif preposizione =='O':
        preposizione='A'

      for x in range(len(lista_atomi_presenti)):
        stringa=stringa+lista_atomi_presenti[x]
        if x == 0:
          stringa=stringa+preposizione
      stringa=stringa+')'+')'

      return stringa.replace('A', ' and ').replace('N','not ').replace('O', ' or ')

    equivalente=distribuitiva()
    return equivalente


def costruisci(albero, nodo):
  nodo_corrente=nodo
  for x in albero:
    match x:
      case '(':
        nodo_sinistro=Nodo('',parent=nodo_corrente)
        nodo_corrente.left=nodo_sinistro
        nodo_corrente=nodo_sinistro
      case ')':
        nodo_corrente=nodo_corrente.parent
      case 'A' | 'O':
        nodo_corrente.name=x
        nodo_destro=Nodo('', nodo_corrente)
        nodo_corrente.right=nodo_destro
        nodo_corrente=nodo_destro
      case 'N' :
        nodo_corrente=nodo_corrente.parent
        nodo_corrente.left=None
        nodo_corrente.name=x
        nodo_destro=Nodo('', nodo_corrente)
        nodo_corrente.right=nodo_destro
        nodo_corrente=nodo_destro
      case _:
        nodo_corrente.name=x
        nodo_corrente=nodo_corrente.parent

def is_equal(p1,n1, p2, n2):
  tab_p1=p1.tabella(n1,False)
  tab_p2=p2.tabella(n2,False)

  if len(tab_p1)>len(tab_p2) or len(tab_p1)<len(tab_p2):
    print('Non equivalenti, lunghezza differente')
    return False
  if tab_p1==tab_p2:
    print('equivalenti')
    return True
  else:
    print('non equivalenti')
    return False


def main():
  A='((p and q) and (not r))'.replace(' and ', 'A').replace('not ','N').replace(' or ', 'O')
  B='((r or q) and (not r))'.replace(' and ', 'A').replace('not ','N').replace(' or ', 'O')
  C='(p or (not p))'.replace(' and ', 'A').replace('not ','N').replace(' or ', 'O')
  D='((p or q) and (p or r))'.replace(' and ', 'A').replace('not ','N').replace(' or ', 'O')

  p1=Nodo(A)
  p2=Nodo(B)
  p3=Nodo(C)
  p4=Nodo(D)

  dizionario ={'p': True, 'q': True, 'r': False, 'A': ' and ', 'O': ' or ', 'N': 'not '} #1) dizionario per il primo caso
 
  #print(p1.values(dizionario)) #1) caso, calcolare VdV per qualche valore che abbiamo assegnato (assegnazione manuale tramite dizionario)
  #print(p1.tabella(3)) #2) caso, calcolare la tabella di verita' di una proposizione (la funzione tabella returna la colonna dei VdV, ma la tabella diventa comunque un attributo della classe.)
  #print(p2.tabella(2)) #Bisogna specificare quanti atomi non ripetuti ci sono
  #print(p3.tabella(1)) #tabella 2x2
  #print(p4.tabella(3))
  #print(p3.is_tautologia(1))  #3.1)Tautologia
  #print(p3.is_soddisfacibile(1)) #3.2)Soddisfacibile
  #print(p2.is_notsoddisfacibile(2)) #3.3)Non soddisfacibile
   #print(p1.is_falsificabile()) #3.4)Falsificabile
  #is_equal(p1,3,p2,2) 4) Calcolo se una proposizione e' equivalente

  #4) Calcolo della preposizione equivalente solo in un caso (come richiesto dal prof), con la proprieta dei predicati distribuitiva
  #print(p4.calcola_equivalente())

    #verifico:
  #preposizione_equivalente=Nodo(p4.calcola_equivalente().replace(' and ', 'A').replace('not ','N').replace(' or ', 'O'))
  #is_equal(p4,3,preposizione_equivalente,3)

  #costruzione del albero
  #costruisci(A,p1)

if __name__ == "__main__":
  main()
