#
# Creates an instance from SignatureProvider class that is used to authenticate
# and authorize access to Oracle NoSQL service.
# 
# For more information, check the SDK documentation at the link below:
# https://nosql-python-sdk.readthedocs.io/en/latest/api/borneo.iam.SignatureProvider.html
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

# create AuthorizationProvider
at_provider = SignatureProvider(
    tenant_id='<your-tenancy-id>',
    user_id='<your-user-id>',
    private_key='<path-to-your-private-key-file>',
    fingerprint='<fingerprint-of-your-public-key>')

at_provider.close()