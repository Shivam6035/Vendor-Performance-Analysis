# # This is dashboard

# import dash
# from dash import dcc, html, Input, Output
# import plotly.express as px
# import pandas as pd
# import sqlite3

# # 1. Connect to Database and Load Data
# db_path = r"C:\Users\6035s\Desktop\MLOPS\Vendor-Performance-Analysis\inventory.db"
# conn = sqlite3.connect(db_path)

# # Fetch the main summary table
# df_summary = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)
# conn.close()

# # 2. Initialize the Dash Web App
# app = dash.Dash(__name__)

# # 3. Build the Layout (The Frontend)
# app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif'}, children=[
    
#     # Dashboard Header
#     html.H1("Vendor Performance Dashboard", style={'textAlign': 'center', 'color': '#2C3E50'}),
#     html.Hr(),
    
#     # Interactive Slicer / Filter
#     html.Div([
#         html.Label("Select Vendor(s) to Filter:", style={'fontWeight': 'bold'}),
#         dcc.Dropdown(
#             id='vendor-filter',
#             # Populate dropdown with unique vendor names
#             options=[{'label': vendor, 'value': vendor} for vendor in df_summary['VendorName'].unique()],
#             value=df_summary['VendorName'].unique()[:5], # Default to first 5 vendors
#             multi=True # Allows selecting multiple, like Power BI
#         )
#     ], style={'width': '40%', 'paddingBottom': '30px', 'paddingTop': '10px'}),

#     # Visualizations Container
#     html.Div([
#         # Scatter Plot Component
#         html.Div(dcc.Graph(id='sales-vs-profit-scatter'), style={'width': '48%', 'display': 'inline-block'}),
        
#         # Bar Chart Component
#         html.Div(dcc.Graph(id='vendor-sales-bar'), style={'width': '48%', 'display': 'inline-block', 'float': 'right'})
#     ])
# ])

# # 4. Create Callbacks (The Interactivity Logic)
# @app.callback(
#     [Output('sales-vs-profit-scatter', 'figure'),
#      Output('vendor-sales-bar', 'figure')],
#     [Input('vendor-filter', 'value')]
# )
# def update_graphs(selected_vendors):
#     # Handle edge case where nothing is selected
#     if not selected_vendors:
#         return px.scatter(title="No Vendor Selected"), px.bar(title="No Vendor Selected")
        
#     # Filter the DataFrame based on the dropdown selection
#     filtered_df = df_summary[df_summary['VendorName'].isin(selected_vendors)]
    
#     # Visual 1: Scatter Plot (Sales vs Profit Margin by Brand)
#     fig_scatter = px.scatter(
#         filtered_df, 
#         x='TotalSalesDollars', 
#         y='ProfitMargin', 
#         color='Brand',
#         size='TotalSalesQuantity',
#         hover_name='Description',
#         title="Brand Performance: Sales vs. Profit Margin",
#         template="plotly_white"
#     )
    
#     # Visual 2: Bar Chart (Total Sales by Vendor)
#     fig_bar = px.bar(
#         filtered_df, 
#         x='VendorName', 
#         y='TotalSalesDollars', 
#         color='VendorName',
#         title="Total Sales Dollars by Vendor",
#         template="plotly_white"
#     )
    
#     return fig_scatter, fig_bar

# if __name__ == '__main__':
#     # debug=True allows the dashboard to auto-update when you save code changes
#     app.run(debug=True, port=8080)

#---- 2nd testing Dashboard -----------------##-------------------------------------------------------- 


import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# 1. Connect to Database and Load Data
db_path = r"C:\Users\6035s\Desktop\MLOPS\Vendor-Performance-Analysis\inventory.db"
conn = sqlite3.connect(db_path)
df_summary = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)
conn.close()

# 2. Initialize the Dash Web App
app = dash.Dash(__name__)

# CSS styling for the Power BI-style KPI Cards
card_style = {
    'display': 'inline-block',
    'width': '28%',
    'margin': '1%',
    'backgroundColor': '#ffffff',
    'borderRadius': '10px',
    'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
    'padding': '20px',
    'textAlign': 'center',
    'borderTop': '5px solid #2C3E50'
}

# 3. Build the Layout
app.layout = html.Div(style={'fontFamily': 'Segoe UI, Arial, sans-serif', 'backgroundColor': '#f4f6f9', 'padding': '20px'}, children=[
    
    html.H1("Vendor Performance Dashboard", style={'textAlign': 'center', 'color': '#2C3E50', 'marginBottom': '30px'}),
    
    # Interactive Slicer
    html.Div([
        html.Label("Filter by Vendor:", style={'fontWeight': 'bold', 'color': '#333'}),
        dcc.Dropdown(
            id='vendor-filter',
            options=[{'label': vendor, 'value': vendor} for vendor in df_summary['VendorName'].unique()],
            value=df_summary['VendorName'].unique()[:5], 
            multi=True 
        )
    ], style={'width': '50%', 'margin': '0 auto', 'paddingBottom': '30px'}),

    # ---------------- NEW: Top Descriptive Summary (KPI Cards) ----------------
    html.Div(style={'textAlign': 'center', 'marginBottom': '30px'}, children=[
        html.Div([
            html.H4("Total Sales", style={'color': '#7f8c8d', 'margin': '0'}),
            html.H2(id='kpi-sales', style={'color': '#27ae60', 'margin': '10px 0 0 0'})
        ], style=card_style),
        
        html.Div([
            html.H4("Average Profit Margin", style={'color': '#7f8c8d', 'margin': '0'}),
            html.H2(id='kpi-margin', style={'color': '#2980b9', 'margin': '10px 0 0 0'})
        ], style=card_style),
        
        html.Div([
            html.H4("Total Items Sold", style={'color': '#7f8c8d', 'margin': '0'}),
            html.H2(id='kpi-quantity', style={'color': '#e67e22', 'margin': '10px 0 0 0'})
        ], style=card_style)
    ]),
    # --------------------------------------------------------------------------

    # Visualizations Container
    html.Div([
        html.Div(dcc.Graph(id='sales-vs-profit-scatter'), style={'width': '49%', 'display': 'inline-block', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),
        html.Div(dcc.Graph(id='vendor-sales-bar'), style={'width': '49%', 'display': 'inline-block', 'float': 'right', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
    ])
])

# 4. Create Callbacks (Link Slicer to Cards AND Graphs)
@app.callback(
    [Output('kpi-sales', 'children'),
     Output('kpi-margin', 'children'),
     Output('kpi-quantity', 'children'),
     Output('sales-vs-profit-scatter', 'figure'),
     Output('vendor-sales-bar', 'figure')],
    [Input('vendor-filter', 'value')]
)
def update_dashboard(selected_vendors):
    # Handle edge case where nothing is selected
    if not selected_vendors:
        return "$0", "0%", "0", px.scatter(title="No Vendor Selected"), px.bar(title="No Vendor Selected")
        
    # Filter the DataFrame
    filtered_df = df_summary[df_summary['VendorName'].isin(selected_vendors)]
    
    # Calculate KPIs dynamically based on the filtered data
    total_sales = filtered_df['TotalSalesDollars'].sum()
    avg_margin = filtered_df['ProfitMargin'].mean()
    total_quantity = filtered_df['TotalSalesQuantity'].sum()
    
    # Format the KPI text
    kpi_sales_text = f"${total_sales:,.2f}"
    kpi_margin_text = f"{avg_margin:,.2f}%"
    kpi_quantity_text = f"{total_quantity:,.0f}"
    
    # Visual 1: Scatter Plot
    fig_scatter = px.scatter(
        filtered_df, 
        x='TotalSalesDollars', 
        y='ProfitMargin', 
        color='Brand',
        size='TotalSalesQuantity',
        hover_name='Description',
        title="Brand Performance: Sales vs. Profit Margin",
        template="simple_white"
    )
    
    # Visual 2: Bar Chart
    fig_bar = px.bar(
        filtered_df, 
        x='VendorName', 
        y='TotalSalesDollars', 
        color='VendorName',
        title="Total Sales Dollars by Vendor",
        template="simple_white"
    )
    
    # Return 5 items matching the 5 Outputs listed in the @app.callback
    return kpi_sales_text, kpi_margin_text, kpi_quantity_text, fig_scatter, fig_bar

# 5. Run the Local Server
if __name__ == '__main__':
    app.run(debug=True, port=8080)
    