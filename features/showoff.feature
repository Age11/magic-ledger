# language: ro
Functionalitate:  Inregistrari pentru luna decembrie

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie
    * creez un proiect:
      | nume | organizatie   | cif     | nrc           | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" S.A | R910910 | J40/65703/200 | proiect | 0721222333 | contact@abc.com | facturare | 4778     | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |

    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada      | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„AAA” SA | 3021130 | J29/777/1999 | afiliat | 0755623155 | contact@aaa.com | facturare | 6201     | Romania | Bucuresti | Bucuresti | Garofitelor | 112   | 031183     | RO50PORL888888286982666 | Zarzavat Bank |

    * adaug "actiuni" detinute la entitatea afiliata:
      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
      | S.C.„AAA” SA | 2              | 500       | 500            | 261           | 2021-09-01     |

    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„BBB” SA | 2255048 | J42/111/2006 | afiliat | 0763999882 | contact@bbb.com | facturare | 771      | Romania | Bucuresti | Bucuresti | Zambilelor | 11    | 031183     | RO50PORL777777286982666 | Zarzavat Bank |

    * adaug "titluri de plasament" detinute la entitatea afiliata:
      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
      | S.C.„BBB” SA | 3              | 100       | 20             | 5081          | 2022-11-01     |

    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon     | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„CCC” SA | 4589721 | J29/235/1989 | afiliat | 07442236666 | contact@ccc.com | facturare | 9003     | Romania | Bucuresti | Bucuresti | Liliacului | 76B   | 031183     | RO50PORL666666286980066 | Zarzavat Bank |

    * adaug "titluri de plasament" detinute la entitatea afiliata:
      | organizatie  | id_organizatie | cantitate | pret_achizitie | cont_analitic | data_achizitie |
      | S.C.„CCC” SA | 4              | 200       | 50             | 5081          | 2023-10-11     |

    * adaug o imobilizare corporala
      | asset_name         | clasa | cont_analitic | cont_analitic_amortizare | tip_amortizare | valoare_totala | durata_utilizare | data_achizitie | data_inregistrare | descriere                            |
      | masina tip A       | 21    | 2133          | 2813                     | liniara        | 30000          | 5                | 2020-10        | 2023-11           | renault clio, 2019, 1.5 diesel, 90cp |
      | cladire depozit    | 21    | 212           | 2812                     | liniara        | 180000         | 50               | 2014-07        | 2023-11           | cladire depozit, zona pipera         |
      | program informatic | 208   | 208           | 2808                     | liniara        | 3600           | 36               | 2021-04        | 2023-11           | program informatic gestiune depozit  |
      | program informatic | 214   | 214           | 2814                     | liniara        | 4800           | 48               | 2023-06        | 2023-11           | mobilier de birou                    |

    * actualizez rezerva de valuta:
      | moneda | cantitate | pret_achizitie | cont_analitic | data_achizitie |
      | EUR    | 10417     | 4.799          | 5124          | 2023-09-01     |

    * preiau balanta de verificare pentru luna "2023-11":
      | cont | debit_initial | credit_initial | debit      | credit    |
      | 1012 | 0.00          | 220000.00      | 0.00       | 0.00      |
      | 1061 | 0.00          | 5000.00        | 0.00       | 0.00      |
      | 1068 | 0.00          | 100000.00      | 0.00       | 0.00      |
      | 117  | 0.00          | 60000.00       | 0.00       | 25000.00  |
      | 121  | 0.00          | 30000.00       | 30000.00   | 0.00      |
      | 121  | 596710.00     | 728000.00      | 93851.00   | 119000.00 |
      | 129  | 5000.00       | 5000.00        | 0.00       | 0.00      |
      | 208  | 3600.00       | 0.00           | 0.00       | 0.00      |
      | 212  | 180000.00     | 0.00           | 0.00       | 0.00      |
      | 2133 | 30000.00      | 0.00           | 0.00       | 0.00      |
      | 214  | 4800.00       | 0.00           | 0.00       | 0.00      |
      | 261  | 250000.00     | 0.00           | 0.00       | 0.00      |
      | 2808 | 0.00          | 2900.00        | 0.00       | 100.00    |
      | 2812 | 0.00          | 33000.00       | 0.00       | 300.00    |
      | 2813 | 0.00          | 12500.00       | 0.00       | 5500.00   |
      | 2814 | 0.00          | 300.00         | 0.00       | 100.00    |
      | 2961 | 0.00          | 50000.00       | 0.00       | 0.00      |
      | 301  | 37500.00      | 30000.00       | 7500.00    | 12000.00  |
      | 303  | 0.00          | 0.00           | 2500.00    | 2500.00   |
      | 345  | 15000.00      | 15000.00       | 15000.00   | 15000.00  |
      | 371  | 15000.00      | 15000.00       | 350000.00  | 310000.00 |
      | 4011 | 0.00          | 0.00           | 470700.00  | 917205.00 |
      | 404  | 0.00          | 28200.00       | 0.00       | 0.00      |
      | 4091 | 12000.00      | 0.00           | 0.00       | 12000.00  |
      | 4092 | 16000.00      | 0.00           | 0.00       | 16000.00  |
      | 4111 | 0.00          | 0.00           | 1020800.00 | 450000.00 |
      | 4112 | 18000.00      | 0.00           | 0.00       | 10000.00  |
      | 421  | 0.00          | 0.00           | 51458.00   | 55000.00  |
      | 425  | 0.00          | 0.00           | 1000.00    | 1000.00   |
      | 4315 | 0.00          | 0.00           | 21880.00   | 24064.00  |
      | 4316 | 0.00          | 0.00           | 1750.00    | 1925.00   |
      | 436  | 0.00          | 0.00           | 113.00     | 113.00    |
      | 441  | 0.00          | 0.00           | 9500.00    | 9500.00   |
      | 4423 | 0.00          | 0.00           | 61142.00   | 70300.00  |
      | 4426 | 0.00          | 0.00           | 13072.00   | 13072.00  |
      | 4427 | 0.00          | 0.00           | 22230.00   | 22230.00  |
      | 444  | 0.00          | 0.00           | 6080.00    | 6688.00   |
      | 447  | 0.00          | 0.00           | 380.00     | 418.00    |
      | 471  | 0.00          | 0.00           | 5500.00    | 2300.00   |
      | 508  | 0.00          | 0.00           | 12000.00   | 0.00      |
      | 5121 | 0.00          | 0.00           | 840401.00  | 576252.00 |
      | 5124 | 0.00          | 0.00           | 50000.00   | 0.00      |
      | 5191 | 0.00          | 0.00           | 0.00       | 300000.00 |
      | 5311 | 0.00          | 0.00           | 162000.00  | 120000.00 |
      | 581  | 0.00          | 0.00           | 13000.00   | 13000.00  |
      | 601  | 0.00          | 0.00           | 12000.00   | 12000.00  |
      | 6022 | 0.00          | 0.00           | 2000.00    | 2000.00   |
      | 603  | 0.00          | 0.00           | 2500.00    | 2500.00   |
      | 604  | 0.00          | 0.00           | 1000.00    | 1000.00   |
      | 6051 | 0.00          | 0.00           | 300.00     | 300.00    |
      | 6052 | 0.00          | 0.00           | 500.00     | 500.00    |
      | 607  | 0.00          | 0.00           | 32000.00   | 32000.00  |
      | 611  | 0.00          | 0.00           | 6000.00    | 6000.00   |
      | 612  | 0.00          | 0.00           | 3000.00    | 3000.00   |
      | 613  | 0.00          | 0.00           | 3000.00    | 3000.00   |
      | 623  | 0.00          | 0.00           | 2500.00    | 2500.00   |
      | 626  | 0.00          | 0.00           | 1000.00    | 1000.00   |
      | 627  | 0.00          | 0.00           | 1400.00    | 1400.00   |
      | 628  | 0.00          | 0.00           | 9000.00    | 9000.00   |
      | 635  | 0.00          | 0.00           | 38.00      | 38.00     |
      | 641  | 0.00          | 0.00           | 10000.00   | 10000.00  |
      | 636  | 0.00          | 0.00           | 113.00     | 113.00    |
      | 6581 | 0.00          | 0.00           | 3000.00    | 3000.00   |
      | 6584 | 0.00          | 0.00           | 2000.00    | 2000.00   |
      | 6588 | 0.00          | 0.00           | 0.00       | 0.00      |
      | 6651 | 0.00          | 0.00           | 1500.00    | 1500.00   |
      | 6811 | 0.00          | 0.00           | 1000.00    | 1000.00   |
      | 691  | 10.00         | 10.00          | 0.00       | 0.00      |
      | 7015 | 0.00          | 0.00           | 22000.00   | 22000.00  |
      | 704  | 0.00          | 0.00           | 50000.00   | 50000.00  |
      | 707  | 0.00          | 0.00           | 45000.00   | 45000.00  |
      | 711  | 0.00          | 0.00           | 15000.00   | 15000.00  |
      | 7588 | 0.00          | 0.00           | 1200.00    | 1200.00   |
      | 761  | 0.00          | 0.00           | 0.00       | 0.00      |
      | 7651 | 0.00          | 0.00           | 0.00       | 0.00      |
      | 766  | 0.00          | 0.00           | 800.00     | 800.00    |

    * inchid luna "2023-11"

    * creez un furnizor:
      | organizatie            | cif     | nrc          | tip      | telefon    | email                     | mod_tva   | cod_caen | tara    | judet     | oras      | strada   | numar | cod_postal | cont_bancar             | detalii       |
      | „Happy Leasing” IFN SA | 3020048 | J29/777/1999 | supplier | 0721222333 | contact@happy-leasing.com | facturare | 4511     | Romania | Bucuresti | Bucuresti | Crinului | 220   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |
    * creez un client:
      | organizatie   | cif     | nrc          | tip    | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | SC. "ASS" S.A | 3020048 | J29/777/1999 | client | 0721112373 | contact@ass.com | facturare | 6611     | Romania | Bucuresti | Bucuresti | Ghioceilor | 17    | 031183     | RO50PORL739266211223366 | Zarzavat Bank |
    * creez un client agent:
      | nume    | prenume1 | prenume | telefon    | cnp     | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
      | Ionescu | -        | Emilian | 0721666555 | Emilian | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |
