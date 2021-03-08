#
# 
# For more information, check the SDK documentation at the link below:
# https://nosql-python-sdk.readthedocs.io/en/latest/tables.html
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
from borneo import TableRequest

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

table_ddl = """
  
  ALTER TABLE produtos (ADD data_criacao TIMESTAMP(0))

"""

# creates a request object that contains the DLL instruction.
table_request = TableRequest()
table_request.set_statement(table_ddl)

# execute the DDL instruction.
nosql_handle.table_request(table_request)

# free up the resources from handle.
nosql_handle.close()