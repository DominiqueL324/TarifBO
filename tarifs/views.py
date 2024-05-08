from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions, generics,mixins,status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from datetime import date, datetime,time,timedelta
import string, json,  requests
from .models import Tarifs
from .serializer import TarifSerializer
from bson import ObjectId
from django.core.paginator import Paginator
from djongo.models import Q


class TarifApi(APIView):

    def post(self,request):
        data = request.data
        com =  Tarifs()
        com.user_id = data["user_id"]
        com.meuble =data["meuble"]        
        com.edl_prix_std = data["edl_prix_std"]
        com.edl_appt_prix_f2 =  data["edl_appt_prix_f2"]
        com.edl_appt_prix_f1 =  data["edl_appt_prix_f1"]
        com.edl_appt_prix_f3 = data["edl_appt_prix_f3"]
        com.edl_appt_prix_f4 = data["edl_appt_prix_f4"]
        com.edl_appt_prix_f5 = data["edl_appt_prix_f5"]
        com.edl_appt_prix_f6 =  data["edl_appt_prix_f6"]
        com.edl_pav_villa_prix_t1 =  data["edl_pav_villa_prix_t1"]
        com.edl_pav_villa_prix_t2 = data["edl_pav_villa_prix_t2"]
        com.edl_pav_villa_prix_t3 = data["edl_pav_villa_prix_t3"]
        com.edl_pav_villa_prix_t4 = data["edl_pav_villa_prix_t4"]
        com.edl_pav_villa_prix_t5 =  data["edl_pav_villa_prix_t5"]
        com.edl_pav_villa_prix_t6 =  data["edl_pav_villa_prix_t6"]
        com.edl_pav_villa_prix_t7 = data["edl_pav_villa_prix_t7"]
        com.edl_pav_villa_prix_t8 = data["edl_pav_villa_prix_t8"]
        com.chif_appt_prix_stu = data["chif_appt_prix_stu"]
        com.chif_appt_prix_f1 =  data["chif_appt_prix_f1"]
        com.chif_appt_prix_f2 =  data["chif_appt_prix_f2"]
        com.chif_appt_prix_f3 = data["chif_appt_prix_f3"]
        com.chif_appt_prix_f4 = data["chif_appt_prix_f4"]
        com.chif_appt_prix_f5 = data["chif_appt_prix_f5"]
        com.chif_appt_prix_f6 =  data["chif_appt_prix_f6"]
        com.chif_appt_prix_f7 =  data["chif_appt_prix_f7"]
        com.chif_appt_prix_f8 = data["chif_appt_prix_f8"]
        com.chif_pav_villa_prix_t1 = data["chif_pav_villa_prix_t1"]
        com.chif_pav_villa_prix_t2 =  data["chif_pav_villa_prix_t2"]
        com.chif_pav_villa_prix_t3 = data["chif_pav_villa_prix_t3"]
        com.chif_pav_villa_prix_t4 = data["chif_pav_villa_prix_t4"]
        com.chif_pav_villa_prix_t5 = data["chif_pav_villa_prix_t5"]
        com.chif_pav_villa_prix_t6 =  data["chif_pav_villa_prix_t6"]
        com.chif_pav_villa_prix_t7 =  data["chif_pav_villa_prix_t7"]
        com.chif_pav_villa_prix_t8 = data["chif_pav_villa_prix_t8"]
        com.code_tva =data["code_tva"]
        com.com_cell_tech_ref_agent =data["com_cell_tech_ref_agent"]
        com.referent_as_client = data["referent_as_client"]
        com.com_as_sur_ca_client =  data["com_as_sur_ca_client"]
        com.com_cell_dev_ref_agent = data["com_cell_dev_ref_agent"]
        com.com_cell_dev_ref_responsable = data["com_cell_dev_ref_responsable"]
        com.com_cell_tech_ref_responsable = data["com_cell_tech_ref_responsable"]
        com.com_cell_planif_ref_responsable =  data["com_cell_planif_ref_responsable"]
        com.com_cell_tech_ref_suiveur =  data["com_cell_tech_ref_suiveur"]
        com.com_cell_planif_ref_suiveur = data["com_cell_planif_ref_suiveur"]
        com.com_cell_planif_ref_gent_saisie = data["com_cell_planif_ref_gent_saisie"]
        com.cell_dev_ref_responsable = data["cell_dev_ref_responsable"]
        com.cell_dev_ref_agent =  data["cell_dev_ref_agent"]
        com.cell_tech_ref_suiveur =  data["cell_tech_ref_suiveur"]
        com.cell_tech_ref_responsable = data["cell_tech_ref_responsable"]
        com.cell_planif_ref_responsable = data["cell_planif_ref_responsable"]
        com.cell_planif_ref_suiveur =  data["cell_planif_ref_suiveur"]
        com.cell_planif_ref_gent_saisie = data["cell_planif_ref_gent_saisie"]
        com.commentaire_libre =data["commentaire_libre"]
        com.chif_edl_pav_villa_prix_t2 = data["chif_edl_pav_villa_prix_t2"]
        com.chif_edl_pav_villa_prix_t3 =  data["chif_edl_pav_villa_prix_t3"]
        com.chif_edl_pav_villa_prix_t4 =  data["chif_edl_pav_villa_prix_t4"]
        com.chif_edl_pav_villa_prix_t5 = data["chif_edl_pav_villa_prix_t5"]
        com.chif_edl_pav_villa_prix_t6 =data["chif_edl_pav_villa_prix_t6"]
        com.chif_edl_pav_villa_prix_t7 =data["chif_edl_pav_villa_prix_t7"]
        com.chif_edl_pav_villa_prix_t8 = data["chif_edl_pav_villa_prix_t8"]
        com.chif_appt_prix_f7 =  data["chif_appt_prix_f7"]
        com.chif_appt_prix_f8 = data["chif_appt_prix_f8"]
        com.com_as_sur_ca_client = data["com_as_sur_ca_client"]
        com.cell_tech_ref_agent = data["cell_tech_ref_agent"]
        com.com_as_sur_client =  data["com_as_sur_client"]
        com.prix_autres =  data["prix_autres"]
        com.taux_meuble = data["taux_meuble"]
        com.nature_bien = data["nature_bien"]
        com.client_id = data["client_id"]
        com.ref_client = data["ref_client"]
        com.nature_bien_text = data["nature_bien_text"]
        com.save()
        all_comments = Tarifs.objects.all()[Tarifs.objects.all().__len__()-1]
        serializer = TarifSerializer(Tarifs.objects.filter(pk=all_comments.id),many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 

    def get(self,request):
        all_comments = Tarifs.objects.all()

        # Number of items per page
        page_number = request.GET.get('page') 
         
        # Cas sans pagination
        if page_number is None:
            serializer = TarifSerializer(all_comments,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK) 
        
        # Cas avec pagination
        paginator = Paginator(all_comments, per_page=10)  
        try:
            page_obj = paginator.page(page_number)
        except :
            # Handle invalid page number error
            return JsonResponse({'error': 'Invalid page number'}, status=400)
        pagination_metadata = {
            'current_page': page_obj.number,
            'num_pages': paginator.num_pages,
            'total_items': paginator.count,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
        }
        serializer = TarifSerializer(page_obj,many=True)
        res={}
        res['info_pagination'] = pagination_metadata
        res['results']= serializer.data
        return Response(res,status=status.HTTP_200_OK)

class TarifsEditeApi(APIView):

    def put(self,request,id):
        data = request.data
        com = Tarifs.objects.filter(pk= ObjectId(id))
        com = com.first()
        if com is not None:
            #com.user_id = data["user_id"]
            com.meuble =data["meuble"]        
            com.edl_prix_std = data["edl_prix_std"]
            com.edl_appt_prix_f2 =  data["edl_appt_prix_f2"]
            com.edl_appt_prix_f1 =  data["edl_appt_prix_f1"]
            com.edl_appt_prix_f3 = data["edl_appt_prix_f3"]
            com.edl_appt_prix_f4 = data["edl_appt_prix_f4"]
            com.edl_appt_prix_f5 = data["edl_appt_prix_f5"]
            com.edl_appt_prix_f6 =  data["edl_appt_prix_f6"]
            com.edl_pav_villa_prix_t1 =  data["edl_pav_villa_prix_t1"]
            com.edl_pav_villa_prix_t2 = data["edl_pav_villa_prix_t2"]
            com.edl_pav_villa_prix_t3 = data["edl_pav_villa_prix_t3"]
            com.edl_pav_villa_prix_t4 = data["edl_pav_villa_prix_t4"]
            com.edl_pav_villa_prix_t5 =  data["edl_pav_villa_prix_t5"]
            com.edl_pav_villa_prix_t6 =  data["edl_pav_villa_prix_t6"]
            com.edl_pav_villa_prix_t7 = data["edl_pav_villa_prix_t7"]
            com.edl_pav_villa_prix_t8 = data["edl_pav_villa_prix_t8"]
            com.chif_appt_prix_stu = data["chif_appt_prix_stu"]
            com.chif_appt_prix_f1 =  data["chif_appt_prix_f1"]
            com.chif_appt_prix_f2 =  data["chif_appt_prix_f2"]
            com.chif_appt_prix_f3 = data["chif_appt_prix_f3"]
            com.chif_appt_prix_f4 = data["chif_appt_prix_f4"]
            com.chif_appt_prix_f5 = data["chif_appt_prix_f5"]
            com.chif_appt_prix_f6 =  data["chif_appt_prix_f6"]
            com.chif_appt_prix_f7 =  data["chif_appt_prix_f7"]
            com.chif_appt_prix_f8 = data["chif_appt_prix_f8"]
            com.chif_pav_villa_prix_t1 = data["chif_pav_villa_prix_t1"]
            com.chif_pav_villa_prix_t2 =  data["chif_pav_villa_prix_t2"]
            com.chif_pav_villa_prix_t3 = data["chif_pav_villa_prix_t3"]
            com.chif_pav_villa_prix_t4 = data["chif_pav_villa_prix_t4"]
            com.chif_pav_villa_prix_t5 = data["chif_pav_villa_prix_t5"]
            com.chif_pav_villa_prix_t6 =  data["chif_pav_villa_prix_t6"]
            com.chif_pav_villa_prix_t7 =  data["chif_pav_villa_prix_t7"]
            com.chif_pav_villa_prix_t8 = data["chif_pav_villa_prix_t8"]
            com.code_tva =data["code_tva"]
            com.com_cell_tech_ref_agent =data["com_cell_tech_ref_agent"]
            com.referent_as_client = data["referent_as_client"]
            com.com_as_sur_ca_client =  data["com_as_sur_ca_client"]
            com.com_cell_dev_ref_agent = data["com_cell_dev_ref_agent"]
            com.com_cell_dev_ref_responsable = data["com_cell_dev_ref_responsable"]
            com.com_cell_tech_ref_responsable = data["com_cell_tech_ref_responsable"]
            com.com_cell_planif_ref_responsable =  data["com_cell_planif_ref_responsable"]
            com.com_cell_tech_ref_suiveur =  data["com_cell_tech_ref_suiveur"]
            com.com_cell_planif_ref_suiveur = data["com_cell_planif_ref_suiveur"]
            com.com_cell_planif_ref_gent_saisie = data["com_cell_planif_ref_gent_saisie"]
            com.cell_dev_ref_responsable = data["cell_dev_ref_responsable"]
            com.cell_dev_ref_agent =  data["cell_dev_ref_agent"]
            com.cell_tech_ref_suiveur =  data["cell_tech_ref_suiveur"]
            com.cell_tech_ref_responsable = data["cell_tech_ref_responsable"]
            com.cell_planif_ref_responsable = data["cell_planif_ref_responsable"]
            com.cell_planif_ref_suiveur =  data["cell_planif_ref_suiveur"]
            com.cell_planif_ref_gent_saisie = data["cell_planif_ref_gent_saisie"]
            com.commentaire_libre =data["commentaire_libre"]
            com.chif_edl_pav_villa_prix_t2 = data["chif_edl_pav_villa_prix_t2"]
            com.chif_edl_pav_villa_prix_t3 =  data["chif_edl_pav_villa_prix_t3"]
            com.chif_edl_pav_villa_prix_t4 =  data["chif_edl_pav_villa_prix_t4"]
            com.chif_edl_pav_villa_prix_t5 = data["chif_edl_pav_villa_prix_t5"]
            com.chif_edl_pav_villa_prix_t6 =data["chif_edl_pav_villa_prix_t6"]
            com.chif_edl_pav_villa_prix_t7 =data["chif_edl_pav_villa_prix_t7"]
            com.chif_edl_pav_villa_prix_t8 = data["chif_edl_pav_villa_prix_t8"]
            com.chif_appt_prix_f7 =  data["chif_appt_prix_f7"]
            com.chif_appt_prix_f8 = data["chif_appt_prix_f8"]
            com.com_as_sur_ca_client = data["com_as_sur_ca_client"]
            com.cell_tech_ref_agent = data["cell_tech_ref_agent"]
            com.com_as_sur_client =  data["com_as_sur_client"]
            com.prix_autres =  data["prix_autres"]
            com.taux_meuble = data["taux_meuble"]
            com.nature_bien = data["nature_bien"]
            com.client_id = data["client_id"]
            com.ref_client = data["ref_client"]
            com.nature_bien_text = data["nature_bien_text"]
            com.save()
            com = Tarifs.objects.filter(pk= ObjectId(id))
            serializer = TarifSerializer(com,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)

    def get(self,request,id):
        com = Tarifs.objects.filter(pk= ObjectId(id))
        com = com.first()
        if com is not None:
            com = Tarifs.objects.filter(pk= ObjectId(id))
            serializer = TarifSerializer(com,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"status":"none"}, status=status.HTTP_204_NO_CONTENT)
    
class TarifsFiltreApi(APIView):
    def get(self,request):
        contenu = request.GET.get('to_find')
        rubrique = request.GET.get('rubrique')
        query = Q()
        if contenu is not None:
            query &= Q(commentaire__icontains = str(contenu))

        if rubrique is not None:
            query &= Q(key = str(rubrique)) 

        all_comments = Tarifs.objects.filter(query)
        serializer = TarifSerializer(all_comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
            
