import os
import time
from google.cloud import pubsub_v1
from google.oauth2 import service_account

pubsub_topic = "projects/hadooptest-223316/topics/virtualStore"


def pushData(eventData):
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
    testdata = """{"event_name":"eMenu_order_item","data":{"category_id":23371,"created_at":{"_seconds":1594214749,"_nanoseconds":222000000},"customer_id":563391,"customization_view":null,"is_personalized":0,"item_id":351950,"item_name":"Cream of Mushroom Soup","item_price":5.15,"item_qty":1,"item_sequence":1,"item_sku_id":436650,"item_sku_name":"Regular","item_type":"I","menu_mode":"Web","merchant_key":"5eb90f3b10728","parent_item_id":null,"parent_item_price":null,"parent_item_qty":null,"parent_item_sku_id":null,"paxT":2,"pos_order_id":"226596810","selection_group_id":null,"session_id":"845108072020130739","special_request":"","sub_category_id":39721,"table_no":"6","tabs_order_id":"226596810","timestamp":"2020-07-08T13:25:49.093Z"}}"""
    testdata = str.encode(testdata)
    pushData(testdata)
