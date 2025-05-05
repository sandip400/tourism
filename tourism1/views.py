from django.shortcuts import render
import requests

# Load environment variables

def home(request):
    
    return render(request, "home.html")

def allmap(request):
    return render(request, 'allmap.html')

def clickablemap(request):
    return render(request, 'clickablemap.html')

def westbengal(request):
    return render(request, 'westbengal.html')

def wb_7days(request):
    return render(request, 'wb_7days.html')

def wb_12days(request):
    return render(request, 'wb_12days.html')

def andhrapradesh(request):
    return render(request, 'andhrapradesh.html')

def andhrapradesh_7days(request):
    return render(request, 'andhrapradesh_7days.html')

def andhrapradesh_12days(request):
    return render(request, 'andhrapradesh_12days.html')

def arunachalpradesh(request):
    return render(request, 'arunachalpradesh.html')

def arunachalpradesh_7days(request):
    return render(request, 'arunachalpradesh_7days.html')

def arunachalpradesh_12days(request):
    return render(request, 'arunachalpradesh_12days.html')

def assam(request):
    return render(request, 'assam.html')

def assam_7days(request):
    return render(request, 'assam_7days.html')

def assam_12days(request):
    return render(request, 'assam_12days.html')

def bihar(request):
    return render(request, 'bihar.html')

def bihar_7days(request):
    return render(request, 'bihar_7days.html')

def bihar_12days(request):
    return render(request, 'bihar_12days.html')

def chattisgarh(request):
    return render(request, 'chattisgarh.html')

def chattisgarh_7days(request):
    return render(request, 'chattisgarh_7days.html')

def chattisgarh_12days(request):
    return render(request, 'chattisgarh_12days.html')

def goa(request):
    return render(request, 'goa.html')

def goa_7days(request):
    return render(request, 'goa_7days.html')

def goa_12days(request):
    return render(request, 'goa_12days.html')

def gujarat(request):
    return render(request, 'gujarat.html')

def gujarat_7days(request):
    return render(request, 'gujarat_7days.html')

def gujarat_12days(request):
    return render(request, 'gujarat_12days.html')

def haryana(request):
    return render(request, 'haryana.html')

def haryana_7days(request):
    return render(request, 'haryana_7days.html')

def haryana_12days(request):
    return render(request, 'haryana_12days.html')

def himachalpradesh(request):
    return render(request, 'himachalpradesh.html')

def himachalpradesh_7days(request):
    return render(request, 'himachalpradesh_7days.html')

def himachalpradesh_12days(request):
    return render(request, 'himachalpradesh_12days.html')


def eq_weather2(request):
    return render(request, 'eq_weather2.html')

def itmapalt(request):
    return render(request, 'itmapalt.html')

def jharkhand(request):
    return render(request, 'jharkhand.html')

def jharkhand_7days(request):
    return render(request, 'jharkhand_7days.html')

def jharkhand_12days(request):
    return render(request, 'jharkhand_12days.html')

def jammuandkashmir(request):
    return render(request, 'jammuandkashmir.html')

def kashmir_7days(request):
    return render(request, 'kashmir_7days.html')

def kashmir_12days(request):
    return render(request, 'kashmir_12days.html')

def Karnataka(request):
    return render(request, 'Karnataka.html')

def karnataka_7days(request):
    return render(request, 'karnataka_7days.html')

def karnataka_12days(request):
    return render(request, 'karnataka_12days.html')

def kerala(request):
    return render(request, 'kerala.html')

def kerala_7days(request):
    return render(request, 'kerala_7days.html')

def kerala_12days(request):
    return render(request, 'kerala_12days.html')

def madhyapradesh(request):
    return render(request, 'madhyapradesh.html')

def madhyapradesh_7days(request):
    return render(request, 'madhyapradesh_7days.html')

def madhyapradesh_12days(request):
    return render(request, 'madhyapradesh_12days.html')

def maharashtra(request):
    return render(request, 'maharashtra.html')

def maharashtra_7days(request):
    return render(request, 'maharashtra_7days.html')

def maharashtra_12days(request):
    return render(request, 'maharashtra_12days.html')

def manipur(request):
    return render(request, 'manipur.html')

def manipur_7days(request):
    return render(request, 'manipur_7days.html')

def manipur_12days(request):
    return render(request, 'manipur_12days.html')

def meghalaya(request):
    return render(request, 'meghalaya.html')

def meghalaya_7days(request):
    return render(request, 'meghalaya_7days.html')

def meghalaya_12days(request):
    return render(request, 'meghalaya_12days.html')

def mizoram(request):
    return render(request, 'mizoram.html')

def mizoram_7days(request):
    return render(request, 'mizoram_7days.html')

def mizoram_12days(request):
    return render(request, 'mizoram_12days.html')

def nagaland(request):
    return render(request, 'nagaland.html')

def nagaland_7days(request):
    return render(request, 'nagaland_7days.html')

def nagaland_12days(request):
    return render(request, 'nagaland_12days.html')

def odisha(request):
    return render(request, 'odisha.html')

def odisha_7days(request):
    return render(request, 'odisha_7days.html')

def odisha_12days(request):
    return render(request, 'odisha_12days.html')

def punjab(request):
    return render(request, 'punjab.html')

def punjab_7days(request):
    return render(request, 'punjab_7days.html')

def punjab_12days(request):
    return render(request, 'punjab_12days.html')

def rajasthan(request):
    return render(request, 'rajasthan.html')

def rajasthan_7days(request):
    return render(request, 'rajasthan_7days.html')

def rajasthan_12days(request):
    return render(request, 'rajasthan_12days.html')

def sikkim(request):
    return render(request, 'sikkim.html')

def sikkim_7days(request):
    return render(request, 'sikkim_7days.html')

def sikkim_12days(request):
    return render(request, 'sikkim_12days.html')

def tamilnadu(request):
    return render(request, 'tamilnadu.html')

def tamilnadu_7days(request):
    return render(request, 'tamilnadu_7days.html')

def tamilnadu_12days(request):
    return render(request, 'tamilnadu_12days.html')

def telangana(request):
    return render(request, 'telangana.html')

def telangana_7days(request):
    return render(request, 'telangana_7days.html')

def telangana_12days(request):
    return render(request, 'telangana_12days.html')

def tripura(request):
    return render(request, 'tripura.html')

def tripura_7days(request):
    return render(request, 'tripura_7days.html')

def tripura_12days(request):
    return render(request, 'tripura_12days.html')

def uttarakhand(request):
    return render(request, 'uttarakhand.html')

def uttarakhand_7days(request):
    return render(request, 'uttarakhand_7days.html')

def uttarakhand_12days(request):
    return render(request, 'uttarakhand_12days.html')

def uttarpradesh(request):
    return render(request, 'uttarpradesh.html')

def uttarpradesh_7days(request):
    return render(request, 'uttarpradesh_7days.html')

def uttarpradesh_12days(request):
    return render(request, 'uttarpradesh_12days.html')

def laksh(request):
    return render(request, 'laksh.html')

def laksh_7days(request):
    return render(request, 'laksh_7days.html')

def laksh_12days(request):
    return render(request, 'laksh_12days.html')

def newdel(request):
    return render(request, 'newdel.html')

def newdel_7days(request):
    return render(request, 'newdel_7days.html')

def newdel_12days(request):
    return render(request, 'newdel_12days.html')

def puducherry(request):
    return render(request, 'puducherry.html')

def puducherry_4days(request):
    return render(request, 'puducherry_4days.html')


def chandigarh(request):
    return render(request, 'chandigarh.html')

def chandigarh_4days(request):
    return render(request, 'chandigarh_4days.html')

def andamannicobar(request):
    return render(request, 'andamannicobar.html')

def andamannicobar_7days(request):
    return render(request, 'andamannicobar_7days.html')

def andamannicobar_12days(request):
    return render(request, 'andamannicobar_12days.html')

def dadraandnagarhaveli(request):
    return render(request, 'dadraandnagarhaveli.html')

def dadraandnagarhaveli_7days(request):
    return render(request, 'dadraandnagarhaveli_7days.html')

def dadraandnagarhaveli_12days(request):
    return render(request, 'dadraandnagarhaveli_12days.html')

def damananddiu(request):
    return render(request, 'damananddiu.html')


def damananddiu_7days(request):
    return render(request, 'damananddiu_7days.html')


def damananddiu_12days(request):
    return render(request, 'damananddiu_12days.html')

def ladakh(request):
    return render(request, 'ladakh.html')


def ladakh_7days(request):
    return render(request, 'ladakh_7days.html')

def ladakh_12days(request):
    return render(request, 'ladakh_12days.html')

def jammuandkashmir(request):
    return render(request, 'jammuandkashmir.html')

def jammuandkashmir_7days(request):
    return render(request, 'jammuandkashmir_7days.html')

def jammuandkashmir_12days(request):
    return render(request, 'jammuandkashmir_12days.html')