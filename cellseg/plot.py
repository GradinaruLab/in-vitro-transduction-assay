# Plotting tools
import bokeh
from bokeh.plotting import figure

def imshow(im, cmap=None):
    p = bokeh.plotting.figure(frame_height=400,
                              tools="pan,box_zoom,wheel_zoom,save,reset",)
    p.image(image=[im], 
            x=0, 
            y=1, 
            dw=1, 
            dh=1, 
            color_mapper = bokeh.models.LinearColorMapper(cmap))
    
    return(p)

def show_two_ims(im_1, 
                 im_2, 
                 color_mapper=None):
    
    """Convenient function for showing two images side by side."""
    
    p_1 = imshow(im_1,
                 cmap=color_mapper[0])
    
    p_2 = imshow(im_2,
                 cmap=color_mapper[1])
    
    p_1.xaxis.major_label_text_font_size = '12pt'
    p_1.yaxis.major_label_text_font_size = '12pt'

    p_2.xaxis.major_label_text_font_size = '12pt'
    p_2.yaxis.major_label_text_font_size = '12pt'

    p_1.xaxis.axis_label_text_font_size = '18pt'
    p_1.yaxis.axis_label_text_font_size = '18pt'

    p_2.xaxis.axis_label_text_font_size = '18pt'
    p_2.yaxis.axis_label_text_font_size = '18pt'
    
    
    p_2.x_range = p_1.x_range
    p_2.y_range = p_1.y_range
    
    p_1.output_backend = "svg"
    p_2.output_backend = "svg"
    
    return bokeh.layouts.gridplot([p_1, p_2], ncols=2)
        
