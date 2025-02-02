# SECURITY WARNING: DO NOT USE THIS IN PRODUCTION
SECRET_KEY = 'notsecret'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []


# Enable debug logging for rackit
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    },
    'loggers': {
        'rackit.connection': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'azimuth_auth',
    'azimuth',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'azimuth_auth.middleware.SessionTokenMiddleware',
    'azimuth.middleware.CleanupProviderMiddleware',
]

ROOT_URLCONF = 'azimuth_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'azimuth_site.wsgi.application'


# No databases
DATABASES = { }


# Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'


# Use cookie sessions so that we don't need a database
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


REST_FRAMEWORK = {
    'VIEW_DESCRIPTION_FUNCTION': 'azimuth.views.get_view_description',
    'DEFAULT_AUTHENTICATION_CLASSES': ['azimuth.authentication.TokenHeaderAuthentication'],
    'UNAUTHENTICATED_USER': None,
}


AZIMUTH_AUTH = {
    'AUTHENTICATOR': {
        # The authenticator factory to use
        'FACTORY': 'azimuth_auth.authenticator.openstack.PasswordAuthenticator',
        'PARAMS': {
            # OpenStack auth URL
            'AUTH_URL': '',
            # The OpenStack domain to use
            'DOMAIN': '',
            # Whether to verify SSL or not (default true)
            'VERIFY_SSL': False
        },
    },
}


AZIMUTH = {
    'AVAILABLE_CLOUDS': {
        'example': {
            'label': 'Example Cloud',
            'url': 'http://localhost:3000/dashboard',
        },
    },
    'CURRENT_CLOUD': 'example',

    # The cloud provider to use
    'PROVIDER': {
        # The provider factory to use (currently only OpenStack is supported)
        'FACTORY': 'azimuth.provider.openstack.Provider',
        'PARAMS': {
            # OpenStack auth URL
            'AUTH_URL': '',
            # The OpenStack domain to use
            # 'DOMAIN': 'default',
            # CIDR to use for auto-created internal networks
            # Defaults to 192.168.3.0/24
            # 'INTERNAL_NET_CIDR': '10.100.100.0/24',
            # Map of availability zone to backdoor network
            # Required to connect storage networks in JASMIN managed tenancies
            # Can be omitted
            # 'AZ_BACKDOOR_NET_MAP': {
            #     'nova': '',
            # },
            # The type of NIC to use for the backdoor network
            # Set to 'direct' for SR-IOV support, or omit
            # 'BACKDOOR_VNIC_TYPE': 'direct',
        },
    },

    # Settings for app proxy support (optional)
    # 'APPS': {
    #     # Indicates if apps are enabled
    #     'ENABLED': False,
    #     # The base domain for the app proxy
    #     'BASE_DOMAIN': 'apps.cloud.example.com',
    #     # The address of the app proxy SSHD service
    #     # Defaults to the base domain if not given
    #     # 'SSHD_HOST': 'proxy.cloud.example.com',
    #     # The port for the app proxy SSHD service
    #     # Defaults to 22 (standard SSH port) if not given
    #     # 'SSHD_PORT': 32222,
    # },

    # AWX settings for Cluster-as-a-Service support (optional)
    # 'AWX': {
    #     # Indicates whether AWX support should be enabled
    #     'ENABLED': True,
    #     # The AWX URL
    #     'URL': '',
    #     # Indicates whether to verify SSL when connecting over HTTPS
    #     'VERIFY_SSL': True,
    #     # The username to use for CaaS operations
    #     'USERNAME': 'caasctl',
    #     # The password to use for CaaS operations
    #     'PASSWORD': 'secretpassword',
    #     # Indicates whether teams should be created on demand
    #     # If set to false, then teams must be created manually in AWX, giving admins
    #     # control of which tenancies have CaaS enabled and which do not
    #     'CREATE_TEAMS': True,
    #     # Determines whether newly created teams should have the allow all permission granted
    #     # Only used if CREATE_TEAMS = True
    #     'CREATE_TEAM_ALLOW_ALL_PERMISSION': True,
    #     # Username and password for admin operations (e.g. creating resources),
    #     # if different from the username and password for CaaS operations
    #     'ADMIN_USERNAME': 'admin',
    #     'ADMIN_PASSWORD': 'secretadminpassword'
    #     # Any extra credentials to create and associate with the created projects below
    #     #
    #     # Each item should have the keys:
    #     #   * NAME - The name of the credential.
    #     #   * TYPE - The name of the credential type.
    #     #   * INPUTS - The inputs for the credential.
    #     'EXTRA_CREDENTIALS': [
    #         {
    #             'NAME': 'CaaS Consul',
    #             'TYPE': 'Hashicorp Consul',
    #             'INPUTS': {
    #                 'address': 'azimuth-consul-server:8500',
    #             },
    #         },
    #     ],
    #     # Definition of the default projects and job templates.
    #     #
    #     # Each item should have the required keys:
    #     #   * NAME - The name of the project.
    #     #   * GIT_URL - The git URL of the project.
    #     #   * GIT_VERSION - The branch, tag or commit id to use.
    #     #   * METADATA_ROOT - The base URL for cluster metadata files.
    #     # 
    #     # The following keys are optional:
    #     #   * ALWAYS_UPDATE - Boolean indicating if the project should be updated to the latest
    #     #                     commit for the branch every time a job is executed. Defaults to false.
    #     #   * PLAYBOOKS - List of playbooks to create job templates for.
    #     #                 If not given, a job template is created for each playbook
    #     #                 in the project.
    #     #   * EXTRA_VARS - A dictionary whose keys are the playbooks and whose values
    #     #                  are dictionaries of Ansible extra_vars for those playbooks.
    #     #                  The special key '__ALL__' can be used to set common extra_vars
    #     #                  for all playbooks in a project.
    #     #   * EXECUTION_ENVIRONMENT - A dictionary containing settings for a custom
    #     #                             execution environment, containing the keys:
    #     #     * IMAGE - The image for the execution environment (required).
    #     #     * ALWAYS_PULL - Boolean indicating if the image should be pulled every time it is
    #     #                     used or only when it is missing. Defaults to false.
    #     'DEFAULT_PROJECTS': [
    #         {
    #             'NAME': 'My Site Appliances',
    #             'GIT_URL': 'https://github.com/myorg/site-appliances.git',
    #             'GIT_VERSION': 'master',
    #             'METADATA_ROOT': 'https://raw.githubusercontent.com/myorg/site-appliances/master/ui-meta',
    #         },
    #     ]
    # },

    # The SSH key store to use
    # The portal asks this store for the SSH key for a user
    # By default, it will use a key store that calls out to the configured provider
    # to store and retrieve keys natively
    # However if you already have users' SSH keys in an external system, e.g. LDAP, you can implement
    # the key store interface to fetch them
    # 'SSH_KEY_STORE': {
    #     'FACTORY': 'azimuth.keystore.provider.ProviderKeyStore',
    # },
}
