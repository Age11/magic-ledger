test_data = {
  "organizations": [
    {
      "name": "test",
      "cif": "1234567890",
      "nrc": "1234567890",
      "phone": "1234567890",
      "email": "asdasd@asd.com",
      "vat_mode": "on_invoice",
      "status": "active",
      "type": "project",
      "caen_code": "1234"
    },
    {
      "name": "CARMEN IMPEX TM SRL",
      "cif": "5420048",
      "nrc": "J29/747/1994",
      "phone": "0721222222",
      "email": "contact@carmenimpextm.com",
      "vat_mode": "on_invoice",
      "status": "active",
      "type": "project",
      "caen_code": "4941"
    },
    {
      "name": "ADA ONLINE SRL",
      "cif": "31845110",
      "nrc": "J01/375/2013",
      "phone": "0721222223",
      "email": "contact@ada.com",
      "vat_mode": "on_cash_in",
      "status": "active",
      "type": "supplier",
      "caen_code": "4791"
    }
  ],
  "address": [
    {
      "country": "Romania",
      "stat_or_province": "Bucuresti",
      "city": "Bucuresti",
      "street": "Strada",
      "apartment_or_suite": "1",
      "postal_code": "123456",
      "organization_id": "org_id"
    },
    {
      "country": "Romania",
      "stat_or_province": "Prahova",
      "city": "Sinaia",
      "street": "Stanjeneilor",
      "apartment_or_suite": "16",
      "postal_code": "106100",
      "organization_id": "org_id"
    },
    {
      "country": "Romania",
      "stat_or_province": "Alba",
      "city": "Petresti",
      "street": "1 Mai",
      "apartment_or_suite": "308 Et. P Ap. 8",
      "postal_code": "515850",
      "organization_id": "org_id"
    }
  ],
  "banking_details": [
    {
      "account": "test",
      "details": "test",
      "organization_id": "org_id"
    },
    {
      "account": "RO49AAAA1B31007593840000",
      "details": "AAAA BANK",
      "organization_id": "org_id"
    }
  ],
  "inventory": [
    {
      "inv_type": "stock",
      "name": "test",
      "description": "test",
      "inventory_method": "fifo",
      "organization_id": "org_id"
    },
    {
      "inv_type": "stock",
      "name": "inventar marfuri",
      "description": "inventar marfuri",
      "inventory_method": "fifo",
      "organization_id": "org_id"
    }
  ],
  "invoices": [
    {
      "inv_type": "invoice",
      "number": "0001",
      "serial": "FF",
      "issue_date": "2020-01-01",
      "receive_date": "2020-01-01",
      "due_date": "2020-01-01",
      "payment_status": "paid",
      "organization_id": "org_id",
      "supplier_id": "supplier_id",
      "client_id": "client_id",
      "currency": "RON",
      "amount": "100",
      "issuer_name": "issuer_name"
    }
  ],
  "items": [
    {
      "name": "test",
      "description": "test",
      "quantity": "1",
      "measurement_unit": "buc",
      "acquisition_price": "100",
      "inventory_id": "inventory_id",
      "total_value": 100
    },
    {
      "name": "paracetamol",
      "description": "medicament",
      "quantity": "1",
      "measurement_unit": "cutie",
      "acquisition_price": "100",
      "inventory_id": "inventory_id",
      "total_value": 100
    }
  ]
}