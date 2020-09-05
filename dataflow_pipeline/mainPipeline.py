import os, json, ast
import argparse
import apache_beam as beam
from beam_nuggets.io import relational_db
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from pipeline_config import (
    INPUT_SUBSCRIPTION,
    SERVICE_ACCOUNT_PATH,
    SOURCE_CONFIG_PROD,
    TABLE_CONFIG,
)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_PATH

parser = argparse.ArgumentParser()
path_args, pipeline_args = parser.parse_known_args()

##
# This is the main process which will
# unnest our data and map order_id and
# time stamp to every item ordered
# so that they can be considered as a
# single record
##
def mainProcess(element):
    import ast

    # converting bytes into string
    dataDic = json.loads(element.decode("utf-8"))
    # converting string representation of Dictionary to Dictionary Obj
    dataDic = ast.literal_eval(dataDic)
    unnestedData = []
    # mapping all the items ordered to timestamp and order_id
    for items in dataDic["ordered_item"]:
        items["order_id"] = dataDic["order_id"]
        items["timestamp"] = dataDic["timestamp"]
        unnestedData.append(items)
    return unnestedData


# This is the entry point to our pipeline
def run_main(path_arguments, pipeline_arguments):
    options = PipelineOptions(pipeline_arguments)
    options.view_as(StandardOptions).streaming = True
    p = beam.Pipeline(options=options)  # initializing Pipeline object

    main_pipeline = (
        p
        | "Read data from pub sub"
        >> beam.io.ReadFromPubSub(subscription=INPUT_SUBSCRIPTION)
        | "Stripping newline character" >> beam.Map(lambda data: data.rstrip().lstrip())
        | "Applying our main unnesting function" >> beam.FlatMap(mainProcess)
    )

    main_pipeline | "Printing for debugging" >> beam.Map(print)

    main_pipeline | "Writing final data to production db" >> relational_db.Write(
        source_config=SOURCE_CONFIG_PROD, table_config=TABLE_CONFIG
    )

    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run_main(path_args, pipeline_args)

