#
# NoSQLHandle is a handle that can be used to access Oracle NoSQL tables.
# A handle has memory and network resources associated with it. Consequently, 
# the close() method must be invoked to free up the resources when the 
# application is done using the handle. Creating and closing a handle around 
# each operation, would incur large resource allocation overheads resulting 
# in poor application performance. A single handle object is sufficient 
# to access tables in a multi-threaded application.
# 
# For more information, check the SDK documentation at the link below:
# https://nosql-python-sdk.readthedocs.io/en/latest/api/borneo.NoSQLHandle.html
#
#

#----------------------------------------------------------------------------
# This Git repository belongs to my (darmbrust@gmail.com) studies about 
# Oracle NoSQL. To known more, check the blog post (pt-br):
#
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-1
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-2
# ---------------------------------------------------------------------------

from borneo.iam import SignatureProvider
from borneo import NoSQLHandleConfig, NoSQLHandle, Regions

# create and close AuthorizationProvider
at_provider = SignatureProvider(config_file='~/.oci/config')
at_provider.close()

# create handle config using a desired region as endpoint and set a 
# default compartment.
handle_config = NoSQLHandleConfig(Regions.SA_SAOPAULO_1)
handle_config.set_authorization_provider(at_provider)
handle_config.set_default_compartment('<your-compartment-id>')

# create the handle.
nosql_handle = NoSQLHandle(handle_config)

# free up the resources from handle.
nosql_handle.close()