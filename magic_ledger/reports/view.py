from flask_restx import Namespace, Resource

from magic_ledger.reports import reports_service
from magic_ledger.reports.api_model import (
    purchase_journal_entry,
    sales_journal_entry,
)

ns = Namespace(
    "reports",
    path="/<project_id>/reports/",
    description="An api that allows the user to retrieve reports",
)


@ns.route("/<report_date>/purchase/")
class PurchaseReport(Resource):
    @ns.marshal_list_with(purchase_journal_entry, code=200)
    def get(self, project_id, report_date):
        return reports_service.generate_purchase_journal(project_id, report_date), 200


@ns.route("/<report_date>/sales/")
class PurchaseReport(Resource):
    @ns.marshal_list_with(sales_journal_entry, code=200)
    def get(self, project_id, report_date):
        return reports_service.generate_sales_journal(project_id, report_date), 200


@ns.route("/general-ledger/<balance_date>/<account>", endpoint="general-ledger")
class AvailableDates(Resource):
    def get(self, project_id, balance_date, account):
        return (
            reports_service.get_general_ledger_entry(
                owner_id=project_id, balance_date=balance_date, account=account
            ),
            200,
        )
