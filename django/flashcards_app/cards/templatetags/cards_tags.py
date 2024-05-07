from cards.models import STAGES, Card
from django import template

register = template.Library()


@register.inclusion_tag("cards/box_links.html")
def stages_as_links():
    stages = []
    for stage_num in STAGES:
        card_count = Card.objects.filter(box=stage_num).count()
        stages.append({"number": stage_num, "card_count": card_count})

    return {"stages": stages}
