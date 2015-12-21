from django.db.models import Count

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from apps.core.models import Company, BidderCompany

class CompaniesReport(Report):
    renderer = GoogleChartsRenderer

    company_type_chart = charts.PieChart(
        title="By company type",
        width=900,
        height=300
    )

    company_procurements_chart = charts.ColumnChart(
        title="Top 5 companies by number of procurements awarded",
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

    def get_data_for_company_procurements_chart(self):
        data = ChartData()

        data.add_column("Company")
        data.add_column("Procurement Count")

        bidders = BidderCompany.objects.select_related('company').values_list('company_id').annotate(count=Count('id')).order_by('-count')[:5]
        # d = dict(bidders)
        # companies = zip(Company.objects.filter(id__in=d.values())

        for row in bidders:
            data.add_row(row)

        return data
