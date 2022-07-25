from django.contrib import admin
from django.urls import path
from services import views

urlpatterns = [

    # Services url    
    path('',views.services,name="Services"),

    # Vicisoft url
    path('vicisoft',views.vicisoft,name="Vicisoft"),
    path('doc_m',views.doc_m,name="Doc_m"),
    path('workflow',views.workflow,name="Workflow"),

    # Vicisoft url
    path('escan',views.escan,name="Escan"),
    path('enterprise_edition',views.enterprise_edition,name="EnterpriseEdition"),
    path('total_security',views.total_security,name="TotalSecurity"),

    # Sharp Education url
    path('sharp_education',views.sharp_education,name="SharpEducation"),
    path('classroom_management',views.classroom_management,name="ClassroomManagement"),
    path('touch_boards',views.touch_boards,name="TouchBoards"),
    path('sharp_signage',views.sharp_signage,name="SharpSignage"),
    path('learning_management',views.learning_management,name="LearningManagement"),
    path('interactive_content',views.interactive_content,name="InteractiveContent"),

    # NetCore Cloud url
    path('netcore_cloud',views.netcore_cloud,name="NetcoreCloud"),
    path('security',views.security,name="Security"),
    path('email_archive',views.email_archive,name="EmailArchive"),

    # D-link Networking url    
    path('networking',views.networking,name="Networking"),
    path('cable',views.cable,name="Cable"),
    path('router',views.router,name="Router"),
    path('switch',views.switch,name="Switch"),

    # End-Point Security url
    path('endpoint_security',views.endpoint_security,name="EndpointSecurity"),

]