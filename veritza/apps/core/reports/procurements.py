from django.db.models import Count, Sum

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from veritza.apps.core.models import PublicProcurement

class ProcurementsReport(Report):
    renderer = GoogleChartsRenderer

    location_chart = charts.ColumnChart(
        title="By location",
        width=900,
        height=300
    )

    subject_chart = charts.PieChart(
        title="By subject",
        width=500,
        height=300
    )

    procurements_total_chart = charts.ColumnChart(
        title="Top 5 cities by total value of procurements",
        width=500,
        height=300
    )

    notice_type_chart = charts.PieChart(
        title="By notice type",
        width=500,
        height=300
    )

    def get_data_for_location_chart(self):
        data = ChartData()

        data.add_column("Location")
        data.add_column("Procurement count")

        for row in PublicProcurement.objects.values_list('location').annotate(count=Count('id')).order_by('-count')[:10]:
            data.add_row(row)

        return data

    def get_data_for_subject_chart(self):
        data = ChartData()

        data.add_column("Subject")
        data.add_column("Procurement count")

        for row in PublicProcurement.objects.values_list('subject').annotate(count=Count('id')):
            data.add_row(row)

        return data

    def get_data_for_notice_type_chart(self):
        data = ChartData()

        data.add_column("Notice type")
        data.add_column("Procurement count")

        for row in PublicProcurement.objects.values_list('record_type').annotate(count=Count('id')):
            data.add_row(row)

        return data

    def get_data_for_procurements_total_chart(self):
        data = ChartData()

        data.add_column("Municipality")
        data.add_column("Total amount")

        for row in PublicProcurement.objects.values_list('location').annotate(amount=Sum('value')).order_by('-amount')[:5]:
            data.add_row([row[0], int(row[1])])

        return data
