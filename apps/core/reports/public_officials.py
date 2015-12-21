from django.db.models import Count

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from apps.core.models import PublicOfficial, PublicOfficialReport

class PublicOfficialsReport(Report):
    renderer = GoogleChartsRenderer

    official_type_chart = charts.PieChart(
        title="By official type",
        width=900,
        height=300
    )

    def get_data_for_official_type_chart(self):
        data = ChartData()

        data.add_column("Official type")
        data.add_column("Count")

        for row in PublicOfficialReport.objects.values_list('official_id', 'official_type').annotate(count=Count('id')):
        # for row in PublicOfficialReport.objects.values_list('official_type', 'official_id').annotate(count=Count('id')):
            data.add_row([row[1], row[2]])

        return data
