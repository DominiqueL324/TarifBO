from djongo import models



class Tarifs(models.Model):
    id = models.ObjectIdField(db_column="_id", primary_key=True)
    user_id = models.CharField(max_length=40,null=True)
    meuble = models.CharField(max_length=10,null=True)
    date = models.DateTimeField(auto_now_add= True, auto_created=True,null=True)
    edl_prix_std = models.FloatField(default=0.0)
    edl_appt_prix_f2 =  models.FloatField(default=0.0)
    edl_appt_prix_f1 =  models.FloatField(default=0.0)
    edl_appt_prix_f3 = models.FloatField(default=0.0)
    edl_appt_prix_f4 = models.FloatField(default=0.0)
    edl_appt_prix_f5 = models.FloatField(default=0.0)
    edl_appt_prix_f6 =  models.FloatField(default=0.0)
    edl_pav_villa_prix_t1 =  models.FloatField(default=0.0)
    edl_pav_villa_prix_t2 = models.FloatField(default=0.0)
    edl_pav_villa_prix_t3 = models.FloatField(default=0.0)
    edl_pav_villa_prix_t4 = models.FloatField(default=0.0)
    edl_pav_villa_prix_t5 =  models.FloatField(default=0.0)
    edl_pav_villa_prix_t6 =  models.FloatField(default=0.0)
    edl_pav_villa_prix_t7 = models.FloatField(default=0.0)
    edl_pav_villa_prix_t8 = models.FloatField(default=0.0)
    chif_appt_prix_stu = models.FloatField(default=0.0)
    chif_appt_prix_f1 =  models.FloatField(default=0.0)
    chif_appt_prix_f2 =  models.FloatField(default=0.0)
    chif_appt_prix_f3 = models.FloatField(default=0.0)
    chif_appt_prix_f4 = models.FloatField(default=0.0)
    chif_appt_prix_f5 = models.FloatField(default=0.0)
    chif_appt_prix_f6 =  models.FloatField(default=0.0)
    chif_appt_prix_f7 =  models.FloatField(default=0.0)
    chif_appt_prix_f8 = models.FloatField(default=0.0)
    chif_pav_villa_prix_t1 = models.FloatField(default=0.0)
    chif_pav_villa_prix_t2 =  models.FloatField(default=0.0)
    chif_pav_villa_prix_t3 = models.FloatField(default=0.0)
    chif_pav_villa_prix_t4 = models.FloatField(default=0.0)
    chif_pav_villa_prix_t5 = models.FloatField(default=0.0)
    chif_pav_villa_prix_t6 =  models.FloatField(default=0.0)
    chif_pav_villa_prix_t7 =  models.FloatField(default=0.0)
    chif_pav_villa_prix_t8 = models.FloatField(default=0.0)
    code_tva = models.CharField(max_length=10,default="")
    com_cell_tech_ref_agent = models.CharField(max_length=20,default="")
    referent_as_client =  models.CharField(max_length=30,default="")
    com_as_sur_ca_client =  models.FloatField(default=0.0)
    com_cell_dev_ref_agent = models.FloatField(default=0.0)
    com_cell_dev_ref_responsable = models.FloatField(default=0.0)
    com_cell_tech_ref_responsable = models.FloatField(default=0.0)
    com_cell_planif_ref_responsable =  models.FloatField(default=0.0)
    com_cell_tech_ref_suiveur =  models.FloatField(default=0.0)
    com_cell_planif_ref_suiveur = models.FloatField(default=0.0)
    com_cell_planif_ref_gent_saisie = models.FloatField(default=0.0)
    cell_dev_ref_responsable = models.FloatField(default=0.0)
    cell_dev_ref_agent =  models.FloatField(default=0.0)
    cell_tech_ref_suiveur =  models.FloatField(default=0.0)
    cell_tech_ref_responsable = models.FloatField(default=0.0)
    cell_planif_ref_responsable = models.FloatField(default=0.0)
    cell_planif_ref_suiveur =  models.FloatField(default=0.0)
    cell_planif_ref_gent_saisie = models.FloatField(default=0.0)
    commentaire_libre = models.CharField(max_length=200,default="")
    chif_edl_pav_villa_prix_t2 = models.FloatField(default=0.0)
    chif_edl_pav_villa_prix_t3 =  models.FloatField(default=0.0)
    chif_edl_pav_villa_prix_t4 =  models.FloatField(default=0.0)
    chif_edl_pav_villa_prix_t5 = models.FloatField(default=0.0)
    chif_edl_pav_villa_prix_t6 = models.CharField(max_length=10,default="")
    chif_edl_pav_villa_prix_t7 = models.CharField(max_length=20,default="")
    chif_edl_pav_villa_prix_t8 =  models.CharField(max_length=30,default="")
    chif_appt_prix_f7 =  models.FloatField(default=0.0)
    chif_appt_prix_f8 = models.FloatField(default=0.0)
    com_as_sur_ca_client = models.FloatField(default=0.0)
    cell_tech_ref_agent = models.FloatField(default=0.0)
    com_as_sur_client =  models.FloatField(default=0.0)
    prix_autres =  models.FloatField(default=0.0)
    taux_meuble = models.FloatField(default=0.0)
    nature_bien = models.CharField(max_length=50,null=True)
    client_id = models.CharField(max_length=20, null=True)
