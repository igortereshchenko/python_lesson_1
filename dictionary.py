import plotly.graph_objects as go

user_info = {
                'name': 'Igor',
                'age': 32,
                'countries': {
                                'IT': {
                                       '10.08.2000': 'IBIS',
                                       '10.08.2010': 'HILTON',
                                      },

                                'DE': {
                                       '10.08.2019': 'IBIS',
                                      }

                             }
            }


user_countries = user_info['countries']
search_country = 'IT'

if search_country in user_countries.keys():
    hotels_info = user_countries[search_country]
    print(hotels_info.values())
else:
    print('No data found')




new_data = {
    "PL":    {
                '10.08.2019': 'Warshava',
                '10.11.2019': 'Warshava'
             }
}
user_info['countries'].update(new_data)

print(user_info)


# IBIS: 2
# HILTON 1
statisics = dict()

for hotels in user_info['countries'].values():
    # print(country, hotels)
    for data, hotel in hotels.items():
        # print(data, hotel)
        # print(hotel)

        if hotel in statisics:
            statisics[hotel] += 1
        else:
            statisics[hotel] = 1


print(statisics)


fig = go.Figure( go.Bar( x=list(statisics.keys()),  y=list(statisics.values()))  )
fig.write_html('statistics.html',auto_open=True)



fig2 = go.Figure( go.Pie( labels=list(statisics.keys()),  values =list(statisics.values()))  )
fig2.write_html('statistics2.html',auto_open=True)