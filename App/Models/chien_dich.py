import uuid
from django.db import models
from cnx_service.model import BaseModel


class ChienDich(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdBy = models.CharField(max_length=255, null=True, blank=True)
    createdByName = models.CharField(max_length=255, null=True, blank=True)
    modifiedBy = models.CharField(max_length=255, null=True, blank=True)
    modifiedByName = models.CharField(max_length=255, null=True, blank=True)
    c_ketQuaGoi = models.TextField(null=True, blank=True)
    c_nguon = models.TextField(null=True, blank=True)
    c_tyLeGoi = models.TextField(null=True, blank=True)
    c_nhom = models.TextField(null=True, blank=True)
    c_maxRingtime = models.TextField(null=True, blank=True)
    c_soLanGoiToiDa = models.TextField(null=True, blank=True)
    c_tieuDe = models.TextField(null=True, blank=True)
    c_ngayKetThuc = models.TextField(null=True, blank=True)
    c_kqMacDinh = models.TextField(null=True, blank=True)
    c_khoangThoiGianGoiLai = models.TextField(null=True, blank=True)
    c_ngayBatDau = models.TextField(null=True, blank=True)
    c_phanLoai = models.TextField(null=True, blank=True)
    c_trangThai = models.TextField(null=True, blank=True)
    c_timeStopUncall = models.TextField(null=True, blank=True)
    c_thoiGianGiua2LanGoi = models.TextField(null=True, blank=True)
    c_loaicd = models.TextField(null=True, blank=True)
    c_queueNumber = models.TextField(null=True, blank=True)
    c_maxChannel = models.TextField(null=True, blank=True)
    c_kqTimeout = models.TextField(null=True, blank=True)
    c_nhomKetQua = models.TextField(null=True, blank=True)
    c_kichBanGoi = models.TextField(null=True, blank=True)
    c_nu = models.TextField(null=True, blank=True)
    c_nfu_ignored_day = models.TextField(null=True, blank=True)
    c_max_no_connected = models.TextField(null=True, blank=True)
    c_nfu_code = models.TextField(null=True, blank=True)
    c_mobiChannel = models.TextField(null=True, blank=True)
    c_viettelChannel = models.TextField(null=True, blank=True)
    c_vinaChannel = models.TextField(null=True, blank=True)
    c_priority = models.TextField(null=True, blank=True)
    c_type_order = models.TextField(null=True, blank=True)
    c_poolnum = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Chien_dich"
        verbose_name_plural = "Chien_dich"