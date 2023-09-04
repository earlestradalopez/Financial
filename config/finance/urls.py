from django.urls import path
from . import views
from . import prep_views
from . import manara_views
from . import new_views


urlpatterns = [

    
   
    path('login/',views.loginView,name = 'login'),
    path('login_form/',views.login_form,name = 'login_form'),
    path('logout/', views.logoutView, name='logout'),
    # path('pl_advantage/',views.pl_advantage,name = 'pl_advantage'),
    # path('pl_advantagechart/', views.pl_advantagechart, name='pl_advantagechart'),
    # path('first_advantage/', views.first_advantage, name='first_advantage'),
    # path('first_advantagechart/', views.first_advantagechart, name='first_advantagechart'),
    # path('gl_advantage/', views.gl_advantage, name='gl_advantage'),
    # path('bs_advantage/', views.bs_advantage, name='bs_advantage'),
    # path('cashflow_advantage/', views.cashflow_advantage, name='cashflow_advantage'),
    
    # path('dashboard_advantage/', views.dashboard_advantage, name='dashboard_advantage'),

    
    path('insert_row/', views.insert_row, name='insert-row'),
    path('delete/<str:fund>/<str:obj>/', views.delete, name='delete'),
    path('insert_bs_advantage/', views.insert_bs_advantage, name='insert_bs_advantage'),
    path('delete_bs/<str:description>/<str:subcategory>/', views.delete_bs, name='delete_bs'),
    path('delete_bsa/<str:obj>/<str:Activity>/', views.delete_bsa, name='delete_bsa'),
    path('generate_excel/', views.generate_excel, name='generate_excel'),
    
  
    path('delete_func/<str:func>/', views.delete_func, name='delete_func'),
    path('viewgl/<str:fund>/<str:obj>/<str:yr>/', views.viewgl, name='viewgl'),
    path('viewglfunc/<str:func>/<str:yr>/', views.viewglfunc, name='viewglfunc'),
    path('viewgl_activitybs/<str:obj>/<str:yr>/', views.viewgl_activitybs, name='viewgl_activitybs'),
    path('viewglexpense/<str:obj>/<str:yr>/', views.viewglexpense, name='viewglexpense'),

    
    # path('bs_cumberland/', views.bs_cumberland, name='bs_cumberland'),
    # path('pl_cumberlandchart/', views.pl_cumberlandchart, name='pl_cumberlandchart'),
    # path('pl_cumberland/',views.pl_cumberland,name = 'pl_cumberland'),
    # path('gl_cumberland/', views.gl_cumberland, name='gl_cumberland'),
    # path('cashflow_cumberland/', views.cashflow_cumberland, name='cashflow_cumberland'),
    # path('first_cumberland/', views.first_cumberland, name='first_cumberland'),
    # path('dashboard_cumberland/', views.dashboard_cumberland, name='dashboard_cumberland'),

    

    path('viewgl_cumberland/<str:fund>/<str:obj>/<str:yr>/', views.viewgl_cumberland, name='viewgl_cumberland'),
    path('viewglfunc_cumberland/<str:func>/<str:yr>/', views.viewglfunc_cumberland, name='viewglfunc_cumberland'),
    path('viewgl_activitybs_cumberland/<str:obj>/<str:yr>/', views.viewgl_activitybs_cumberland, name='viewgl_activitybs_cumberland'),
    path('viewglexpense_cumberland/<str:obj>/<str:yr>/', views.viewglexpense_cumberland, name='viewglexpense_cumberland'),


    # path('pl_villagetech/',views.pl_villagetech,name = 'pl_villagetech'),
    # path('bs_villagetech/', views.bs_villagetech, name='bs_villagetech'),

    # path('pl_prep/',prep_views.pl_prep,name = 'pl_prep'),
    # path('bs_prep/',prep_views.bs_prep,name = 'bs_prep'),

    # path('pl_manara/',manara_views.pl_manara,name = 'pl_manara'),
    # path('bs_manara/',manara_views.bs_manara,name = 'bs_manara'),

    # refactored urls
    path('dashboard/<str:school>',new_views.dashboard),
    path('charter-first/<str:school>',new_views.charter_first),
    path('charter-first-charts/<str:school>',new_views.charter_first_charts),
    path('profit-loss/<str:school>',new_views.profit_loss),
    path('profit-loss-charts/<str:school>',new_views.profit_loss_charts),
    path('balance-sheet/<str:school>',new_views.balance_sheet),
    path('balance-sheet-charts/<str:school>',new_views.balance_sheet_charts),
    path('cashflow-statement/<str:school>',new_views.cashflow),
    path('cashflow-statement-charts/<str:school>',new_views.cashflow_charts),
    path('general-ledger/<str:school>',new_views.general_ledger)
]
