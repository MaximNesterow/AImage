from pixellib.instance import instance_segmentation
def aimage():
    predmet=instance_segmentation()
    predmet.load_model("")
    predmet.segmentImage(image_path="", show_bboxes=True, output_image_name="OK")
def poisk():
    aimage()
if __name__ == '__main__':
    poisk()
