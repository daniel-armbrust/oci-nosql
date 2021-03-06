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
from borneo import TableLimits, TableRequest

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
  
  CREATE TABLE produtos (
      id INTEGER GENERATED BY DEFAULT ON NULL AS IDENTITY (START WITH 1 INCREMENT BY 1),
      propriedades JSON,
      valor NUMBER,
      frete_gratis BOOLEAN,
      imagens ARRAY(STRING),
    PRIMARY KEY(id)) 

"""

# 10 Read Units (RU)
#  5 Write Units (WU)
#  1 GB of Storage 
table_limits = TableLimits(10, 5, 1)

# creates a request object that contains the DLL instruction and 
# throughput/capacity limits.
table_request = TableRequest()
table_request.set_statement(table_ddl)
table_request.set_table_limits(table_limits)

# perform the creation of the new nosql table.
nosql_handle.table_request(table_request)

# free up the resources from handle.
nosql_handle.close()