from scrapy.dupefilter import RFPDupeFilter

from apps.core.models import Company


class DBDupeFilter(RFPDupeFilter):

    def __init__(self, path=None, *args, **kwargs):
        self.urls_seen = set(Company.objects.all().values_list('link', flat=True))
        super(DBDupeFilter, self).__init__(path, *args, **kwargs)

    def request_seen(self, request):
        if request.url in self.urls_seen:
            return True
        else:
            self.urls_seen.add(request.url)
