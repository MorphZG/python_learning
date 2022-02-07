import colorgram

# use colorgram to extract colors from the image
# turtle module works with tuples so store colors to list of RGB tuples
rgb_tuples = []
colors = colorgram.extract('image.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    rgb_tuples.append(color_tuple)

print(rgb_tuples)








#modules: turtle
#tags: turtle drawing,
