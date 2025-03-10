from django.db import models
from decimal import Decimal
# Create your models here.
from account.models import UserProfile
from django.utils.translation import ugettext_lazy as _
from agency.models import Agency
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class PaymentType(models.Model):
    alias = models.CharField(
        max_length = 250,
        help_text=_('Alias'),
        verbose_name=_('Alias')
        )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal(0.00),
        verbose_name=_('User'))   
    name = models.CharField(
        max_length=250,
        help_text=_('Name'),
        verbose_name=_('Name')
        )         
    
    def __str__(self):
        return self.name

class Payment(models.Model):
    type = models.ForeignKey(PaymentType, on_delete=models.SET_NULL, null=True)
    payer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="payer")
    reciver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reciver")
    agency = models.ForeignKey(Agency, null=True, on_delete=models.CASCADE, related_name="agency")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    ammount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal(0.00),
        verbose_name=_('User'))

    type = models.CharField(
        max_length=50,
        help_text=_('Type'),
        verbose_name=_('Type')
        )
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=True)

    @staticmethod
    def get_chat_text_payment_or_create(room):
        tp = PaymentType.objects.get(alias='text-chat')
        payer = room.get_payer()
        reciver = room.get_woman()
        try:
            p = Payment.objects.get(payer=payer, reciver=reciver,object_id=room.id, is_closed=False)
            p.ammount += tp.price
        except Exception as e:
            print(e)
            p = Payment()
            p.payer = payer
            p.reciver = reciver
            p.ammount = tp.price
            p.is_closed = False
            p.content_object = room
            p.agency = reciver.get_agency()
        p.save()
        return p

    class Meta:
        verbose_name = _('User payment')
        verbose_name_plural = _('User payments')