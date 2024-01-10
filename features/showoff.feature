# language: ro
Functionalitate:  Inregistrari pentru luna decembrie

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie

#     SC „ABC” S.A. are ca obiect de activitate producţie, comerţ, servicii diverse, operaţiuni de import-export,
#     speculaţii la bursă etc., derulează operațiuni în luna decembrie N.

    * creez un proiect:
      | nume | organizatie   | cif     | nrc           | tip     |cod_caen| telefon    | email           | mod_tva   | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" S.A | R910910 | J40/65703/200 | proiect |4444| 0721222333 | contact@abc.com | facturare | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |

##     Acţiunile deţinute la entităţile afiliate, în valoare de 250.000 lei, sunt reprezentate de 500 de acţiuni emise
##     de S.C.„AAA” SA, cumpărate pentru 500 lei/bucata și evidențiate în contul 261
#
#    * creez o entitate afiliata:
#      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada      | numar | cod_postal | cont_bancar             | detalii       |
#      | S.C.„AAA” SA | 3021130 | J29/777/1999 | afiliat | 0755623155 | contact@aaa.com | facturare | Romania | Bucuresti | Bucuresti | Garofitelor | 112   | 031183     | RO50PORL888888286982666 | Zarzavat Bank |
#
#    * adaug "actiuni" detinute la entitatea afiliata:
#      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
#      | S.C.„AAA” SA | 2              | 500       | 500            | 261           | 2021-09-01     |
#
##      La 31.12.N-1 valoarea de piaţă a acţiunilor „AAA” a fost de 400 lei/bucata;
#
##   * actualizez valoarea actiunilor detinute la entitatea afiliata "S.C.„AAA” SA":
##      | id_organizatie | valoare_de_piata |
#
##     Titlurile de plasament se referă la 100 acţiuni „BBB”, cumpărate pentru 20 lei/bucata şi 200 acţiuni „CCC”,
##     cumpărate pentru 50 lei/bucata; conturile contabile utilizate sunt 5081/ BBB și 5081/CCC.
#
#    * creez o entitate afiliata:
#      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
#      | S.C.„BBB” SA | 2255048 | J42/111/2006 | afiliat | 0763999882 | contact@bbb.com | facturare | Romania | Bucuresti | Bucuresti | Zambilelor | 11    | 031183     | RO50PORL777777286982666 | Zarzavat Bank |
#
#    * adaug "titluri de plasament" detinute la entitatea afiliata:
#      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
#      | S.C.„BBB” SA | 3              | 100       | 20             | 5081          | 2022-11-01     |
#
#    * creez o entitate afiliata:
#      | organizatie  | cif     | nrc          | tip     | telefon     | email           | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
#      | S.C.„CCC” SA | 4589721 | J29/235/1989 | afiliat | 07442236666 | contact@ccc.com | facturare | Romania | Bucuresti | Bucuresti | Liliacului | 76B   | 031183     | RO50PORL666666286980066 | Zarzavat Bank |
#
#    * adaug "titluri de plasament" detinute la entitatea afiliata:
#      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
#      | S.C.„CCC” SA | 4              | 200       | 50             | 5081          | 2023-10-11     |
#
#
#
#
#    * adaug o imobilizare corporala
#      | asset_name         | clasa | cont_analitic | cont_analitic_amortizare | tip_amortizare | valoare_totala | durata_utilizare | data_achizitie | data_inregistrare | descriere                            |
#      | masina tip A       | 21    | 2133          | 2813                     | liniara        | 30000          | 5                | 2020-10        | 2023-11           | renault clio, 2019, 1.5 diesel, 90cp |
#      | cladire depozit    | 21    | 212           | 2812                     | liniara        | 180000         | 50               | 2014-07        | 2023-11           | cladire depozit, zona pipera         |
#      | program informatic | 208   | 208           | 2808                     | liniara        | 3600           | 36               | 2021-04        | 2023-11           | program informatic gestiune depozit  |
#      | program informatic | 214   | 214           | 2814                     | liniara        | 4800           | 48               | 2023-06        | 2023-11           | mobilier de birou                    |
#
#    * actualizez rulaj valutar:
#      | moneda | cantitate | pret_achizitie | cont_analitic | data_achizitie | tip_rulaj_valuta |
#      | EUR    | 10417     | 4.799          | 5124          | 2023-09-01     | cash             |
#
#    * preiau balanta de verificare pentru luna "2023-11":
#      | cont | debit_initial | credit_initial | debit      | credit    |
#      | 1012 | 0.00          | 220000.00      | 0.00       | 0.00      |
#      | 1061 | 0.00          | 5000.00        | 0.00       | 0.00      |
#      | 1068 | 0.00          | 100000.00      | 0.00       | 0.00      |
#      | 117  | 0.00          | 60000.00       | 0.00       | 25000.00  |
#      | 121  | 0.00          | 30000.00       | 30000.00   | 0.00      |
#      | 121  | 596710.00     | 728000.00      | 93851.00   | 119000.00 |
#      | 129  | 5000.00       | 5000.00        | 0.00       | 0.00      |
#      | 208  | 3600.00       | 0.00           | 0.00       | 0.00      |
#      | 212  | 180000.00     | 0.00           | 0.00       | 0.00      |
#      | 2133 | 30000.00      | 0.00           | 0.00       | 0.00      |
#      | 214  | 4800.00       | 0.00           | 0.00       | 0.00      |
#      | 261  | 250000.00     | 0.00           | 0.00       | 0.00      |
#      | 2808 | 0.00          | 2900.00        | 0.00       | 100.00    |
#      | 2812 | 0.00          | 33000.00       | 0.00       | 300.00    |
#      | 2813 | 0.00          | 12500.00       | 0.00       | 5500.00   |
#      | 2814 | 0.00          | 300.00         | 0.00       | 100.00    |
#      | 2961 | 0.00          | 50000.00       | 0.00       | 0.00      |
#      | 301  | 37500.00      | 30000.00       | 7500.00    | 12000.00  |
#      | 303  | 0.00          | 0.00           | 2500.00    | 2500.00   |
#      | 345  | 15000.00      | 15000.00       | 15000.00   | 15000.00  |
#      | 371  | 15000.00      | 15000.00       | 350000.00  | 310000.00 |
#      | 4011 | 0.00          | 0.00           | 470700.00  | 917205.00 |
#      | 404  | 0.00          | 28200.00       | 0.00       | 0.00      |
#      | 4091 | 12000.00      | 0.00           | 0.00       | 12000.00  |
#      | 4092 | 16000.00      | 0.00           | 0.00       | 16000.00  |
#      | 4111 | 0.00          | 0.00           | 1020800.00 | 450000.00 |
#      | 4112 | 18000.00      | 0.00           | 0.00       | 10000.00  |
#      | 421  | 0.00          | 0.00           | 51458.00   | 55000.00  |
#      | 425  | 0.00          | 0.00           | 1000.00    | 1000.00   |
#      | 4315 | 0.00          | 0.00           | 21880.00   | 24064.00  |
#      | 4316 | 0.00          | 0.00           | 1750.00    | 1925.00   |
#      | 436  | 0.00          | 0.00           | 113.00     | 113.00    |
#      | 441  | 0.00          | 0.00           | 9500.00    | 9500.00   |
#      | 4423 | 0.00          | 0.00           | 61142.00   | 70300.00  |
#      | 4426 | 0.00          | 0.00           | 13072.00   | 13072.00  |
#      | 4427 | 0.00          | 0.00           | 22230.00   | 22230.00  |
#      | 444  | 0.00          | 0.00           | 6080.00    | 6688.00   |
#      | 447  | 0.00          | 0.00           | 380.00     | 418.00    |
#      | 471  | 0.00          | 0.00           | 5500.00    | 2300.00   |
#      | 508  | 0.00          | 0.00           | 12000.00   | 0.00      |
#      | 5121 | 0.00          | 0.00           | 840401.00  | 576252.00 |
#      | 5124 | 0.00          | 0.00           | 50000.00   | 0.00      |
#      | 5191 | 0.00          | 0.00           | 0.00       | 300000.00 |
#      | 5311 | 0.00          | 0.00           | 162000.00  | 120000.00 |
#      | 581  | 0.00          | 0.00           | 13000.00   | 13000.00  |
#      | 601  | 0.00          | 0.00           | 12000.00   | 12000.00  |
#      | 6022 | 0.00          | 0.00           | 2000.00    | 2000.00   |
#      | 603  | 0.00          | 0.00           | 2500.00    | 2500.00   |
#      | 604  | 0.00          | 0.00           | 1000.00    | 1000.00   |
#      | 6051 | 0.00          | 0.00           | 300.00     | 300.00    |
#      | 6052 | 0.00          | 0.00           | 500.00     | 500.00    |
#      | 607  | 0.00          | 0.00           | 32000.00   | 32000.00  |
#      | 611  | 0.00          | 0.00           | 6000.00    | 6000.00   |
#      | 612  | 0.00          | 0.00           | 3000.00    | 3000.00   |
#      | 613  | 0.00          | 0.00           | 3000.00    | 3000.00   |
#      | 623  | 0.00          | 0.00           | 2500.00    | 2500.00   |
#      | 626  | 0.00          | 0.00           | 1000.00    | 1000.00   |
#      | 627  | 0.00          | 0.00           | 1400.00    | 1400.00   |
#      | 628  | 0.00          | 0.00           | 9000.00    | 9000.00   |
#      | 635  | 0.00          | 0.00           | 38.00      | 38.00     |
#      | 641  | 0.00          | 0.00           | 10000.00   | 10000.00  |
#      | 636  | 0.00          | 0.00           | 113.00     | 113.00    |
#      | 6581 | 0.00          | 0.00           | 3000.00    | 3000.00   |
#      | 6584 | 0.00          | 0.00           | 2000.00    | 2000.00   |
#      | 6588 | 0.00          | 0.00           | 0.00       | 0.00      |
#      | 6651 | 0.00          | 0.00           | 1500.00    | 1500.00   |
#      | 6811 | 0.00          | 0.00           | 1000.00    | 1000.00   |
#      | 691  | 10.00         | 10.00          | 0.00       | 0.00      |
#      | 7015 | 0.00          | 0.00           | 22000.00   | 22000.00  |
#      | 704  | 0.00          | 0.00           | 50000.00   | 50000.00  |
#      | 707  | 0.00          | 0.00           | 45000.00   | 45000.00  |
#      | 711  | 0.00          | 0.00           | 15000.00   | 15000.00  |
#      | 7588 | 0.00          | 0.00           | 1200.00    | 1200.00   |
#      | 761  | 0.00          | 0.00           | 0.00       | 0.00      |
#      | 7651 | 0.00          | 0.00           | 0.00       | 0.00      |
#      | 766  | 0.00          | 0.00           | 800.00     | 800.00    |
#
#    * inchid luna "2023-11"
#
#    * creez un furnizor:
#      | organizatie            | cif     | nrc          | tip      | telefon    | email                     | mod_tva   | tara    | judet     | oras      | strada   | numar | cod_postal | cont_bancar             | detalii       |
#      | „Happy Leasing” IFN SA | 3020048 | J29/777/1999 | supplier | 0721222333 | contact@happy-leasing.com | facturare | Romania | Bucuresti | Bucuresti | Crinului | 220   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |
#    * creez un client:
#      | organizatie   | cif     | nrc          | tip    | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
#      | SC. "ASS" S.A | 3020048 | J29/777/1999 | client | 0721112373 | contact@ass.com | facturare | Romania | Bucuresti | Bucuresti | Ghioceilor | 17    | 031183     | RO50PORL739266211223366 | Zarzavat Bank |
#    * creez un client agent:
#      | nume    | prenume | telefon    | cnp     | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
#      | Ionescu | Emilian | 0721666555 | Emilian | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |
#
#
##     02 decembrie Se vinde domnului Ionescu Emilian, CNP 1790718341701, mijlocul de transport cu 15.000 lei,
##     TVA 19%; valoarea de intrare a imobilizării este de 30.000 lei, iar amortizarea cumulată până în momentul
##     vânzării este de 18.000 lei.
#
#
##     07 decembrie Se recepţionează mărfuri din import (Australia); potrivit DVI preţul de cumpărare negociat cu
##     furnizorul extern „BaBeB” este de 5.000 euro (condiţia de livrare exworks); transport extern 1.000 euro; taxa
##     vamală 10%, comisionul vamal 0,5% şi TVA 19% sunt plătite în aceeaşi zi prin virament bancar; cursul
##     valutar de la data vămuirii este de 5,00 lei/euro, iar cursul de la data emiterii facturii externe este de 4,95
##     lei/euro;
#
#    * creez un furnizor:
#      | organizatie | cif | nrc | tip      | telefon      | email             | mod_tva   | tara      | judet | oras | strada | numar | cod_postal | cont_bancar | detalii               |
#      | „BaBeB”     | -   | -   | supplier | 02 9876 5432 | contact@bebebe.au | facturare | Australia | -     | -    | -      | -     | -          | 062-001     | Zarzavat Bank BSB COD |
#
##    * inregistrez import de marfuri
#
#
##    * inregistrez tranzactii:
##      | data       | document                 | descriere                      | cont_debit | cont_credit | suma_debit | suma_credit |
##
##      | 2023-07-12 | Factura furnizor extern  | Înregistrare achiziție mărfuri | 371        | 401         | 24750.00   | 24750.00    |
##      | 2023-07-12 | Factura transport extern | Înregistrare transport         | 371        | 401         | 4950.00    | 4950.00     |
##
##      | 2023-07-12 | Document                 | Inregistrare taxe vamale       | 371        | 446         | 3000.00    | 3000.00     |
##      | 2023-07-12 | Document                 | Inregistrare comision vamal    | 371        | 446         | 150.00     | 150.00      |
##      | 2023-07-12 |                          | Inregistrare TVA import vamal  | 4426       | 446         | 6298.50    | 6298.50     |
##      | 2023-07-12 | Ordin de plată           | Plata datorii vamale           | 446        | 5121        | 3000.00    | 3000.00     |
##      | 2023-07-12 | Ordin de plată           | Plata comision vamal           | 446        | 5121        | 150.00     | 150.00      |
##      | 2023-07-12 | Ordin de plată           | Plata TVA import               | 446        | 5121        | 6298.50    | 6298.50     |
#
#    * inregistrez tranzactii:
#      | data       | document                          | descriere                                          | cont_debit | cont_credit | suma_debit | suma_credit |
#      | 2023-02-12 | Factura                           | Vânzare autoturism                                 | 461        | 7583        | 15000.00   | 15000.00    |
#      | 2023-02-12 | Factura                           | TVA Vanzare autoturism                             | 461        | 4427        | 2850.00    | 2850.00     |
#      | 2023-02-12 | Fișa mijlocului fix               | Scoatere din evidență autoturism. Amortizare       | 2813       | 2133        | 18000.00   | 18000.00    |
#      | 2023-02-12 | Fișa mijlocului fix               | Scoatere din evidență autoturism                   | 6583       | 2133        | 12000.00   | 12000.00    |
#      | 2023-05-12 | Contract de leasing               | Inregistrare contract de leasing                   | 2133       | 2133        | 95000.00   | 95000.00    |
##      | 2023-05-12 | Nota contabila                    | Evidentierea dobanzii                              | -          | 8051        | 14250.00   | 14250.00    |
#      | 2023-06-12 | Contract vânzare- cumpărare       | Vânzare acțiuni                                    | 461        | 7642        | 500.00     | 500.00      |
#      | 2023-06-12 | Contract vânzare- cumpărare       | Vânzare acțiuni                                    | 461        | 5081        | 125.00     | 125.00      |
#      | 2023-06-12 | Extras de cont                    | Comision bancar vanzare actiuni                    | 668        | 461         | 12.50      | 12.50       |
#      | 2023-06-12 | Jurnal de banca                   | Incasare prin virament bancar                      | 5121       | 461         | 12.50      | 12.50       |
#
#
#
#      | 2023-08-12 | Bon de consum                     | Consum materii prime                               | 601        | 301         | 2500.00    | 2500.00     |
#      | 2023-09-12 | Ordin de schimb valutar           | Înregistrare schimb valutar - vanzare la licitatie | 5125       | 5121        | 49000.00   | 49          |
#      | 2023-09-12 | Ordin de schimb valutar           | Înregistrare schimb valutar - cumparare valuta     | 5124       | 5125        | 49000.00   | 49000.      |
#      | 2023-09-12 | Ordin de plata in valuta          | Plata BeBeBe datorii furnizor                      | 401        | 5124        | 19800.00   | 19800.00    |
#      | 2023-09-12 | Ordin de plata in valuta          | Inregistrare diferenta favorabila de curs          | 401        | 7651        | 200.00     | 200.00      |
#      | 2023-09-12 | Extras bancar in valuta           | Înregistrare comision bancar                       | 627        | 5124        | 247.50     | 247.50      |
#      | 2023-12-12 | Registru de casa Stat de plata    | Plata salarii                                      | 421        | 5311        | 3542.00    | 3542.00     |
#      | 2023-12-12 | Factura furnizor extern           | Achizitie marfuri                                  | 371        | 401         | 53900.00   | 53900.00    |
#      | 2023-12-12 | Notă contabilă                    | Înregistrare taxă inversă                          | 4426       | 4427        | 10241.00   | 10241.00    |
#      | 2023-12-13 | Bon de predare                    | Obținere produs finit                              | 345        | 711         | 6000.00    | 6000.00     |
#      | 2023-12-13 | Bon fiscal                        | Plata furnizor                                     | 401        | 5311        | 384.00     | 384.00      |
#      | 2023-12-13 | Decont de cheltuieli              | Înregistrare bon fiscal combustibil                | 6022       | 401         | 322.70     | 322.70      |
#      | 2023-12-13 | Decont de cheltuieli              | Înregistrare TVA combustibil                       | 4426       | 4011        | 61.30      | 61.30       |
#      | 2023-12-13 | Factura vânzare                   | Vânzarea mărfurilor                                | 4111       | 707         | 4000.00    | 4000.00     |
#      | 2023-12-14 | Factura vânzare                   | TVA Vânzarea mărfurilor                            | 4111       | 4427        | 760.00     | 760.00      |
#      | 2023-12-14 | Bon consum                        | Scoatere din gestiune mărfurile                    | 607        | 371         | 2800.00    | 2800.00     |
#      | 2023-12-14 | Extras de cont in valuta          | Încasare client extern                             | 5124       | 4112        | 7200.00    | 7200.00     |
#      | 2023-12-15 | Extras de cont in valuta          | Încasare client extern                             | 5124       | 7651        | 255.00     | 255.00      |
#      | 2023-12-15 | Extras de cont in valuta          | Înregistrare comision bancar                       | 627        | 5121        | 500.00     | 500.00      |
#      | 2023-12-16 | Factura                           | Factură apă                                        | 6052       | 401         | 300.00     | 300.00      |
#      | 2023-12-16 | Factura                           | Factură apă TVA                                    | 4426       | 401         | 57.00      | 57.00       |
#      | 2023-12-16 | Factura                           | Ffactură energie electrică                         | 6051       | 401         | 400.00     | 400.00      |
#      | 2023-12-16 | Factura                           | Factură energie electrică TVA                      | 4426       | 401         | 76.00      | 76.00       |
#      | 2023-12-16 | Factura                           | Factură telefonie                                  | 626        | 401         | 500.00     | 500.00      |
#      | 2023-12-16 | Factura                           | Factură telefonie TVA                              | 4426       | 401         | 95.00      | 95.00       |
#      | 2023-12-16 | Factura                           | Inregistrare chirie datorată                       | 612        | 401         | 2000.00    | 2000.00     |
#      | 2023-12-16 | Factura                           | Inregistrare chirie datorată                       | 471        | 401         | 2000.00    | 2000.00     |
#      | 2023-12-16 | Factura                           | Inregistrare chirie datorată TVA                   | 4426       | 401         | 760.00     | 760.00      |
#      | 2023-12-19 | Ordin retragere numerar din banca | Retragere numerar                                  | 581        | 5121        | 2000.00    | 2000.00     |
#      | 2023-12-19 | Ștat de plata                     | Depunere în caserie                                | 5311       | 581         | 2000.00    | 2000.00     |
#      | 2023-12-19 | Registru de casa                  | Plată avansuri salariale                           | 425        | 5311        | 1500.00    | 1500.00     |
#      | 2023-12-20 | Factura                           | Plată furnizor apă                                 | 401        | 5311        | 357.00     | 357.00      |
#      | 2023-12-20 | Factura                           | Plată furnizor energie                             | 401        | 5311        | 476.00     | 476.00      |
#      | 2023-12-20 | Factura                           | Plată furnizor telefonie                           | 401        | 5311        | 595.00     | 595.00      |
#      | 2023-12-20 | Factura leasing                   | Rata I leasing                                     | 167        | 404         | 2375.00    | 2375.00     |
#      | 2023-12-21 | Factura leasing                   | Rata I leasing                                     | 666        | 404         | 490.00     | 490.00      |
#      | 2023-12-21 | Factura leasing                   | Rata I leasing                                     | 668        | 404         | 75.00      | 75.00       |
#      | 2023-12-21 | Factura leasing                   | Rata I leasing                                     | 4426       | 404         | 558.60     | 558.60      |
#      | 2023-12-22 | Ordin de plata                    | Plată datorii salariati                            | 4423       | 5121        | 9158.00    | 9158.00     |
#      | 2023-12-22 | Ordin de plata                    | Plată datorii salariati                            | 4315       | 5121        | 2188.00    | 2188.00     |
#      | 2023-12-22 | Ordin de plata                    | Plată datorii salariati                            | 4316       | 5121        | 175.00     | 175.00      |
#      | 2023-12-22 | Ordin de plata                    | Plată datorii salariati                            | 444        | 5121        | 608.00     | 608.00      |
#      | 2023-12-22 | Ordin de plata                    | Plată datorii salariati                            | 447        | 5121        | 38.00      | 38.00       |
#      | 2023-12-22 | Extras bancar                     | Comision bancar                                    | 627        | 5121        | 40.00      | 40.00       |
#      | 2023-12-22 | Dispozitie de incasare            | Incasare numerar din creanță                       | 5311       | 461         | 17850.00   | 17850.00    |
#      | 2023-12-22 | Factura avans                     | Înregistrare factură avans                         | 4091       | 4011        | 3000.00    | 3000.00     |
#      | 2023-12-22 | Factura avans                     | Înregistrare factură avans TVA                     | 4426       | 4011        | 570.00     | 570.00      |
#      | 2023-12-22 | Ordin de plata                    | Plata factură avans                                | 4011       | 5121        | 3570.00    | 3570.00     |
#      | 2023-12-22 | Factura vanzare                   | Vânzare produs finit                               | 4111       | 7015        | 10000.00   | 10000.00    |
#      | 2023-12-22 | Factura vanzare                   | Vânzare produs finit TVA                           | 4111       | 4427        | 1900.00    | 1900.00     |
#      | 2023-12-22 | bon de livrare                    | Livrare produse afinite                            | 711        | 345         | 3500.00    | 3500.00     |
#      | 2023-12-27 | Bilet la ordin                    | Acceptare bilet la ordin                           | 413        | 4111        | 11900.00   | 11900.00    |
#      | 2023-12-28 | Factura de vanzare                | Înregistrare factură externă                       | 4111       | 707         | 39200.00   | 39200.00    |
#      | 2023-12-28 | Bon de livrare                    | Livrare mărfuri din stoc                           | 607        | 371         | 15000.00   | 15000.00    |
#      | 2023-12-28 | Chitanta                          | Plată factură leasing I/comision bancar            | 404        | 5121        | 3498.00    | 3498.00     |
#      | 2023-12-28 | Chitanta                          | Plată factură leasing I/comision bancar            | 627        | 5121        | 15.00      | 15.00       |
#      | 2023-12-28 | Factura de vanzare                | Factură de servicii                                | 4111       | 704         | 50000.00   | 50000.00    |
#      | 2023-12-29 | Factura de vanzare                | Factură de servicii                                | 4111       | 4427        | 9500.00    | 9500.00     |
#      | 2023-12-31 |                                   | Încasare dobânzii                                  | 5121       | 766         | 10.00      | 10.00       |
#      | 2023-12-31 | Extras bancar                     | Comision bancar                                    | 627        | 5121        | 50.00      | 50.00       |
#      | 2023-12-31 | Notă contabilă                    | Inregistrare amortizare                            | 6811       | 2812        | 300.00     | 300.00      |
#      | 2023-12-31 | Notă contabilă                    | Inregistrare amortizare                            | 6811       | 2813        | 500.00     | 500.00      |
#      | 2023-12-31 | Notă contabilă                    | Inregistrare amortizare                            | 6811       | 2808        | 100.00     | 100.00      |
#      | 2023-12-31 | Notă contabilă                    | Inregistrare amortizare                            | 6811       | 2814        | 100.00     | 100.00      |
#      | 2023-12-31 |                                   | Înregistrare ștat de salarii                       | 641        | 421         | 11500.00   | 11500.00    |
#      | 2023-12-31 |                                   | Înregistrare ștat de salarii                       | 421        | 4315        | 2875.00    | 2875.00     |
#      | 2023-12-31 |                                   | Înregistrare ștat de salarii                       | 421        | 4316        | 1150.00    | 1150.00     |
#      | 2023-12-31 | Ștat de plata                     |                                                    | 421        | 444         | 663.00     | 663.00      |
#      | 2023-12-31 | Ștat de plata                     |                                                    | 6461       | 436         | 259.00     | 259.00      |
#      | 2023-12-31 | Ștat de plata                     | Lipsa inventar                                     | 601        | 301         | 400.00     | 400.00      |
#      | 2023-12-31 | Nota contabila                    | Ajustare inventar                                  | 635        | 4426        | 76.00      | 76.00       |
#      | 2023-12-31 |                                   | Depreciere marfurilor                              | 6814       | 397         | 1000.00    | 1000.00     |
#      | 2023-12-31 |                                   | Reevaluarea cheltuielilor de ajustare deprecieri   | 2961       | 7863        | 50000.00   | 50000.00    |
#      | 2023-12-31 | Ștat de plata                     | Acțiuniile din portofoliu                          | 6864       | 698         | 150.00     | 150.00      |
#      | 2023-12-31 | Notă contabilă                    | Actualizare creanta externa                        | 4112       | 7651        | 46.69      | 46.69       |
#      | 2023-12-31 | Notă contabilă                    | Actualizare creanta externa                        | 4112       | 7651        | 800.00     | 800.00      |
#      | 2023-12-31 | Notă contabilă                    | Actualizare creanta externa                        | 6651       | 401         | 140.00     | 140.00      |
#      | 2023-12-31 | Notă contabilă                    | Actualizare creanta externa                        | 6651       | 401         | 1870.00    | 1870.00     |
#      | 2023-12-31 | Notă contabilă                    | Actualizare creanta externa                        | 668        | 167         | 6240.00    | 6240.00     |