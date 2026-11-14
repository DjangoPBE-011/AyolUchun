from django.db import models
from django.utils.translation import gettext_lazy as _


class DeletedReason(models.TextChoices):
    I_THOUGHT_ABOUT_IT = "I thought about it", _("I thought about it")
    THE_INFORMATION_WAS_ENTERED_INCORRECTLY = "The information was entered incorrectly", _("The information was entered incorrectly")
    THEY_FORCED_ME = "They forced me", _("They forced me")
    