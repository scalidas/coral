# coral
Coral is a software that uses machine learning to predict potential illegal fishing operations. 

<i>By: Ayush Nayak, Sean Boerhout, Siddarth Calidas, Vignesh Nydhruva</i>

The first part of our project is about predicting whether a particular boat is fishing illegally or not, given some data. This model utilizes machine learning (the TensorFlow library) to make this prediction. 

We first traversed through a CSV file, which contained various data for a particular boat (course direction, speed, distance from port & shore, etc.), and we used a sample size of a few thousand boats. After running a linear regression model in TensorFlow, we were able to predict whether a boat was fishing illegeally or not, achieved an accuracy of about 92% (much higher than we expected). 
