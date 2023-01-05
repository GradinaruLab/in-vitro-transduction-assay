# Image processing tools
import skimage.io
import glob

# Plotting tools
import bokeh
from bokeh.plotting import figure

import cellseg.quant

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
        
def single_image_viewer(path, round_, plate, well): 
        # Set the file directory to those images
    if well < 10:
        well_directory = path + '/round_' + str(round_) + '/plate_' + str(plate) + '/XY0'+ str(well) +'/'
    else:
        well_directory = path + '/round_' + str(round_) + '/plate_' + str(plate) + '/XY'+ str(well) +'/'
        
    # Collect the images at that well
    file_list = glob.glob(well_directory + '*.tif')
    
    # Initialize both the signal and autofluorescence image:
    im_sig = skimage.img_as_float(skimage.io.imread(file_list[0])[:,:,1])
    im_bf = skimage.img_as_float(skimage.io.imread(file_list[1])[:,:])
    im_dapi = skimage.img_as_float(skimage.io.imread(file_list[2])[:,:,2])

    # Perform the brightfield segmentation
    brightfield_areas, total_area = cellseg.quant.brightfield_segmentation(im_bf)

    # Perform the signal segmentation
    signal_areas, signal_total_area = cellseg.quant.signal_segmentation(im_sig)
    
    bf_plot = cellseg.plot.show_two_ims(im_bf, brightfield_areas, color_mapper=[bokeh.palettes.gray(256), bokeh.palettes.gray(256)])
    sig_plot = cellseg.plot.show_two_ims(im_sig, signal_areas, color_mapper=[bokeh.palettes.gray(256), bokeh.palettes.gray(256)])
    
    return(bf_plot, sig_plot)