import uuid
from cnx_service.model import BaseModel
from django.db import models

# Create your models here.
class Activities(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    created_by_name = models.CharField(max_length=255, null=True, blank=True)
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    modified_by_name = models.CharField(max_length=255, null=True, blank=True)
    c_call_outcome = models.TextField(null=True, blank=True)
    c_call_outcome_sub = models.TextField(null=True, blank=True)
    c_tab = models.TextField(null=True, blank=True)
    c_ghi_chu = models.TextField(null=True, blank=True)
    c_call_status = models.TextField(null=True, blank=True)
    c_final = models.TextField(null=True, blank=True)
    c_appointment_place = models.TextField(null=True, blank=True)
    c_type = models.TextField(null=True, blank=True)
    c_fk_dsg = models.CharField(max_length=255, null=True, blank=True)
    c_fk_cti = models.TextField(null=True, blank=True)
    c_fk_kh = models.CharField(max_length=255, null=True, blank=True)
    c_thoi_gian = models.TextField(null=True, blank=True)
    c_fk_order = models.TextField(null=True, blank=True)
    c_phone_call = models.TextField(null=True, blank=True)
    c_talking_call = models.TextField(null=True, blank=True)
    c_logcall_status = models.TextField(null=True, blank=True)
    c_langoithu = models.TextField(null=True, blank=True)
    c_ext_number = models.TextField(null=True, blank=True)
    c_pds = models.TextField(null=True, blank=True)
    c_ringing_call = models.TextField(null=True, blank=True)
    c_url_recording = models.TextField(null=True, blank=True)
    c_note = models.TextField(null=True, blank=True)
    c_br_type = models.TextField(null=True, blank=True)
    c_city = models.TextField(null=True, blank=True)
    c_subject = models.TextField(null=True, blank=True)
    c_channel = models.TextField(null=True, blank=True)
    c_ward = models.TextField(null=True, blank=True)
    c_dia_chi_moi = models.TextField(null=True, blank=True)
    c_br_status = models.TextField(null=True, blank=True)
    c_br_brand = models.TextField(null=True, blank=True)
    c_brand_switch_reason = models.TextField(null=True, blank=True)
    c_br_prev_brand = models.TextField(null=True, blank=True)
    c_registration_date = models.TextField(null=True, blank=True)
    c_drop_out_reason = models.TextField(null=True, blank=True)
    c_main_address_street_line1 = models.TextField(null=True, blank=True)
    c_main_address_street_line2 = models.TextField(null=True, blank=True)
    c_call_id = models.TextField(null=True, blank=True)
    c_nu_validation_result = models.TextField(null=True, blank=True)
    c_district = models.TextField(null=True, blank=True)
    c_secondary_product_discussed = models.TextField(null=True, blank=True)
    c_creation_of_channel_response = models.TextField(null=True, blank=True)
    c_br_curr_brand = models.TextField(null=True, blank=True)
    c_primary_product_discussed = models.TextField(null=True, blank=True)
    c_note_sotienhuathanhtoan = models.TextField(null=True, blank=True)
    c_note_ngayhuathanhtoan = models.TextField(null=True, blank=True)
    c_fk_cd = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
    


