from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard


class VeritzaDashboard(Dashboard):
    def __init__(self, **kwargs):

        Dashboard.__init__(self, **kwargs)

        self.children.append(
            modules.AppList(
                title=_("Applications"),
                column=1,
                models=(
                    'veritza.apps.core.*',
                )
            )
        )

        self.children.append(
            modules.AppList(
                title=_("Administration"),
                column=2,
                models=(
                    'veritza.apps.core.*',
                )
            )
        )

        self.children.append(
            modules.AppList(
                title=_("Others"),
                column=3,
                models=(
                    'veritza.apps.core.*',
                )
            )
        )