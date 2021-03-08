#
# 
# For more information, check the SDK documentation at the link below:
# https://nosql-python-sdk.readthedocs.io/en/latest/tables.html#add-data
#
#

#----------------------------------------------------------------------------
# This Git repository belongs to my (darmbrust@gmail.com) studies about 
# Oracle NoSQL. To known more, check the blog post (pt-br):
#
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-1
# https://blogs.oracle.com/lad-cloud-experts/pt/introducao-ao-oracle-nosql-database-cloud-parte-2
# ---------------------------------------------------------------------------

import json

from borneo.iam import SignatureProvider
from borneo import NoSQLHandleConfig, NoSQLHandle, Regions
from borneo import PutRequest

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

put_request = PutRequest()
put_request.set_table_name('produtos')

f = open('data/ecommerce.json')

for json_line in f.readlines():
    json_line = json.loads(json_line)
    put_request.set_value(json_line)    
    nosql_handle.put(put_request)

f.close()

# free up the resources from handle.
nosql_handle.close()