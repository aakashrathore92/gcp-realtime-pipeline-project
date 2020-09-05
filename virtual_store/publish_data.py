import os, json, time
from google.cloud import pubsub_v1
from google.oauth2 import service_account

##
# Function called by our virtual store application
# to push data in pub/sub Topic
##
def pushData(eventData):
    # Replace with your projectid
    projectid = "hadooptest-223316"
    # Replace  with your pubsub topic
    pubsub_topic = "projects/hadooptest-223316/topics/virtualStore"
    # Replace with your service account path
    service_account_path = "/home/aakash/credentials/pubsubtest.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

    publisher = pubsub_v1.PublisherClient.from_service_account_file(
        service_account_path
    )

    publisher.publish(pubsub_topic, eventData)


if __name__ == "__main__":
    testdata = str(
        {
            "order_id": "84c538fa-ef6f-11ea-a9c3-3db3abcedca9",
            "timestamp": 1599307283.61477,
            "ordered_item": [
                {
                    "item_name": "Sample Product Trolly",
                    "item_id": "1001",
                    "category_name": "sample category 1",
                    "item_price": 189.99,
                    "item_qty": 1,
                },
                {
                    "item_name": "Sample Product Mystery Box",
                    "item_id": "1002",
                    "category_name": "sample category 2",
                    "item_price": 47.0,
                    "item_qty": 3,
                },
                {
                    "item_name": "Sample Product Gift Bag",
                    "item_id": "1003",
                    "category_name": "sample category 3",
                    "item_price": 23.19,
                    "item_qty": 5,
                },
                {
                    "item_name": "Sample Product Small Block",
                    "item_id": "1004",
                    "category_name": "sample category 4",
                    "item_price": 44.99,
                    "item_qty": 1,
                },
                {
                    "item_name": "Sample Product Cardboard Box",
                    "item_id": "1005",
                    "category_name": "sample category 5",
                    "item_price": 64.59,
                    "item_qty": 5,
                },
            ],
        }
    )
    testdata = json.dumps(testdata).encode("utf-8")
    pushData(testdata)
