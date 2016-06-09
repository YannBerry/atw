#-*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from atw.map.models import TripStage


class LatestStageFeed(Feed):
    title = "WASC latest Stages"
    link = "/map/list-trips/"
    description = "Follow the latest WASC's adventures"

    def items(self):
        return TripStage.objects.order_by('-date_published')[:5]

    def item_title(self, item):
        return item.stage_name

    def item_description(self, item):
        return item.story

    # item_link is only needed if TripStage has no get_absolute_url method.
    def item_link(self, item):
        return reverse('trip_stage', args=[item.pk])
