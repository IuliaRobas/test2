# test2
Instructions of a processor.

Gestiunea instructiunilor pe procesor
Sistem multicod cu 2 coruri
O Instructiune e identificata prin: 
-ID unic, 
-ID programului din care face parte
-un camp care poate fi:
 	I-instructiune de inceput a programului 
 	F- instr de final a programului
 	O- instr obisnuita
-resure : intreg care reprezinta cantitatea de resurse de care are nevoie
-durata: intreg = timpul in milisecunde

Functionalitatea1: introducerea unei instructiuni caracterisitce unui program in aplicatie
Functionalitatea2: se stie ca fiecarui program i se introduce atat instructiunea de inceput, cat si de sfarsit =>calculam durata de 
timp de la instructiunea initiala si pana cand a fost introdusa instructiunea finala. Avand un core care are o capacitate de resurse, un program poate rula doar pe un core care ii asigura minimul de resurse.
resursele sunt hardcodate.
Determinam core-ul pe care poate rula in acelasi timp o instructiune si pt fiecare program din aplicatie il scriem in fisier (la finalul acestuia) si durata totala de executie a programului  (momentul de inceput pana la momentul de final)

