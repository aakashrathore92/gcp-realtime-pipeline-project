import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import base64
import time
import uuid

app = dash.Dash(__name__)

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

productIventory = [
    {
        "item_name": "Sample Product Trolly",
        "item_id": "1001",
        "category_name": "sample category 1",
        "item_price": 189.99,
    },
    {
        "item_name": "Sample Product Mystery Box",
        "item_id": "1002",
        "category_name": "sample category 2",
        "item_price": 47.00,
    },
    {
        "item_name": "Sample Product Gift Bag",
        "item_id": "1003",
        "category_name": "sample category 3",
        "item_price": 23.19,
    },
    {
        "item_name": "Sample Product Small Block",
        "item_id": "1004",
        "category_name": "sample category 4",
        "item_price": 44.99,
    },
    {
        "item_name": "Sample Product Cardboard Box",
        "item_id": "1005",
        "category_name": "sample category 5",
        "item_price": 64.59,
    },
]

initialLayout = [
    html.Div([html.H3("Aakash Virtual Store", style={"textAlign": "center"})]),
    html.Div(
        [
            html.Div(
                [
                    # html.H3("Column 1"),
                    html.Img(
                        src="assets/product_5.png",
                        style={
                            "height": "25%",
                            "width": "25%",
                            "margin": ".5px 150px",
                        },
                    )
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 2"),
                    html.Br(),
                    dcc.Markdown(
                        """\n **Sample Product Trolly**  
                            Description:  
                            ⭐⭐⭐⭐  
                            **$189.99**"""
                    ),
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 3"),
                    html.Br(),
                    dcc.Markdown("""**Quantity**"""),
                    dcc.Input(id="prod1", type="number", debounce=False, min=0,),
                ],
                className="four columns",
            ),
        ],
        className="row",
    ),
    html.Div(
        [
            html.Div(
                [
                    # html.H3("Column 1"),
                    html.Img(
                        src="assets/product_4.png",
                        style={
                            "height": "25%",
                            "width": "25%",
                            "margin": ".5px 150px",
                        },
                    )
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 2"),
                    html.Br(),
                    dcc.Markdown(
                        """\n **Sample Product Mystery Box**  
                            Description:  
                            ⭐⭐⭐⭐  
                            **$47.00**"""
                    ),
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 3"),
                    html.Br(),
                    dcc.Markdown("""**Quantity**"""),
                    dcc.Input(id="prod2", type="number", debounce=False, min=0),
                ],
                className="four columns",
            ),
        ],
        className="row",
    ),
    html.Div(
        [
            html.Div(
                [
                    # html.H3("Column 1"),
                    html.Img(
                        src="assets/product_3.png",
                        style={
                            "height": "25%",
                            "width": "25%",
                            "margin": ".5px 150px",
                        },
                    )
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 2"),
                    html.Br(),
                    dcc.Markdown(
                        """\n **Sample Product Gift Bag**  
                            Description:  
                            ⭐⭐⭐⭐  
                            **$23.19**"""
                    ),
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 3"),
                    html.Br(),
                    dcc.Markdown("""**Quantity**"""),
                    dcc.Input(id="prod3", type="number", debounce=False, min=0),
                ],
                className="four columns",
            ),
        ],
        className="row",
    ),
    html.Div(
        [
            html.Div(
                [
                    # html.H3("Column 1"),
                    html.Img(
                        src="assets/product_2.png",
                        style={
                            "height": "25%",
                            "width": "25%",
                            "margin": ".5px 150px",
                        },
                    )
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 2"),
                    html.Br(),
                    dcc.Markdown(
                        """\n **Sample Product Small Block**  
                            Description:  
                            ⭐⭐⭐⭐  
                            **$44.99**"""
                    ),
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 3"),
                    html.Br(),
                    dcc.Markdown("""**Quantity**"""),
                    dcc.Input(id="prod4", type="number", debounce=False, min=0),
                ],
                className="four columns",
            ),
        ],
        className="row",
    ),
    html.Div(
        [
            html.Div(
                [
                    # html.H3("Column 1"),
                    html.Img(
                        src="assets/product_1.png",
                        style={
                            "height": "25%",
                            "width": "25%",
                            "margin": ".5px 150px",
                        },
                    )
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 2"),
                    html.Br(),
                    dcc.Markdown(
                        """\n **Sample Product Cardboard Box**  
                            Description:  
                            ⭐⭐⭐⭐  
                            **$64.59**"""
                    ),
                ],
                className="four columns",
            ),
            html.Div(
                [
                    # html.H3("Column 3"),
                    html.Br(),
                    dcc.Markdown("""**Quantity**"""),
                    dcc.Input(id="prod5", type="number", debounce=False, min=0,),
                ],
                className="four columns",
            ),
        ],
        className="row",
    ),
    html.Div(
        [
            html.Button(
                "Submit", id="submit-val", n_clicks=0, style={"margin": "10px 700px"},
            ),
        ]
    ),
    html.Div([html.Br()]),
    html.Div(id="output"),
]

app.layout = html.Div(id="main-page", children=initialLayout)


# @app.callback(Output("submit-val", "n_clicks"), [Input("submit-val", "n_clicks")])
# def update(reset):
#    return 0


@app.callback(
    [Output("output", "children"), Output("main-page", "children")],
    [Input("submit-val", "n_clicks")],
    [
        State("prod1", "value"),
        State("prod2", "value"),
        State("prod3", "value"),
        State("prod4", "value"),
        State("prod5", "value"),
    ],
)
def update(input_clicks, prod_1_qty, prod_2_qty, prod_3_qty, prod_4_qty, prod_5_qty):
    order = {"order_id": str(uuid.uuid1()), "timestamp": time.time()}
    ordered_item = []

    if input_clicks > 0:
        for i, product_qty in enumerate(
            [prod_1_qty, prod_2_qty, prod_3_qty, prod_4_qty, prod_5_qty]
        ):
            if product_qty:
                itemDetails = productIventory[i]
                itemDetails["item_qty"] = product_qty
                ordered_item.append(itemDetails)
        if len(ordered_item):
            order["ordered_item"] = ordered_item
            print(
                "========================================================================\n"
            )
            print(order)
            print(
                "========================================================================\n\n"
            )
        return (
            f"there are {input_clicks} and values {prod_1_qty},{prod_2_qty},{prod_3_qty},{prod_4_qty},{prod_5_qty}.",
            initialLayout,
        )
    else:
        return (False, initialLayout)


if __name__ == "__main__":
    app.run_server(debug=False)
