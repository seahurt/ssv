from django.db import models
import psutil


# Create your models here.
def get_total_memory():
    return psutil.virtual_memory().total


class SystemConfig(models.Model):
    bridge_name = models.CharField(max_length=128, default='br0')
    bridge_network = models.CharField(max_length=128, default="192.168.100.1/24")
    dns = models.CharField(max_length=128, default='114.114.114.114,223.5.5.5')

    # location
    vm_location = models.CharField(max_length=256, default='/var/lib/ssv/vms')
    image_location = models.CharField(max_length=256, default='/var/lib/ssv/images')

    disk_size = models.IntegerField(default=100)  # unit GB
    disk_size_upper_limit = models.IntegerField(default=1024)  # up to 1T

    mem_size = models.IntegerField(default=8)
    vcpu_count = models.IntegerField(default=4)

    username = models.CharField(max_length=128, null=True, blank=True)
    ssh_key = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)  # store password hash here


class BaseImage(models.Model):
    """
    config:
    {
        "os": "CentOS7",
    }
    """
    name = models.CharField(max_length=128, unique=True)
    path = models.CharField(max_length=256)
    config = models.JSONField(default=dict, null=True, blank=True)


class IPPool(models.Model):
    network = models.IPAddressField()
    gateway = models.IPAddressField()
    netmask = models.IPAddressField()
    known_ips = models.JSONField()


class VM(models.Model):
    ST_PENDING = 'pending'
    ST_RUNNING = 'running'
    ST_SHUTDOWN = 'shutdown'

    st_choices = (
        (ST_PENDING, ST_PENDING),
        (ST_RUNNING, ST_RUNNING),
        (ST_SHUTDOWN, ST_SHUTDOWN),
    )
    name = models.CharField(max_length=128, unique=True)
    status = models.CharField(choices=st_choices, max_length=16)
    config = models.JSONField(default=dict, null=True, blank=True)


config = {
    "network": {

    },
    "users": {

    }
}
