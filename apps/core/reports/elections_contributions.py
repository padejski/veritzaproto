from django.db.models import Count, Sum

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from apps.core.models import ElectionsContributions

class ElectionsContributionsReport(Report):
    renderer = GoogleChartsRenderer

    location_chart = charts.PieChart(
        title="By elections location",
        width=500,
        height=300
    )

    contributor_type_chart = charts.PieChart(
        title="By contributor type",
        width=500,
        height=300
    )


    political_party_chart = charts.ColumnChart(
        title="Number of contributors by political party",
        width=500,
        height=300
    )

    political_party_amount_chart = charts.ColumnChart(
        title="Total amount contributed by political party",
        width=900,
        height=300
    )


    def get_data_for_location_chart(self):
        data = ChartData()

        data.add_column("Elections Location")
        data.add_column("Contributions count")

        for row in ElectionsContributions.objects.values_list('election_place').annotate(count=Count('id')).order_by('-count')[:10]:
            data.add_row(row)

        return data

    def get_data_for_contributor_type_chart(self):
        data = ChartData()

        data.add_column("Contributor type")
        data.add_column("Contributions count")

        for row in ElectionsContributions.objects.values_list('contributor_type').annotate(count=Count('id')):
            data.add_row(row)

        return data

    def get_data_for_political_party_chart(self):
        data = ChartData()

        data.add_column("Political party")
        data.add_column("Contributions count")

        for row in ElectionsContributions.objects.values_list('political_party').annotate(count=Count('id')):
            data.add_row(row)

        return data

    def get_data_for_political_party_amount_chart(self):
        data = ChartData()

        data.add_column("Political party")
        data.add_column("Total amount")

        for row in ElectionsContributions.objects.values_list('political_party').annotate(count=Sum('amount')):
            data.add_row([row[0], int(row[1])])

        return data
