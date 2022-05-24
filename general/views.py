from django.shortcuts import render
import tensorflow as tf
import os
from pathlib import Path
from .forms import InputForm
# Create your views here.

#home page
def index(request):
    return render(request, 'general/index.html')

#ml interface
def interface(request):
    imported = tf.saved_model.load(os.path.join(Path(__file__).resolve().parent.parent, r'general/tf_models/1653176436'))

    if request.method=='POST':
        form = InputForm(request.POST, request.FILES)
        distance_from_shore = float(form.data.get('distance_from_shore'))
        distance_from_port =  float(form.data.get('distance_from_port'))
        speed = float(form.data.get('speed'))
        course = float(form.data.get('course'))
        lat = float(form.data.get('lat'))
        lon =  float(form.data.get('lon'))

        prediction_raw = makeprediction(distance_from_shore, distance_from_port, speed, course, lat, lon, imported)
        prediction_tensor = str(prediction_raw['probabilities'])
        prediction_number_index = prediction_tensor.find("numpy=array")
        prediction_number = prediction_tensor[prediction_number_index+15:prediction_number_index+18]
        return render(request, 'general/prediction.html', {'prediction_raw' : prediction_raw, 'prediction_tensor': prediction_tensor, 'prediction_number': prediction_number})
    else:
        form = InputForm
    return render(request, 'general/interface.html', {'form' : form})



def makeprediction(distance_from_shore, distance_from_port, speed, course, lat, lon, imported):
   example = tf.train.Example()
   example.features.feature["distance_from_shore"].float_list.value.extend([distance_from_shore])
   example.features.feature["distance_from_port"].float_list.value.extend([distance_from_port])
   example.features.feature["speed"].float_list.value.extend([speed])
   example.features.feature["course"].float_list.value.extend([course])
   example.features.feature["lat"].float_list.value.extend([lat])
   example.features.feature["lon"].float_list.value.extend([lon])
   return imported.signatures["predict"](examples=tf.constant([example.SerializeToString()]))