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


    #preluarea balantei initiale


    * creez un furnizor:
      | organizatie            | cif     | nrc          | tip      | telefon    | email                     | mod_tva   | cod_caen | tara    | judet     | oras      | strada   | numar | cod_postal | cont_bancar             | detalii       |
      | „Happy Leasing” IFN SA | 3020048 | J29/777/1999 | supplier | 0721222333 | contact@happy-leasing.com | facturare | 4511     | Romania | Bucuresti | Bucuresti | Crinului | 220   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |
    * creez un client:
      | organizatie   | cif     | nrc          | tip    | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | SC. "ASS" S.A | 3020048 | J29/777/1999 | client | 0721112373 | contact@ass.com | facturare | 6611     | Romania | Bucuresti | Bucuresti | Ghioceilor | 17    | 031183     | RO50PORL739266211223366 | Zarzavat Bank |
    * creez un client agent:
      | nume    | prenume1 | prenume | telefon    | cnp     | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
      | Ionescu | -        | Emilian | 0721666555 | Emilian | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |
