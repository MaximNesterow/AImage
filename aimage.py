import pixellib
import tensorflow
from pixellib.instance import instance_segmentation
def aimage():
    predmet=instance_segmentation()
    predmet.load_model()
def poisk():
    aimage()
if __name__=='__name__':
    poisk()
print("hello")
