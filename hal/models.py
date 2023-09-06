from django.db import models


class MailResult(models.Model):
    tdstamp = models.DateTimeField(auto_now_add=True, blank=True)
    #mailid = models.ForeignKey()
    pluginid = models.IntegerField()
    alertid = models.IntegerField()
    severity = models.CharField()
