# language: ro
Functionalitate:  Inregistrari pentru luna decembrie

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie
    * creez un proiect:
      | nume | organizatie   | cif     | nrc           | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" S.A | R910910 | J40/65703/200 | proiect | 0721222333 | contact@abc.com | facturare | 4778     | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |

    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada      | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„AAA” SA | 3021130 | J29/777/1999 | afiliat | 0755623155 | contact@aaa.com | facturare | 6201     | Romania | Bucuresti | Bucuresti | Garofitelor | 112   | 031183     | RO50PORL888888286982666 | Zarzavat Bank |
    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„BBB” SA | 2255048 | J42/111/2006 | afiliat | 0763999882 | contact@bbb.com | facturare | 771      | Romania | Bucuresti | Bucuresti | Zambilelor | 11    | 031183     | RO50PORL777777286982666 | Zarzavat Bank |
    * creez o entitate afiliata:
      | organizatie  | cif     | nrc          | tip     | telefon     | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | S.C.„CCC” SA | 4589721 | J29/235/1989 | afiliat | 07442236666 | contact@ccc.com | facturare | 9003     | Romania | Bucuresti | Bucuresti | Liliacului | 76B   | 031183     | RO50PORL666666286980066 | Zarzavat Bank |


    * creez un furnizor:
      | organizatie            | cif     | nrc          | tip      | telefon    | email                     | mod_tva   | cod_caen | tara    | judet     | oras      | strada   | numar | cod_postal | cont_bancar             | detalii       |
      | „Happy Leasing” IFN SA | 3020048 | J29/777/1999 | supplier | 0721222333 | contact@happy-leasing.com | facturare | 4511     | Romania | Bucuresti | Bucuresti | Crinului | 220   | 031183     | RO50PORL739266286982666 | Zarzavat Bank |
    * creez un client:
      | organizatie   | cif     | nrc          | tip    | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada     | numar | cod_postal | cont_bancar             | detalii       |
      | SC. "ASS" S.A | 3020048 | J29/777/1999 | client | 0721112373 | contact@ass.com | facturare | 6611     | Romania | Bucuresti | Bucuresti | Ghioceilor | 17    | 031183     | RO50PORL739266211223366 | Zarzavat Bank |
    * creez un client agent:
      | nume    | prenume1 | prenume | telefon    | cnp     | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
      | Ionescu | -        | Emilian | 0721666555 | Emilian | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |
