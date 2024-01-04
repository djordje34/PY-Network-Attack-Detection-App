from django.db import models

# Create your models here.
class NetworkData(models.Model):
    IPV4_SRC_ADDR = models.GenericIPAddressField()
    L4_SRC_PORT = models.IntegerField()
    IPV4_DST_ADDR = models.GenericIPAddressField()
    L4_DST_PORT = models.IntegerField()
    PROTOCOL = models.IntegerField()
    L7_PROTO = models.FloatField()
    IN_BYTES = models.IntegerField()
    OUT_BYTES = models.IntegerField()
    IN_PKTS = models.IntegerField()
    OUT_PKTS = models.IntegerField()
    TCP_FLAGS = models.IntegerField()
    FLOW_DURATION_MILLISECONDS = models.IntegerField()