from django.db import models


class ImportExport(models.Model):
    timestamp = models.IntegerField('시간', blank=False, null=False)
    country = models.CharField('국가', max_length=255, blank=True, null=True, default=None)
    # usd
    imp_count = models.IntegerField('수입건수', blank=False, default=None)
    imp_amount = models.IntegerField('수입액', blank=False, default=None)
    # usd
    exp_count = models.IntegerField('수출건수', blank=False, default=None)
    exp_amount = models.IntegerField('수출액', blank=False, default=None)
    # usd
    balance = models.IntegerField('무역수지', blank=False, default=None)
    note = models.TextField('비고', max_length=8192, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        s = ''

    # def get_absolute_url(self):
    #     return reverse('bankaccount-detail', kwargs={'pk': self.partner.pk, 'ba_pk': self.pk})
