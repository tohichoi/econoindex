import pendulum
from django_tables2 import Table, SingleTableView, Column
from econoindex.models import ImportExport


class TimeStampColumn(Column):
    def render(self, value):
        return pendulum.from_timestamp(value, tz='Asia/Seoul').to_date_string()


class CurrencyColumn(Column):
    def render(self, value):
        return f'{value:,}'


class ImportExportListTable(Table):
    timestamp = TimeStampColumn()
    imp_count = CurrencyColumn()
    imp_amount = CurrencyColumn()
    exp_count = CurrencyColumn()
    exp_amount = CurrencyColumn()
    balance = CurrencyColumn()

    class Meta:
        model = ImportExport
        template_name = "django_tables2/bootstrap4.html"
        fields = ['timestamp', 'country', 'imp_count', 'imp_amount', 'exp_count', 'exp_amount', 'balance']


class ImportExportListView(SingleTableView):
    template_name = 'econoindex/importexport_list.html'
    model = ImportExport
    table_class = ImportExportListTable
