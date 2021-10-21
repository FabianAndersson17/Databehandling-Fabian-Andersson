from numpy.lib.shape_base import tile
import plotly_express as px

gapminder = px.data.gapminder()
nordic = gapminder[gapminder["country"].isin(["Sweden", "Norway", "Denmark", "Iceland", "Finland"])]
europe = gapminder[gapminder["continent"].isin(["Europe"])]
asia = gapminder[gapminder["continent"].isin(["Asia"])]


fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", 
                 size="pop", color="country", size_max = 70,
                 log_x=True, animation_frame="year", title="Gapminder",
                 range_x= [100, 100000], range_y=[25, 90])
fig.show()

fig2 = px.line_3d(asia, x="year", y="pop", z="gdpPercap", color="country", 
                    title="Nordic countries GDP per capita 1952-2007",
                    labels=dict(gpdPercap = "GDP/capita", year = "Year", country = "Country"))
fig2.show()
