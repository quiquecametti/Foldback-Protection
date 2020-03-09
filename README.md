# Foldback-protection
Utiliza diversas ecuaciones que permiten elegir la mejor combinación de resistencias para realizar la protección foldback de una fuente de tensión.

## Descarga
```sh
$ git clone https://github.com/Quik-e/Foldback-Protection.git
```

## Output de ejemplo
```
   Rb
---------  =  0.048
 Rb + Rc

Ra (ohm)  Rb (kohm)  Rc (kohm)  Vo (V)  Io (A)  VBEon (V)
  1.0        1.0     19.625    15.0     1.5        0.7
  1.0        1.2     23.550    15.0     1.5        0.7
  1.0        1.5     29.438    15.0     1.5        0.7
  1.0        1.8     35.325    15.0     1.5        0.7
  1.0        2.2     43.175    15.0     1.5        0.7
  1.0        3.3     64.762    15.0     1.5        0.7
  1.0        3.9     76.538    15.0     1.5        0.7
  1.0        4.7     92.238    15.0     1.5        0.7
  1.0        5.1    100.087    15.0     1.5        0.7
  1.0        5.6    109.900    15.0     1.5        0.7
  1.0        6.8    133.450    15.0     1.5        0.7
  1.0        8.2    160.925    15.0     1.5        0.7

Elijo Rb = 5.6 kohm y Rc = 100kohm

Iomax (A)  Iocc (A)  Io max Pd T1 (A)  Vo max Pd T1  Ro max Pd T1
1.5007    0.7357          0.883777      2.903478      3.285304

```
