from math import pi
from cairo import Context, ImageSurface, FORMAT_ARGB32


WIDTH = 3
HEIGHT = 3
PIXEL_SCALE = 100


surface = ImageSurface(FORMAT_ARGB32, WIDTH*PIXEL_SCALE,
                             HEIGHT*PIXEL_SCALE)
ctx = Context(surface)

ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

# face
ctx.arc(1.5, 1.8, 1, 0, 2 * pi)

ctx.close_path()

ctx.set_source_rgb(1, 5, 0)
ctx.fill_preserve()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.05)
ctx.stroke()

ctx.fill()

# eye - left
ctx.arc(1, 1.6, 0.3, 0, 2 * pi)
ctx.close_path()

ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.01 )
ctx.stroke()
ctx.fill()
# globe eye - left
ctx.arc(1, 1.6, 0.1, 0, 2 * pi)
ctx.close_path()

ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.stroke()
ctx.fill()


# eye - right
ctx.arc(2, 1.6, 0.3, 0, 2 * pi)
ctx.close_path()

ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.01)
ctx.stroke()
ctx.fill()
# globe eye - right
ctx.arc(2, 1.6, 0.1, 0, 2 * pi)
ctx.close_path()

ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.stroke()
ctx.fill()


# eyebrow - left
ctx.move_to(0.8 , 1.2)
ctx.curve_to(0.8, 1.2, 1, 1.2, 1.2, 1.2 )   
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.06)
ctx.stroke()
ctx.fill()


# eyebrow - right
ctx.move_to(1.7, 1.2)
ctx.curve_to(1.8, 1.3, 2, 1, 2.2, 1.2 )    
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.06)
ctx.stroke()
ctx.fill()

#mouth
ctx.move_to(1, 2.3)
ctx.line_to(2, 2.3 )
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png('emoji.png')