#Progetto: Oscillazioni climatiche
Matteo Francescangeli (matteo.francescangeli1@studenti.unipg.it)
università degli studi di Perugia: corso di Metodi Computazionali per la Fisica
# Oscillazioni Climatiche negli Ultimi 800.000 Anni

Questo progetto analizza le variazioni climatiche degli ultimi 800.000 anni,
focalizzandosi sulle temperature, sulla concentrazione di CO₂ atmosferica e
sulla loro correlazione. I dati utilizzati provengono da carotaggi di ghiaccio,
che offrono registrazioni dettagliate delle condizioni climatiche passate.

## Descrizione del Progetto

I carotaggi di ghiaccio forniscono informazioni preziose sulle condizioni
climatiche storiche, in particolare su temperatura e concentrazione di CO₂.

In questo progetto, si vuole analizzare i dati ottenuti da tali carotaggi per:

- Determinare le principali frequenze e periodi di oscillazione delle
temperature e delle concentrazioni di CO₂.
- Valutare la correlazione tra queste due variabili nel tempo.

## Metodologia

A causa della natura irregolare dei dati temporali derivanti dai carotaggi di
ghiaccio, l'uso della Trasformata di Fourier (FFT) non era appropriato.
Pertanto si è optato  per il Periodogramma di Lomb-Scargle utilizzato per
l'analisi spettrale di dati campionati in modo non uniforme. (sia dalla
libreria di scipy sia di astropy)
Per individuare i picchi maggiori nello spettro di potenze si è utilizzato un
fit rispetto alla funzione del rumore così da dividere i picchi dovuti a rumore
e i picchi veri e propri che indicano una periodicità.
## Risultati

L'analisi ha permesso di identificare:
- Frequenze Dominanti: Specifiche frequenze che caratterizzano le oscillazioni
climatiche nel periodo studiato.
- Periodi di Ripetizione: I principali periodi di ripetizione sia per le variazioni di temperatura che per le concentrazioni di CO₂.
- Correlazione: Una forte correlazione tra le variazioni di temperatura e i
livelli di CO₂, suggerendo un legame stretto tra queste due variabili.


## Come usare il progetto

Per replicare l'analisi:
i file contenenti i dati si trovano ai seguenti link (non è necessario
scaricarli):
  -https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3deuttemp2007-noaa.txt
  -https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3-composite-co2-2008-noaa.txt

il progetto è all'interno del file 'progetto.py' il quale è diviso in 6
argomenti (argparse).
le opzioni sono le seguenti:
  -h, --help  show this help message and exit
  --pt1       'grafici di temperatura e concentrazione di CO2 rispetto al tempo'
  	      mette in relazione i dati  con il tempo
  --pt2       'analisi di distanze temporali di campionamento'
  	      si osserva l'irregolarità dei campionamenti
  --pt3       'Lombscargle e spettri di potenza'
  	      studio degli spettri in frequenza
  --pt4       'fit degli spettri di potenza'
  	      fit rispetto alla funzione generica del rumore
  --pt5       'confronto nel dominio temporale e di frequenze'
  	      confronto qualitativo degli andamenti normalizzati
  --pt6       'individuazione frequenze principali'
  	      stampa le frequenze considerate principali e ricostruisce gli
	      andamenti con solo le frequenze principali

nel selezionare le opzioni --pt3,--pt4 e --pt5 il programma richiederà
all'utente di inserire quale metodo si preferisce per produrre lo spettro di
potenza: '1' (stringa) per utilizzare scipy e '2' (stringa) per Astropy.