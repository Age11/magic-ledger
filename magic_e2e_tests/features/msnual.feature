# language: ro
Functionalitate:  Inregistrari pentru luna mai

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie

    * creez un proiect:
      | nume | organizatie   | cif      | nrc            | tip     | cod_caen | telefon    | email           | mod_tva   | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" SRL | RO910910 | J40/65703/2000 | proiect | 471,4791 | 0721222333 | contact@abc.com | facturare | Romania | București | București | Panseluțelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |

#    * preiau balanta de verificare pentru "2023-11-01":
#      | cont | debit_initial | credit_initial | debit_cumulat | credit_cumulat |
#      | 1012 | 0.00          | 200.00         | 0.00          | 0.00           |
#      | 121  | 0.00          | 600.00         | 9067.00       | 10000.00       |
#      # Mijloc de transport și amortizare
#      | 2133 | 10000.00      | 0.00           | 0.00          | 0.00           |
#      | 2813 | 0.00          | 1000.00        | 0.00          | 0.00           |
#      #Mărfuri
#      | 371  | 2000.00       | 0.00           | 5000.00       | 6000.00        |
#      #Furnizori
#      | 401  | 0.00          | 10100.00       | 0.00          | 5950.00        |
#      | 4111 | 0.00          | 0.00           | 11900.00      | 10000.00       |
#      #Salarii
#      | 421  | 0.00          | 500.00         | 1650.00       | 3000.00        |
#      | 4315 | 0.00          | 100.00         | 100.00        | 750.00         |
#      | 4316 | 0.00          | 50.00          | 50.00         | 300.00         |
#      | 436  | 0.00          | 11.00          | 11.00         | 67.00          |
#      #TVA
#      | 4423 | 0.00          | 100.00         | 100.00        | 950.00         |
#      | 4426 | 0.00          | 0.00           | 950.00        | 950.00         |
#      | 4427 | 0.00          | 0.00           | 1900.00       | 1900.00        |
#      #Impozit pe venit de natura salarii
#      | 444  | 0.00          | 9.00           | 9.00          | 100.00         |
#      #Conturi
#      | 5121 | 500.00        | 0.00           | 10000.00      | 770.00         |
#      | 5311 | 170.00        | 0.00           | 0.00          | 0.00           |
#      #Cheltuieli
#      | 607  | 0.00          | 0.00           | 6000.00       | 6000.00        |
#      | 641  | 0.00          | 0.00           | 3000.00       | 3000.00        |
#      | 6461 | 0.00          | 0.00           | 67.00         | 67.00          |
#      #Venituri
#      | 707  | 0.00          | 0.00           | 10000.00      | 10000.00       |

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

#    * inchid luna "2023-11"


  #    02-12-2023 - În vederea amenajării unui spațiu nou de desfacere pentru marfă în cadrul unui centru comercial societatea comercială a închiriat un stand.
  #    Primește prima factură în valoare de 1.000 de lei  de la furnizorul „Alfa” SRL având seria 12345. Furnizorul aplică TVA în regim normal.

    * adaug tratament contabil pentru înregistrarea chiriei

    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 12345 | 2024-05-10   | 2024-05-13    | 2           | 1         | RON    | 1000.00         | 190.00      | V. M.        | primită     | plată     |

    * înregistrez un articol din factură:
      | nume_articol | descriere                          | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
      | chirie       | Chiria pentru punctul de desfacere | 1         | lună           | 1000.00     | 19       | 1          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii | serie_document | id_document |
      | 1         | 1000 | 2024-05-10         | 12345          | 1           |

#    # 05-12-2023
#
#    # Achiziționează 10 rafturi de mobilier de la furnizorul „Mobila” SRL pentru a schimba designul vitrinei în valoare totală de 5000 de lei.
#
    * adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA normal și dare în folosință
#
    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 78956 | 2024-05-10   | 2024-05-13    | 4           | 1         | RON    | 5000.00         | 950.00      | B. B.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol    | descriere                                         | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Rafturi Vitrină | Rafturi pentru amenajarea vitrinei, design modern | 10        | buc            | 500.00      | N/A          | 19       | 2           | 2          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii | serie_document | id_document |
      | 2         | 5000 | 2024-05-13         | 78956          | 2           |
#
#    # Pentru a echipa noul punct comercial societatea comercială achiziționează o casă de marcat de la furnizorul „DateCS” SRL în baza facturii 12859 în valoare de 1.500 lei.
#
    * adaug tratament contabil pentru Înregistrarea achiziției de obiecte de inventar de la furnizor cu regim TVA la încasare și dare în folosință
#
    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 12859 | 2024-05-10   | 2024-05-13    | 3           | 1         | RON    | 1500.00         | 285.00      | G. D.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol   | descriere             | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Casă de marcat | Casă de marcat DataCS | 1         | buc            | 1500        | N/A          | 19       | 2           | 3          |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii | serie_document | id_document |
      | 3         | 1500 | 2024-05-10         | 12859          | 3           |
#
#    #Pentru a se conforma cu regulile impuse de complexul comercial societatea achiziționează și un sistem de supraveghere și alarmă efracție de la „SUPRAVEGHERE” SRL, în baza facturii 6952 în valoare de 5.000 lei.
#
    * adaug tratament contabil pentru achiziția de active corporale de la furnizor de imobilizări regim TVA normal
#
    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 6952  | 2024-05-10   | 2024-05-13    | 3           | 1         | RON    | 5000.00         | 950.00      | G. D.        | primită     | plată     |

    * adaug o imobilizare corporala
      | asset_name          | tip_amortizare | valoare_initiala | valoare_inventar | valoare_curenta | durata_utilizare | data_achizitie | data_inregistrare | descriere                                 |
      | Sistem supraveghere | liniară        | 5000             | 5000             | 5000            | 72               | 2023-12        | 2023-12           | Sistem supraveghere complet Guards Guards |

    * creez tranzacții din șablon:
      | id_sablon | suma | data_inregistrarii | serie_document | id_document |
      | 4         | 5000 | 2024-05-10         | 6952           | 4           |
#
#
#  # 06-12-2023
#
#  # Achiziționează mărfuri sub forma anumitor articole de îmbrăcăminte de la furnizorul „TRICOUL” SRL în baza facturii 76953. Este vorba de 1000 de tricouri cu imprimeu la 20 de lei bucata, preț fără TVA.
#
    * creez un furnizor:
      | organizatie   | cif       | nrc          | tip      | telefon    | email                 | mod_tva   | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | „TRICOUL” SRL | 987456312 | J11/000/2000 | supplier | 0700000001 | contact@fz-tricou.com | facturare | Romania | Bucuresti | Bucuresti | Liliacului | 512   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |

    * adaug tratament contabil pentru achiziție de marfă de la furnizor regim tva normal
#
    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 76953 | 2024-05-10   | 2024-05-13    | 10          | 1         | RON    | 20000.00        | 3800.00     | G. D.        | primită     | plată     |

    * adaug un articol din factura in inventar:
      | nume_articol       | descriere                                         | cantitate | unitate_masura | pret_unitar | pret_vanzare | cota_tva | id_inventar | id_factura |
      | Tricouri imprimate | Tricouri cu imprimeu, 100% bumbac, diverse culori | 1000      | buc            | 20.00       | N/A          | 19       | 1           | 5          |

    * creez tranzacții din șablon:
      | id_sablon | suma     | data_inregistrarii | serie_document | id_document |
      | 5         | 20000.00 | 2024-05-10         | 76953          | 5           |
#
#  # 2023-12-10
#
#  # Vinde marfă clientului „Popescu” SRL eliberând factura 0001. Încasează suma de 5.000 lei prin casă și restul, până la 11.900 lei, prin bancă.
#
    * adaug tratament contabil pentru vânzare către client regim tva normal
#
    * adaug o factura:
      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
      | 00001 | 2024-05-10   | 2024-05-10    | 1           | 9         | RON    | 10000.00        | 1900.00     | G. A.        | emisă       | încasare  |

    * scad stocul de mărfuri:
      | id_articol | cantitate | id_gestiune | id_factura |
      | 5          | 200       | 1           | 6          |

    * creez tranzacții din șablon:
      | id_sablon | suma     | data_inregistrarii | serie_document | id_document |
      | 6         | 10000.00 | 2024-05-10         | 00001          | 6           |
#
    * adaug tratament contabil pentru descărcare din gestiunea de mărfuri
#
    * creez tranzacții din șablon:
      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
      | 7         | 4000.00 | 2024-05-10         | 00001          | 6           |
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 6        | 5000.00 |
#
    * adaug tratament contabil pentru incasare in casa de la client
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 8         | 5000.00 | 2023-12-10         | OP0001         | -1          |
#
#  # Decide să achite factura de chirie de la „Alfa” SRL utilizând numerar din casă.
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 1        | 1190.00 |
#
    * adaug tratament contabil pentru plata furnizor din casă
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 9         | 1190.00 | 2023-12-10         | 12345          | 1           |
#
#  # 2023-12-11
#    # Vinde marfă către o persoana fizică și încasează plata cu cardul pentru suma totală de 2.380 lei cu TVA .
#
    * adaug tratament contabil pentru vânzare către client regim tva normal cu încasare directă
#
#    * adaug o factura:
#      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
#      | 0001  | 2023-12-11   | 2023-12-31    | 1           | 9         | RON    | 2000.00         | 380.00      | G. A.        | emisă       | încasare  |
#
#    * scad stocul de mărfuri:
#      | id_articol | cantitate | id_gestiune | id_factura |
#      | 5          | 20        | 1           | 7          |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 10        | 2000.00 | 2023-12-11         | 0001           | 7           |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 7         | 400.00 | 2023-12-11         | BON0001         | -1          |
#
#   # 2023-12-12
#   # Încasează prin bancă creanța generată prin factura 0001 de la clientul  „Popescu” SRL.
    * adaug tratament contabil pentru incasare in cont de la client
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 6        | 6900.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 11        | 6900.00 | 2023-12-12         | 00001          | 6           |
#
#   # Achită prin bancă facturile 12859 și 6952 către „DateCS” SRL și „Supraveghere” SRL în valoare de 1.875 lei, respectiv 5.950 de lei.
#
    * adaug tratament contabil pentru plata furnizor din cont
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 4        | 5950.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 12        | 5950.00 | 2023-12-12         | 6952           | 4           |
#
#
    * adaug tratament contabil pentru plata furnizor din cont cu exigibilizare TVA
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 3        | 1785.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 13        | 1785.00 | 2023-12-12         | 12859          | 3           |
#
#  # 2023-12-15
## Primește factura de telefonie cu numărul 65897 în valoare de 200 de lei, pe care o achită din casă.
#    * adaug o factura:
#      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
#      | 65897 | 2023-12-11   | 2023-12-31    | 6           | 1         | RON    | 168.07          | 31.93       | T. M.        | primită     | plată     |
#
#    * înregistrez un articol din factură:
#      | nume_articol | descriere           | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
#      | telefonie    | Abonament telefonie | 1         | lună           | 168.07      | 19       | 8          |
#
    * adaug tratament contabil pentru înregistrarea cheltuielilor cu servicii poștale și cu telecomunicațiile
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 14        | 168.07 | 2023-12-15         | 65897          | 8           |
#
#    * rezolv plata:
#      | id_plata | suma   |
#      | 8        | 200.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 9         | 200.00 | 2023-12-15         | OP0003         | 3           |
#
#    # Achită din bancă factura 78956 către „Mobilă” SRL în valoare de 5950 de lei.
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 2        | 5950.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 12        | 5950.00 | 2023-12-15         | 78956          | 2           |
#
#    #Primește un împrumut pe termen scurt de la bancă în valoare de 10.000 de lei.
#
    * adaug tratament contabil pentru incasare credit pe termen scurt in cont
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma     | data_inregistrarii | serie_document | id_document |
#      | 15        | 10000.00 | 2023-12-15         | CTR20          | -1          |
#
#    * creez o plată:
#      | suma     | tip_plata | data_plata | data_scadenta | status     | id_factura | id_tranzactie |
#      | 10000.00 | încasare  | 2023-12-15 | 2023-12-31    | 2023-12-15 | -1         | 33            |
#
#    * rezolv plata:
#      | id_plata | suma     |
#      | 9        | 10000.00 |
#
#  # 2023-12-16
#    # 16-12-2023 - Achită parțial factura „76953” scadentă la 07-01-2024 către furnizorul de marfă în valoare de 5.000 lei.
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 12        | 5000.00 | 2023-12-16         | 76953          | 5           |
#
#    * rezolv plata:
#      | id_plata | suma    |
#      | 5        | 5000.00 |
#
#  # 2023-12-20
#    # Primește factura de la furnizorul de energie cu numărul 4567 în valoare de 654,50 lei
#
#    * adaug o factura:
#      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
#      | 4567  | 2023-12-20   | 2024-01-31    | 7           | 1         | RON    | 550.00          | 104.50      | E. E.        | primită     | plată     |
#
#    * înregistrez un articol din factură:
#      | nume_articol      | descriere          | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
#      | Energie electrică | Abonament + consum | 1         | lună           | 550.00      | 19       | 9          |
#
    * adaug tratament contabil pentru înregistrarea cheltuielilor cu energia
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 16        | 550.00 | 2023-12-20         | 4567           | 9           |
#
#  # 2023-12-21
#    # Primește din bancă contribuțiile salariale aferente lunii noiembrie în valoare de 1.267 de lei. Plătește TVA aferent lunii noiembrie în valoare de 950 de lei.
#
    * adaug tratament contabil pentru plata asigurării sociale
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 17       | 750.00 | 2023-12-21         | OP0003         | -1           |
#
    * adaug tratament contabil pentru plata asigurării sociale de sănătate
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 18        | 300.00 | 2023-12-21         | OP0005         | -1          |
#
    * adaug tratament contabil pentru plata contribuției asiguratorie de munca
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma  | data_inregistrarii | serie_document | id_document |
#      | 19        | 67.00 | 2023-12-21         | OP0007         | -1          |
#
    * adaug tratament contabil pentru plata impozitului pe venit de natura salariilor
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 20        | 100.00 | 2023-12-21         | OP0009         | -1          |
#
    * adaug tratament contabil pentru plata TVA de plată
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 21        | 950.00 | 2023-12-21         | OP0011         | -1          |
#
#  # 2023-12-23
#    # Primește factura de apă cu numărul 789 în valoare de 357 lei și achită din casă.
#
#    * adaug o factura:
#      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
#      | 789   | 2023-12-23   | 2024-01-31    | 8           | 1         | RON    | 300.00          | 57.00       | H. N.        | primită     | plată     |
#
#    * înregistrez un articol din factură:
#      | nume_articol | descriere          | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
#      | Apă          | Abonament + Consum | 1         | lună           | 300.00      | 19       | 10         |
#
    * adaug tratament contabil pentru înregistrarea cheltuielilor cu apa
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 22        | 300.00 | 2023-12-23         | 789            | 10          |
#
#    * rezolv plata:
#      | id_plata | suma   |
#      | 10       | 357.00 |
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 9         | 357.00 | 2023-12-23         | 789            | 10          |
#
## 2023-12-31
#
#    # Achiziționează servicii de întreținere pentru casa de marcat de la furnizorul „DataCS” SRL în baza facturii cu nr. 582 în valoare de 119 lei.
#
#    * adaug o factura:
#      | serie | data_factura | data_scadenta | id_furnizor | id_client | moneda | valoare_factura | valoare_tva | nume_emitent | tip_factura | tip_plata |
#      | 582   | 2023-12-31   | 2024-01-31    | 3           | 1         | RON    | 100.00          | 19.00       | C. M.        | primită     | plată     |
#
#    * înregistrez un articol din factură:
#      | nume_articol            | descriere                                  | cantitate | unitate_masura | pret_unitar | cota_tva | id_factura |
#      | Întreținere casă marcat | Evaluare periodică și curățare casă marcat | 1         | buc            | 100.00      | 19       | 11         |
#
    * adaug tratament contabil pentru achiziție de servicii de la furnizor regim tva la încasare
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 23        | 100.00 | 2023-12-31         | 582            | 11          |
#
    * adaug tratament contabil pentru înregistrarea cheltuielilor cu amortizarea imobilizărilor
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma   | data_inregistrarii | serie_document | id_document |
#      | 24        | 257.14 | 2023-12-31         | -1             | -1          |
#
#    # Înregistrează cheltuielile cu salariile în valoare de 2475 și impozitele aferente.
#
    * adaug tratament contabil pentru cheltuieli cu salariile fără normă întreagă
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 25        | 2475.00 | 2023-12-31         | ST0002         | -1          |
#
#
## Completare 2023-12-12 Plătește salariul din casă 1.850 de lei.
#
    * adaug tratament contabil pentru plata salarii din casă
#
#    * creez tranzacții din șablon:
#      | id_sablon | suma    | data_inregistrarii | serie_document | id_document |
#      | 26        | 1850.00 | 2023-12-12         | ST000          | -1          |
#
#
#
#
#
