from beam_nuggets.io import relational_db

##
# Change the subscription details as per your GCP project
##
INPUT_SUBSCRIPTION = "projects/hadooptest-223316/subscriptions/vitualStoreSubscriber"

##
# Change the path to the dir where your service account private key file is kept
##
SERVICE_ACCOUNT_PATH = "/home/aakash/credentials/pubsubtest.json"


##
# Change the details as per your MYSQL config
##
SOURCE_CONFIG_PROD = relational_db.SourceConfiguration(
    drivername="mysql+pymysql",
    host="35.200.253.253",
    port=3306,
    username="root",
    password="aakash@123",
    database="virtual_store",
    create_if_missing=False,  # create the database if not there
)

##
# Change the details as per your table name
##
TABLE_CONFIG = relational_db.TableConfiguration(
    name="transaction_data",
    create_if_missing=True,  # automatically create the table if not there
    primary_key_columns=["id"],  # and use 'num' column as primary key
)
