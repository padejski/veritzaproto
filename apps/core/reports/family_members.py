from django.db.models import Count

from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts

from veritza.apps.core.models import FamilyMember

class FamilyMembersReport(Report):
    renderer = GoogleChartsRenderer

    relationship_chart = charts.PieChart(
        title="By relationship type",
        width=900,
        height=300
    )

    def get_data_for_relationship_chart(self):
        data = ChartData()

        data.add_column("Relationship")
        data.add_column("Count")

        for row in FamilyMember.objects.values_list('relationship').annotate(count=Count('id')):
            data.add_row([FamilyMember.FAMILY_RELATION_CHOICES[row[0]], row[1]])

        return data
