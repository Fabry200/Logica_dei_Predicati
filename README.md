# Verifica Logica e Tabelle di Verità

Un progetto in Python per lavorare con proposizioni logiche, costruire alberi sintattici e calcolare tabelle di verità. Consente anche di verificare proprietà logiche come tautologie, soddisfacibilità ed equivalenza tra proposizioni.

## Funzionalità principali

- **Costruzione di tabelle di verità**: Genera tutte le combinazioni di valori di verità per proposizioni logiche.
- **Verifica di proprietà logiche**:
  - Tautologia
  - Soddisfacibilità
  - Non-soddisfacibilità
  - Falsificabilità
- **Equivalenza logica**: Controlla se due proposizioni sono logicamente equivalenti.
- **Costruzione di alberi sintattici**: Rappresenta le proposizioni in forma di albero binario.
- **Generazione di proposizioni equivalenti**: Utilizza la proprietà distributiva per trasformare le proposizioni.
-  **Generazione della DNF**: Trasforma le preposizioni nella forma disgiuntiva normale.


## Struttura del progetto

Il progetto ruota attorno alla classe `Nodo`, che rappresenta i nodi di un albero sintattico per le proposizioni logiche. Le principali funzioni includono:

- `values(dizionario)`: Calcola il valore di verità di una proposizione data una mappatura degli atomi logici.
- `tabella(n)`: Genera la tabella di verità per una proposizione con `n` atomi distinti.
- `is_tautologia(n)`, `is_soddisfacibile(n)`, `is_falsificabile(n)`, `is_notsoddisfacibile(n)`: Verifica le proprietà logiche.
- `calcola_equivalente()`: Applica la proprietà distributiva per trasformare una proposizione.
- `costruisci(preposizione, nodo)`: costruisce l'albero delle preposizioni
- `node_instance.dnf(atom_num)`: restituisce la tabella DNF, e la preposizione in forma abbreviata e completa

## Requisiti

- **Python 3.9 o superiore**
- Modulo `itertools` (incluso nella libreria standard di Python)

## Come iniziare

1. Clona il repository:

   ```bash
   git clone https://github.com/tuo-utente/verifica-logica.git
   cd verifica-logica
