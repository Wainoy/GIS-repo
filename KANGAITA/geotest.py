import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon

# Read the CSV file
df = pd.read_csv('E:/KANGAITA/JUNE 2025/revised_polygons.csv')

# Create geometry column from X and Y coordinates
df['geometry'] = df.apply(lambda row: Point(row.X, row.Y), axis=1)

# Convert DataFrame to GeoDataFrame
df = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")

# Initialize a list to store polygons
polygons = []

# Group by 'GrowersNo' and create polygons
for item, group in df.groupby('GrowersNo'):
    print("farm: ", item)
    print(group)
    
    if len(group) >= 3:
        poly = Polygon(zip(group.X, group.Y))
        polygons.append({'GrowersNo': item, 'geometry': poly})

# Create a GeoDataFrame from the list of polygons
polygon_gdf = gpd.GeoDataFrame(polygons, crs="EPSG:4326")

print(polygon_gdf)

# Save the GeoDataFrame to a shapefile
output_filepath='E:/KANGAITA/JUNE 2025/revised_polygons.shp'
polygon_gdf.to_file(output_filepath, driver="ESRI Shapefile")


