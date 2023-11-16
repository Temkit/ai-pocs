# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
openai.api_key = "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";

completion = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": """ act as a senior banker, here a salary certificate for a user, can you give all the informaitons it contains :2221a4LJiwieglis,aji
SntF
soclÉTÉ NATIONALE DES TRANSPORTS FERROVIAIRES
UNITE
REG
FER
ORAN
BULLETIN DE PAIE
N €NMs:$:
31
429.878-34
Vi
PERTODE
24701F
1
R4
SEPTEMBRE/2023
FABYSSEMENT
1 dence
Trains
d'Oran
MATRICULE
NOM
PRENOMS
S. F
P.A €
0681306
SOTRI
YACINE
PO STE
CATISECT.
INDICE
DATE POSTE
CONDUCTEUR
EN
QUEUE /TRAIN
2/1
06
TPE
0361
31/03/22
DATE EMBAUCHE
N' S.S
N' MUT.
MODE PAIEMENT
N' COMPTE
12/11/09
840859004143
4120019J
C
B
0031
226205168867
CODE
DES/G N A TI0 N
NBREIBASE
TAUX
ARETENIR
A PAYER
100
Salaire
de
base
29
602 , 00
29.602
00
101
I .E .P
(s.N.T .F)
32,50
9 . 620
65
122
Ind
de
nuisances
20
00
5
920
40
156
Prime
cond
Part
Expl
8
00
2
210,28
135
Prime
Risque
Roulant
poo
00
840 ,00
159
Pr
Acc
Train
Sce
Exp
10
00
2.762,85
154
Ind
de
zone
414
42
164
Ind.Util
Rep. Legaux
15
865 , 30
9
979
50
180
Ind
Serv
Commandé
22
25
00
5
427 
01
129
Prime
Rend
Ind
(PRK
3.552,00
28
00
8
727
32
106
Prime
Rend
Ind
(PRI
13
25
522
96
141
Pr
Rend
Collect ( PRC
50
1
924
13
202
Ind
de
transport
3
000
00
207
Ind
de panier
6oo
00
2
000
00
344
Al1
Conjoint/charge
3
0o0
00
313
I .Comp
F
Tel
Cond
L
Pso
00
233,33
318
Ind
depl
RP / roulant
195
00
85
00
16.575,00
400
Cot
Sécurité
Sociale
77
951
52
9
00
7 .015,64
406
Cot
fixe
MUTRASEF
77
951
52
0o
410 ,00
410
Ret
Impôt
(I .R.G)
75
521
46
2
690 , 40
412
Cot
fixe
M.G . F
77 .951
52
50
169,27
413
cot
fonds
décès
MGF
1 , 00
779,51
TOTAL A PAYER
TOTAL A RETENIR
TOTAL IND. N. IMP
NET A PAYER
+102
759,85
+22
064 ,82
+19.808 , 33
+80.695 , 03
Ret
0 ,0 j &
0 , 0
h;
Congés :
2 ,0
j;
Mal
0
0
Scanné avec CamScanner
<

""" }
  ]
  ,temperature=0.1
)

html = completion.choices[0].message.content
print(html)

#write html to file
f = open("crm1.html", "w")
f.write(html)
f.close()

