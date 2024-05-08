# language: ro
Functionalitate:  Inregistrari pentru luna decembrie

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie

    * creez un proiect:
      | nume | organizatie   | cif      | nrc            | tip     | cod_caen | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" SRL | RO910910 | J40/65703/2000 | proiect | 471,4791 | 0721222333 | contact@abc.com | facturare | Romania | București | București | Panseluțelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |

    * preiau balanta de verificare pentru "2023-11-01":
      | cont | debit_initial | credit_initial | debit_cumulat | credit_cumulat |
      | 1012 | 0.00          | 200.00         | 0.00          | 0.00           |
      | 121  | 0.00          | 600.00         | 9067.00       | 10000.00       |
      # Mijloc de transport și amortizare
      | 2133 | 10000.00      | 0.00           | 0.00          | 0.00           |
      | 2813 | 0.00          | 1000.00        | 0.00          | 0.00           |
      #Mărfuri
      | 371  | 2000.00       | 0.00           | 5000.00       | 6000.00        |
      #Furnizori
      | 401  | 0.00          | 10100.00       | 0.00          | 5950.00        |
      | 4111 | 0.00          | 0.00           | 11900.00      | 10000.00       |
      #Salarii
      | 421  | 0.00          | 500.00         | 1650.00       | 3000.00        |
      | 4315 | 0.00          | 100.00         | 100.00        | 750.00         |
      | 4316 | 0.00          | 50.00          | 50.00         | 300.00         |
      | 436  | 0.00          | 11.00          | 11.00         | 67.00          |
      #TVA
      | 4423 | 0.00          | 100.00         | 100.00        | 950.00         |
      | 4426 | 0.00          | 0.00           | 950.00        | 950.00         |
      | 4427 | 0.00          | 0.00           | 1900.00       | 1900.00        |
      #Impozit pe venit de natura salarii
      | 4427 | 0.00          | 9.00           | 9.00          | 100.00         |
      #Conturi
      | 5121 | 500.00        | 0.00           | 10000.00      | 770.00         |
      | 5311 | 170.00        | 0.00           | 0.00          | 0.00           |
      #Cheltuieli
      | 607  | 0.00          | 0.00           | 6000.00       | 6000.00        |
      | 641  | 0.00          | 0.00           | 3000.00       | 3000.00        |
      | 6461 | 0.00          | 0.00           | 67.00         | 67.00          |
      #Venituri
      | 707  | 0.00          | 0.00           | 10000.00      | 10000.00       |

    * creez un furnizor:
      | organizatie | cif      | nrc          | tip      | telefon    | email                   | mod_tva   | tara    | judet     | oras      | strada   | numar | cod_postal | cont_bancar             | detalii       |
      | „ALFA” SRL  | 12345678 | J11/123/2005 | supplier | 0700100100 | contact@alfa-people.com | facturare | Romania | Bucuresti | Bucuresti | Crinului | 256   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie  | cif     | nrc          | tip      | telefon    | email            | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | „DATECS” SRL | 1289745 | J11/757/1993 | supplier | 0752223667 | office@datec.com | facturare | Romania | Bucuresti | Bucuresti | Margaretei | 81    | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie  | cif    | nrc          | tip      | telefon    | email              | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | „MOBILA” SRL | 859647 | J11/663/2011 | supplier | 0769320676 | vanzari@mobila.com | facturare | Romania | Bucuresti | Bucuresti | Liliacului | 16    | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie        | cif    | nrc          | tip      | telefon    | email                 | mod_tva   | tara    | judet     | oras      | strada    | numar | cod_postal | cont_bancar             | detalii       |
      | „SUPRAVEGHERE” SRL | 852369 | J11/000/2000 | supplier | 0722321727 | vanzari@supra-spy.com | facturare | Romania | Bucuresti | Bucuresti | Garofitei | 225   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie        | cif      | nrc          | tip      | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada    | numar | cod_postal | cont_bancar             | detalii       |
      | „TELEINTERNET” SRL | 85469725 | J22/222/2002 | supplier | 0720322588 | office@tnet.com | facturare | Romania | Bucuresti | Bucuresti | Bujorului | 121   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie   | cif    | nrc          | tip      | telefon    | email               | mod_tva   | tara    | judet     | oras      | strada    | numar | cod_postal | cont_bancar             | detalii       |
      | „ENERGIA” SRL | 456789 | J33/333/2003 | supplier | 0721775223 | support@energia.com | facturare | Romania | Bucuresti | Bucuresti | Lalelelor | 64    | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * creez un furnizor:
      | organizatie | cif   | nrc          | tip      | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada    | numar | cod_postal | cont_bancar             | detalii       |
      | „HIDRO” SRL | 78569 | J44/444/2004 | supplier | 0723554488 | hidro@hidro.com | facturare | Romania | Bucuresti | Bucuresti | Lalelelor | 64    | 031183     | RO50PORL739266286982666 | Zarzavat Bank |


    * creez o gestiune:
      | nume    | descriere              | metoda_inventariere |
      | mărfuri | mărfuri  petru vânzare | fifo                |

    * creez o gestiune:
      | nume             | descriere           | metoda_inventariere |
      | obiecte inventar | obiecte de inventar | fifo                |

    * adaug un articol in inventar:
      | nume_articol | descriere                                 | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | data_achizitie |
      | Tricou mov   | tricou bumbac 100% multicolor cu imprimeu | 100       | buc            | 10.00       | 20.00        | 19       | 1           | 2023-03-01     |

    * adaug o imobilizare corporala
      | asset_name    | tip_amortizare | valoare_initiala | valoare_inventar | valoare_curenta | durata_utilizare | data_achizitie | data_inregistrare | descriere                              |
      | Autoutilitară | liniară        | 10000            | 10000            | 9000            | 48               | 2022-09        | 2023-11           | Renault Kangoo, 2015, 1.4 diesel, 75CP |

    * creez un client:
      | organizatie       | cif      | nrc          | tip    | telefon    | email                 | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | SC. "POPESCU" SRL | 12345689 | J11/999/1999 | client | 0755666999 | popescu1999@gmail.com | facturare | Romania | Bucuresti | Bucuresti | Ghioceilor | 17    | 031183     | RO50PORL739266211223366 | Zarzavat Bank |

    * creez un client agent:
      | nume    | prenume | telefon    | cnp     | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
      | Ionescu | Emilian | 0721666555 | Emilian | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |

    * inchid luna "2023-11"

    # 2023-12-02

    * adaug tratament contabil pentru înregistrarea chiriei

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 12345 | 2023-12-02   | 2023-12-31    | 2           | 1         | RON    | 1000.00         | 190.00      | V. M.        | primită     | plată     |

    * înregistrez un articol din factură:
      | nume_articol | descriere                          | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
      | chirie       | Chiria pentru punctul de desfacere | 1         | lună           | 1000.00     | 19       | 1          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii |
      | 1         | 1000 | 2023-12-02         |

    # 2023-12-05

    * adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA normal și dare în folosință

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 78956 | 2023-12-05   | 2023-12-31    | 4           | 1         | RON    | 5000.00         | 950.00      | B. B.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol    | descriere                                         | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Rafturi Vitrină | Rafturi pentru amenajarea vitrinei, design modern | 10        | buc            | 500.00      | N/A          | 19       | 2           | 2          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii |
      | 2         | 5000 | 2023-12-05         |


    * adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA la încasare și dare în folosință

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 12859 | 2023-12-05   | 2023-12-31    | 3           | 1         | RON    | 1500.00         | 285.00      | G. D.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol   | descriere             | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Casă de marcat | Casă de marcat DataCS | 1         | buc            | 1500        | N/A          | 19       | 2           | 3          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii |
      | 3         | 1500 | 2023-12-05         |


    * adaug tratament contabil pentru achiziția de active corporale de la furnizor de imobilizări regim TVA normal

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 6952  | 2023-12-05   | 2023-12-31    | 3           | 1         | RON    | 5000.00         | 950.00      | G. D.        | primită     | plată     |

    * adaug o imobilizare corporala
      | asset_name          | tip_amortizare | valoare_initiala | valoare_inventar | valoare_curenta | durata_utilizare | data_achizitie | data_inregistrare | descriere                                 |
      | Sistem supraveghere | liniară        | 5000             | 5000             | 5000            | 72               | 2023-12        | 2023-12           | Sistem supraveghere complet Guards Guards |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii |
      | 4         | 5000 | 2023-12-05         |


  # 2023-12-06

    * adaug tratament contabil pentru achiziție de marfă de la furnizor regim tva normal

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 76953 | 2023-12-06   | 2023-12-31    | 3           | 1         | RON    | 20000.00        | 3800.00     | G. D.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol       | descriere                                         | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Tricouri imprimate | Tricouri cu imprimeu, 100% bumbac, diverse culori | 1000      | buc            | 20.00       | N/A          | 19       | 1           | 5          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii |
      | 5         | 1500 | 2023-12-06         |

  # 2023-12-10

    * adaug tratament contabil pentru vânzare către client regim tva normal

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 00001 | 2023-12-10   | 2023-12-31    | 1           | 9         | RON    | 10000.00        | 1900.00     | G. A.        | emisă       | încasare  |

    * scad stocul de mărfuri:
      | id_articol | cantitate | id_gestiune | id_factura |
      | 5          | 200       | 1           | 6          |

    * creez tranzacții din șablon:
      | id_sablon | suma     | data_inregistrarii |
      | 6         | 10000.00 | 2023-12-10         |

    * adaug tratament contabil pentru descărcare din gestiunea de mărfuri

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 7         | 4000.00 | 2023-12-10         |

    * rezolv plata:
      | id_plata | suma    |
      | 6        | 5000.00 |

    * adaug tratament contabil pentru incasare in casa de la client

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 8         | 5000.00 | 2023-12-10         |

    * rezolv plata:
      | id_plata | suma    |
      | 1        | 1190.00 |

    * adaug tratament contabil pentru plata furnizor din casă

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 9         | 1190.00 | 2023-12-10         |

  # 2023-12-11

    * adaug tratament contabil pentru vânzare către client regim tva normal cu încasare directă

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 0001  | 2023-12-11   | 2023-12-31    | 1           | 9         | RON    | 2000.00         | 380.00      | G. A.        | emisă       | încasare  |

    * scad stocul de mărfuri:
      | id_articol | cantitate | id_gestiune | id_factura |
      | 5          | 20        | 1           | 7          |

    * creez tranzacții din șablon:
      | id_sablon | suma   | data_inregistrarii |
      | 7         | 400.00 | 2023-12-11         |

  # 2023-12-12

    * adaug tratament contabil pentru incasare in cont de la client

    * rezolv plata:
      | id_plata | suma    |
      | 6        | 6900.00 |

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 10        | 6190.00 | 2023-12-12         |

    * adaug tratament contabil pentru plata furnizor din cont

    * rezolv plata:
      | id_plata | suma    |
      | 4        | 5950.00 |

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 11        | 5950.00 | 2023-12-12         |

    * adaug tratament contabil pentru plata furnizor din cont cu exigibilizare TVA

    * rezolv plata:
      | id_plata | suma    |
      | 3        | 1785.00 |

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 12        | 1785.00 | 2023-12-12         |

  # 2023-12-15

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 65897 | 2023-12-11   | 2023-12-31    | 6           | 1         | RON    | 168.07          | 31.93      | T. M.        | primită       | plată  |

    * înregistrez un articol din factură:
      | nume_articol | descriere           | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
      | telefonie    | Abonament telefonie | 1         | lună           | 168.07      | 19       | 8          |

    * adaug tratament contabil pentru înregistrarea cheltuielilor cu servicii poștale și cu telecomunicațiile

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 13        | 168.07  | 2023-12-15         |

    * rezolv plata:
      | id_plata | suma    |
      | 8        | 200.00  |

    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii |
      | 9         | 200.00  | 2023-12-15         |

    * rezolv plata:
      | id_plata | suma    |
      | 2        | 5950.00  |

    * creez tranzacții din șablon:
      | id_sablon | suma     | data_inregistrarii |
      | 11        | 5950.00  | 2023-12-15         |

    # 2023-12-20


#    * adaug tratament contabil pentru înregistrarea cheltuielilor cu apa
#
#    * adaug tratament contabil pentru înregistrarea cheltuielilor cu energia
#
#    * adaug tratament contabil pentru înregistrarea cheltuielilor cu servicii poștale și cu telecomunicațiile
#
#    * adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA normal și dare în folosință
#
#    * adaug tratament contabil pentru achiziția de active corporale de la furnizor de imobilizări regim TVA normal
#
#    * adaug tratament contabil pentru plata salariilor
#
#    * adaug tratament contabil pentru vanzare catre client regim tva normal
#
#    * adaug tratament contabil pentru incasare in cont de la client
#
#    * adaug tratament contabil pentru incasare in casa de la client
#
#    * adaug tratament contabil pentru plata furnizor din cont
#
#    * adaug tratament contabil pentru plata furnizor din casă
#
#    * adaug tratament contabil pentru descarcare din gestiunea de marfuri
#
#    * adaug tratament contabil pentru înregistrarea achiziției de materiale consumabile
#
#    * adaug tratament contabil pentru înregistrarea achiziției de materiale consumabile cu TVA la încasare
#
#    * adaug tratament contabil pentru înregistrarea achiziției de imobilizări corporale
#
#    * adaug tratament contabil pentru înregistrarea cheltuielilor cu uzura



