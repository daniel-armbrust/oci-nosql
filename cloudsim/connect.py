#
# 
# For more information, check the SDK documentation at the link below:
# https://nosql-python-sdk.readthedocs.io/en/latest/installation.html#configure-for-the-cloud-simulator
#
#

#----------------------------------------------------------------------------
# This Git repository belongs to my (darmbrust@gmail.com) studies about 
# Oracle NoSQL. To known more, check the blog post (pt-br):
#
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-1
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-2
# ---------------------------------------------------------------------------

from borneo import NoSQLHandle, NoSQLHandleConfig
from borneo.kv import StoreAccessTokenProvider

# NoSQL Cloud Simulator endpoint
simulator_endpoint = 'http://localhost:5000'

# create the AuthorizationProvider for a not secure store:
ap = StoreAccessTokenProvider()

# create handle config 
handle_config = NoSQLHandleConfig(simulator_endpoint)
handle_config.set_authorization_provider(ap)

# create the handle.
nosql_handle = NoSQLHandle(handle_config)
nosql_handle.close()
