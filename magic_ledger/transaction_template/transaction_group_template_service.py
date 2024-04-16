from magic_ledger import db
from magic_ledger.transaction_template.models.GTTFollowupTransaction import (
    GTTFollowupTransaction,
)
from magic_ledger.transaction_template.models.GroupTransactionTemplate import (
    GroupTransactionTemplate,
)
from magic_ledger.transaction_template.models.GTTMainTransaction import (
    GTTMainTransaction,
)
from magic_ledger.transactions.transaction_service import (
    create_transaction_and_update_balance,
)


def create_transaction_group_template(request_body, project_id):
    main_transaction = GTTMainTransaction(**request_body["main_transaction"])
    db.session.add(main_transaction)
    db.session.commit()
    followup_transactions = [
        GTTFollowupTransaction(main_transaction_id=main_transaction.id, **transaction)
        for transaction in request_body["followup_transactions"]
    ]
    db.session.add_all(followup_transactions)
    db.session.commit()

    transaction_group_template = GroupTransactionTemplate(
        name=request_body["name"],
        owner_id=project_id,
        description=request_body["description"],
        main_transaction_id=main_transaction.id,
    )
    db.session.add(transaction_group_template)
    db.session.commit()
    return transaction_group_template


def retrieve_all_transaction_group_templates(project_id):
    gtts = GroupTransactionTemplate.query.filter_by(owner_id=project_id).all()
    for gtt in gtts:
        gtt.main_transaction = GTTMainTransaction.query.filter_by(
            id=gtt.main_transaction_id
        ).first()
        gtt.followup_transactions = GTTFollowupTransaction.query.filter_by(
            main_transaction_id=gtt.main_transaction_id
        ).all()
    return gtts


def retrieve_all_transaction_group_templates_by_type(project_id, tx_type):
    gtts = GroupTransactionTemplate.query.filter_by(owner_id=project_id).all()
    res = []
    for gtt in gtts:
        gtt.main_transaction = GTTMainTransaction.query.filter_by(
            id=gtt.main_transaction_id
        ).first()
        gtt.followup_transactions = GTTFollowupTransaction.query.filter_by(
            main_transaction_id=gtt.main_transaction_id
        ).all()
        if gtt.main_transaction.tx_type == tx_type:
            res.append(gtt)
    return res


def transaction_group_templates_by_type(project_id, tx_type):
    gtts = GroupTransactionTemplate.query.filter_by(owner_id=project_id).all()
    res = []
    for gtt in gtts:
        gtt.main_transaction = GTTMainTransaction.query.filter_by(
            id=gtt.main_transaction_id
        ).first()
        gtt.followup_transactions = GTTFollowupTransaction.query.filter_by(
            main_transaction_id=gtt.main_transaction_id
        ).all()
        if gtt.main_transaction.tx_type in tx_type:
            res.append(gtt)
    return res


def generate_transactions_from_template(
    transaction_group_template_id, owner_id, request_body
):
    # find group template by id
    # get main transaction using the id from the group template
    # get followup transactions using the id from the main transaction
    tgt = GroupTransactionTemplate.query.filter_by(
        id=transaction_group_template_id
    ).first()
    mt = GTTMainTransaction.query.filter_by(id=tgt.id).first()
    ft = GTTFollowupTransaction.query.filter_by(main_transaction_id=mt.id).all()

    # create a transaction for the main transaction
    # create a transaction for each followup transaction
    if "invoice_id" not in request_body.keys():
        invoice_id = "None"
    else:
        invoice_id = request_body["invoice_id"]
    resp = []

    resp.append(
        create_transaction_and_update_balance(
            {
                "debit_account": mt.debit_account,
                "credit_account": mt.credit_account,
                "currency": mt.currency,
                "debit_amount": request_body["amount"],
                "credit_amount": request_body["amount"],
                "transaction_date": request_body["transaction_date"],
                "details": mt.details,
                "owner_id": owner_id,
                "tx_type": mt.tx_type,
                "invoice_id": invoice_id,
            }
        )
    )

    for transaction in ft:
        resp.append(
            create_transaction_and_update_balance(
                {
                    "debit_account": transaction.debit_account,
                    "credit_account": transaction.credit_account,
                    "currency": mt.currency,
                    "debit_amount": eval(
                        str(request_body["amount"]) + transaction.operation
                    ),
                    "credit_amount": eval(
                        str(request_body["amount"]) + transaction.operation
                    ),
                    "transaction_date": request_body["transaction_date"],
                    "details": transaction.details,
                    "owner_id": owner_id,
                    "tx_type": transaction.tx_type,
                    "invoice_id": invoice_id,
                }
            )
        )
    return resp
