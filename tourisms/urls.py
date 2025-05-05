from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from tourism1.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('allmap/', allmap, name="allmap"),
    path('clickablemap/', clickablemap, name="clickablemap"),
    path('andhrapradesh/', andhrapradesh, name="andhrapradesh"),
    path('andhrapradesh_7days/', andhrapradesh_7days, name="andhrapradesh_7days"),
    path('andhrapradesh_12days/', andhrapradesh_12days, name="andhrapradesh_12days"),

    path('andamannicobar/', andamannicobar, name="andamannicobar"),
    path('andamannicobar_7days/', andamannicobar_7days, name="andamannicobar_7days"),
    path('andamannicobar_12days/', andamannicobar_12days, name="andamannicobar_12days"),
    
    path('arunachalpradesh/', arunachalpradesh, name="arunachalpradesh"),
    path('arunachalpradesh_7days/', arunachalpradesh_7days, name="arunachalpradesh_7days"),
    path('arunachalpradesh_12days/', arunachalpradesh_12days, name="arunachalpradesh_12days"),
    
    path('assam/', assam, name="assam"),
    path('assam_7days/', assam_7days, name="assam_7days"),
    path('assam_12days/', assam_12days, name="assam_12days"),
    
    path('bihar/', bihar, name="bihar"),
    path('bihar_7days/', bihar_7days, name="bihar_7days"),
    path('bihar_12days/', bihar_12days, name="bihar_12days"),
    
    path('chattisgarh/', chattisgarh, name="chattisgarh"),
    path('chattisgarh_7days/', chattisgarh_7days, name="chattisgarh_7days"),
    path('chattisgarh_12days/', chattisgarh_12days, name="chattisgarh_12days"),
    
    path('chandigarh/', chandigarh, name="chandigarh"),
    path('chandigarh_4days/', chandigarh_4days, name="chandigarh_4days"),
    
    path('goa/', goa, name="goa"),
    path('goa_7days/', goa_7days, name="goa_7days"),
    path('goa_12days/', goa_12days, name="goa_12days"),
    
    path('gujarat/', gujarat, name="gujarat"),
    path('gujarat_7days/', gujarat_7days, name="gujarat_7days"),
    path('gujarat_12days/', gujarat_12days, name="gujarat_12days"),
    
    path('haryana/', haryana, name="haryana"),
    path('haryana_7days/', haryana_7days, name="haryana_7days"),
    path('haryana_12days/', haryana_12days, name="haryana_12days"),
    
    path('himachalpradesh/', himachalpradesh, name="himachalpradesh"),
    path('himachalpradesh_7days/', himachalpradesh_7days, name="himachalpradesh_7days"),
    path('himachalpradesh_12days/', himachalpradesh_12days, name="himachalpradesh_12days"),
    path('eq_weather2/', eq_weather2, name="eq_weather2"),
    path('itmapalt/', itmapalt, name="itmapalt"),
    
    path('jharkhand/', jharkhand, name="jharkhand"),
    path('jharkhand_7days/', jharkhand_7days, name="jharkhand_7days"),
    path('jharkhand_12days/', jharkhand_12days, name="jharkhand_12days"),
    
    path('Karnataka/', Karnataka, name="Karnataka"),
    path('karnataka_7days/', karnataka_7days, name="karnataka_7days"),
    path('karnataka_12days/', karnataka_12days, name="karnataka_12days"),
    
    path('kerala/', kerala, name="kerala"),
    path('kerala_7days/', kerala_7days, name="kerala_7days"),
    path('kerala_12days/', kerala_12days, name="kerala_12days"),
        
    path('laksh/', laksh, name="laksh"),
    path('laksh_7days/', laksh_7days, name="laksh_7days"),
    path('laksh_12days/', laksh_12days, name="laksh_12days"),

    path('ladakh/', ladakh, name="ladakh"),
    path('ladakh_7days/', ladakh_7days, name="ladakh_7days"),
    path('ladakh_12days/', ladakh_12days, name="ladakh_12days"),
    
    path('madhyapradesh/', madhyapradesh, name="madhyapradesh"),
    path('madhyapradesh_7days/', madhyapradesh_7days, name="madhyapradesh_7days"),
    path('madhyapradesh_12days/', madhyapradesh_12days, name="madhyapradesh_12days"),
    
    path('maharashtra/', maharashtra, name="maharashtra"),
    path('maharashtra_7days/', maharashtra_7days, name="maharashtra_7days"),
    path('maharashtra_12days/', maharashtra_12days, name="maharashtra_12days"),
    
    path('manipur/', manipur, name="manipur"),
    path('manipur_7days/', manipur_7days, name="manipur_7days"),
    path('manipur_12days/', manipur_12days, name="manipur_12days"),
    
    path('meghalaya/', meghalaya, name="meghalaya"),
    path('meghalaya_7days/', meghalaya_7days, name="meghalaya_7days"),
    path('meghalaya_12days/', meghalaya_12days, name="meghalaya_12days"),
    
    path('mizoram/', mizoram, name="mizoram"),
    path('mizoram_7days/', mizoram_7days, name="mizoram_7days"),
    path('mizoram_12days/', mizoram_12days, name="mizoram_12days"),
    
    path('nagaland/', nagaland, name="nagaland"),
    path('nagaland_7days/', nagaland_7days, name="nagaland_7days"),
    path('nagaland_12days/', nagaland_12days, name="nagaland_12days"),
    
    path('newdel/', newdel, name="newdel"),
    path('newdel_7days/', newdel_7days, name="newdel_7days"),
    path('newdel_12days/', newdel_12days, name="newdel_12days"),
    
    path('odisha/', odisha, name="odisha"),
    path('odisha_7days/', odisha_7days, name="odisha_7days"),
    path('odisha_12days/', odisha_12days, name="odisha_12days"),
    
    path('punjab/', punjab, name="punjab"),
    path('punjab_7days/', punjab_7days, name="punjab_7days"),
    path('punjab_12days/', punjab_12days, name="punjab_12days"),
    
    path('puducherry/', puducherry, name="puducherry"),
    path('puducherry_4days/', puducherry_4days, name="puducherry_4days"),
    
    path('rajasthan/', rajasthan, name="rajasthan"),
    path('rajasthan_7days/', rajasthan_7days, name="rajasthan_7days"),
    path('rajasthan_12days/', rajasthan_12days, name="rajasthan_12days"),
    
    path('sikkim/', sikkim, name="sikkim"),
    path('sikkim_7days/', sikkim_7days, name="sikkim_7days"),
    path('sikkim_12days/', sikkim_12days, name="sikkim_12days"),
    
    path('tamilnadu/', tamilnadu, name="tamilnadu"),
    path('tamilnadu_7days/', tamilnadu_7days, name="tamilnadu_7days"),
    path('tamilnadu_12days/', tamilnadu_12days, name="tamilnadu_12days"),
    
    path('telangana/', telangana, name="telangana"),
    path('telangana_7days/', telangana_7days, name="telangana_7days"),
    path('telangana_12days/', telangana_12days, name="telangana_12days"),
    
    path('tripura/', tripura, name="tripura"),
    path('tripura_7days/', tripura_7days, name="tripura_7days"),
    path('tripura_12days/', tripura_12days, name="tripura_12days"),
    
    path('uttarpradesh/', uttarpradesh, name="uttarpradesh"),
    path('uttarpradesh_7days/', uttarpradesh_7days, name="uttarpradesh_7days"),
    path('uttarpradesh_12days/', uttarpradesh_12days, name="uttarpradesh_12days"),
    
    path('uttarakhand/', uttarakhand, name="uttarakhand"),
    path('uttarakhand_7days/', uttarakhand_7days, name="uttarakhand_7days"),
    path('uttarakhand_12days/', uttarakhand_12days, name="uttarakhand_12days"),
    
    path('westbengal/', westbengal, name="westbengal"),
    path('westbengal_7days/', wb_7days, name="wb_7days"),
    path('westbengal_12days/', wb_12days, name="wb_12days"),
    
    path('jammuandkashmir/', jammuandkashmir, name="jammuandkashmir"),
    path('jammuandkashmir_7days/', jammuandkashmir_7days, name="jammuandkashmir_7days"),
    path('jammuandkashmir_12days/', jammuandkashmir_12days, name="jammuandkashmir_12days"),
]
