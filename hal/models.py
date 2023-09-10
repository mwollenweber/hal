from django.db import models


class Mail(models.Model):
    tdstamp = models.DateTimeField(auto_now_add=True, blank=True)


class MailResult(models.Model):
    tdstamp = models.DateTimeField(auto_now_add=True, blank=True)
    # mailid =
    pluginid = models.IntegerField()
    alertid = models.IntegerField()
    severity = models.CharField()


class MailIOC(models.Model):
    tdstamp = models.DateTimeField(auto_now_add=True, blank=True)
    # mailid = models.ForeignKey()

