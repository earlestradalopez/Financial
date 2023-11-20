"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6-e5$@l92n9ma)fq4z83dq6+ynf=!fpbzfb7ps3%_bk33@ys7d"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [    
    "ec2-13-230-82-195.ap-northeast-1.compute.amazonaws.com",
    "data.dssedu.com",
    "financialreport.dssedu.com",
    "localhost"
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "finance",
    "bootstrap4",
    "ckeditor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "finance.middleware.VisitorMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")


AUTH_USER_MODEL = "finance.User"
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
LOGIN_URL = "/login/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "finance", "static"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "finance","json")

MEDIA_URL = "/media/"

CKEDITOR_CONFIGS = {
    "financial_config": {
        "toolbar": [
            ["Bold", "Italic", "Underline", "Strike", "Subscript", "Superscript"],
            ["NumberedList", "BulletedList", "Indent", "Outdent"],
            ["JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock"],
            ["Link", "Unlink"],
            ["Image", "Table", "HorizontalRule", "SpecialChar"],
            ["Undo", "Redo"],
            ["Source"],
        ],
        "width": "100%",
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
    },
}

SCHOOLS = {
    "advantage": "Advantage Academy",
    "cumberland": "Cumberland Academy",
    "village-tech": "Village Tech Schools",
    "leadership": "Leadership Prep School Frisco",
    "manara": "Manara Academy",
    "legacy": "Legacy Preparatory Charter Academy",
    "cityscape": "Cityscape Schools Inc",
    "ptaa": "Pioneer Technology and Arts Academy",
    "aca": "Arlington Classics Academy",
    "trivium": "Trivium Academy",
    "pro-vision": "Pro-Vision Academy",
    "sa": "San Antonio Preparatory Schools",
    "ume": "UME Preparatory Academy",
    "lonestar": "Imagine Lone Star International Academy",
    "stmary": "St Mary's Charter School",
    "goldenrule": "Golden Rule Schools",
}

db = {
    "advantage": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Advantage]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "cumberland": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Cumberland]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "village-tech": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[Skyward_VillageTech]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "leadership": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Leadership]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "manara": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Manara]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"        
    },
    "legacy": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[Skyward_Legacy1]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "cityscape": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[Skyward_CityScape]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "ptaa": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[Skyward_PTAA]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "aca": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_ACA]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"        
    },
    "trivium": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Trivium]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"        
    },
    "pro-vision": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_Provision]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"        
    },
    "sa": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_SA]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"        
    },
    "ume": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[Skyward_UME]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
    "lonestar": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_LoneStar]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
     "stmary": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_StMary]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
     "goldenrule": {
        "object": "[PL_Definition_obj]",
        "function": "[PL_Definition_func]",
        "db": "[AscenderData_GoldenRule]",
        "code": "[PL_ExpensesbyObjectCode]",
        "activities": "[PL_Activities]",
        "bs": "[AscenderData_Advantage_Balancesheet]",
        "bs_activity": "[ActivityBS]",
        "cashflow": "[AscenderData_Advantage_Cashflow]",
        "adjustment": "[Adjustment]",
        "bs_fye":"[BS_FYE]",
        "pl_chart":"[PLData]"
    },
}

schoolCategory = {
    "ascender": ["advantage", "manara", "leadership", "cumberland", "aca", "trivium", "pro-vision", "sa", "lonestar", "stmary", "goldenrule"],
    "skyward": ["village-tech", "legacy", "cityscape", "ptaa", "ume"]
}

schoolMonths ={
    "julySchool": ["manara","leadership", "sa", "lonestar"],
    "septemberSchool" : ["advantage","cumberland","village-tech","legacy", "cityscape", "ptaa", "aca", "trivium", "pro-vision", "ume", "stmary", "goldenrule"]
}
