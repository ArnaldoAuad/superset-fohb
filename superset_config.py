import os

# =============================================================================
# BÁSICO
# =============================================================================
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY')

# =============================================================================
# IDIOMA PT-BR
# =============================================================================
BABEL_DEFAULT_LOCALE = 'pt_BR'
LANGUAGES = {
    'pt_BR': {'flag': 'br', 'name': 'Português (Brasil)'},
    'en': {'flag': 'us', 'name': 'English'},
}

# =============================================================================
# BANCO DE DADOS
# =============================================================================
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

# =============================================================================
# REDIS
# =============================================================================
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))

CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 1,
}

DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_data_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 2,
}

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_filter_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 3,
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_explore_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 4,
}

# =============================================================================
# CELERY
# =============================================================================
class CeleryConfig:
    broker_url = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
    result_backend = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'

CELERY_CONFIG = CeleryConfig

# =============================================================================
# TODAS AS FEATURES HABILITADAS
# =============================================================================
FEATURE_FLAGS = {
    # Templates Jinja
    'ENABLE_TEMPLATE_PROCESSING': True,
    
    # Filtros
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'DASHBOARD_NATIVE_FILTERS_SET': True,
    
    # Alertas e Relatórios
    'ALERT_REPORTS': True,
    
    # Embedding
    'EMBEDDABLE_CHARTS': True,
    'EMBEDDED_SUPERSET': True,
    
    # SQL Lab
    'ENABLE_EXPLORE_DRAG_AND_DROP': True,
    'SQLLAB_BACKEND_PERSISTENCE': True,
    
    # Dashboards
    'DASHBOARD_VIRTUALIZATION': True,
    'DASHBOARD_RBAC': True,
    
    # Gráficos
    'DRILL_TO_DETAIL': True,
    'DRILL_BY': True,
    'HORIZONTAL_FILTER_BAR': True,
    
    # Upload
    'ALLOW_CSV_UPLOAD': True,
    'ALLOW_EXCEL_UPLOAD': True,
    
    # Extras
    'TAGGING_SYSTEM': True,
    'THUMBNAILS': True,
    'LISTVIEWS_DEFAULT_CARD_VIEW': True,
    'ENABLE_JAVASCRIPT_CONTROLS': True,
    'GLOBAL_ASYNC_QUERIES': True,
    'VERSIONED_EXPORT': True,
    'SSH_TUNNELING': True,
}

# =============================================================================
# UPLOADS
# =============================================================================
CSV_EXTENSIONS = {'csv', 'tsv', 'txt'}
EXCEL_EXTENSIONS = {'xls', 'xlsx'}
ALLOWED_EXTENSIONS = {*CSV_EXTENSIONS, *EXCEL_EXTENSIONS}
UPLOAD_FOLDER = '/app/superset_home/uploads/'

# =============================================================================
# SQL LAB
# =============================================================================
SQLLAB_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300
SQL_MAX_ROW = 100000
DISPLAY_MAX_ROW = 10000
SQLLAB_CTAS_NO_LIMIT = True

# =============================================================================
# THUMBNAILS
# =============================================================================
THUMBNAILS = True
THUMBNAIL_SELENIUM_USER = 'admin'
THUMBNAIL_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': 5,
}

# =============================================================================
# ALERTAS E RELATÓRIOS
# =============================================================================
ALERT_REPORTS_NOTIFICATION_DRY_RUN = False

# =============================================================================
# MAPAS (opcional - adicione sua key do Mapbox)
# =============================================================================
MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY', '')

# =============================================================================
# LOGS
# =============================================================================
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
LOG_LEVEL = 'INFO'
