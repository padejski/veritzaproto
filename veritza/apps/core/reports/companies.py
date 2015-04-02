from django.db.models import Count

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from veritza.apps.core.models import Company

class CompaniesReport(Report):
    renderer = GoogleChartsRenderer

    company_type_chart = charts.PieChart(
        title="By company type",
        width=900,
        height=300
    )

    def get_data_for_company_type_chart(self):
        data = ChartData()

        data.add_column("Company type")
        data.add_column("Count")

        for row in Company.objects.values_list('economic_activity').annotate(count=Count('id')):
            data.add_row(row)

        return data
