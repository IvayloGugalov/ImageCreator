from PIL import Image, ImageFont, ImageDraw, ImageEnhance


# def drawRectangle(image, vertices):
#     draw = ImageDraw.Draw(image)
#     for i in range(len(vertices) - 1):
#         draw.line(((vertices[i].x, vertices[i].y), (vertices[i + 1].x, vertices[i + 1].y)),
#                 fill='green',
#                 width=4
#         )

#     draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
#         (vertices[0].x, vertices[0].y)),
#         fill='green',
#         width=4
#     )
    
#     return draw
