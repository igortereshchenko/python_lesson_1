import plotly.graph_objects as go



diagram = go.Bar(x=['Bob', 'Boba', 'Boban'], y=[12, 43, 36])

figura = go.Figure(data=diagram)

figura.write_html('figura.html',auto_open = True)