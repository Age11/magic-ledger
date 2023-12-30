# language: ro
Functionalitate:  Inregistrari pentru luna decembrie

  Scenariu: Inregistrari necesare pentru a descrie activitatea derulata in luna decembrie
    * creez un proiect nou:
      | nume | organizatie   | cif     | nrc          | tip     | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABC  | SC. "ABC" S.A | 3020048 | J29/777/1999 | proiect | 0721222333 | contact@abc.com | facturare | 4778     | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |
    * creez un furnizor nou:
      | nume | organizatie   | cif     | nrc          | tip      | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ABL  | SC. "ABL" S.A | 3020048 | J29/777/1999 | supplier | 0721222333 | contact@abc.com | facturare | 4778     | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |
    * creez un client nou:
      | nume | organizatie   | cif     | nrc          | tip    | telefon    | email           | mod_tva   | cod_caen | tara    | judet     | oras      | strada       | numar | cod_postal | cont_bancar             | detalii       |
      | ASS  | SC. "ASS" S.A | 3020048 | J29/777/1999 | client | 0721222333 | contact@abc.com | facturare | 4778     | Romania | Bucuresti | Bucuresti | Panselutelor | 12    | 031183     | RO50PORL739266286982387 | Zarzavat Bank |
    * creez un client agent nou:
      | nume    | prenume1 | prenume | telefon    | cnp          | tara    | judet   | oras   | strada | numar | cod_postal | email            | cont                     | detalii  |
      | Emilian | -        | Emil    | 0721666555 | 191221445678 | Romania | Prahova | Sinaia | Strazi | 99    | 106100     | ionemi@email.com | RO49AAAA1B31007593840001 | AAA BANK |
