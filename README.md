# Machine Learning - DHISHNA-2k19
 ##Day 1:
   
   -Intro: Training with data for a purpose
-Data mining: Collecting data from large data area.
-Types: 1.Supervised learning
        2.Unsupervised
        3.Reinforcement
-Supervised: --Training data with label
 --Based on testing data

-Unsupervised: No label given.
  --All data given for training. Labelled based on similarity which is created by the system.
-Reinforcemnt:
  --Feedback obtained during running and this is used to catagorize data.
   --eg:chess(cant predit next movemnt)
   --realtime data training

-Algorthm must be anallyzed.
-Ml can be done in any language.
-For python,IDLE-- Software:Anaconda has many libraries,packages for ml.
-Enabling python for Anaconda
-hello world in python
-Preprocessing: data needs to be preprocessed before training.
-numpy: create arrays
-ski-learn: pre functions and packages available for ml. 
   ::preprocessing.  from sklearn import preprocessing  - preprocessing.x 
       - use 'as' for abbreviation for 
-Mean removal, standard deviation
-scale :standard,minmap,organised

standard:data scaled to 0 , standard deviation as 1
minmap: scaled to a range (0 to 1), 

-Normalizer L1,L2
  l1:least absolute deviation l2:least squares
l1: result of normalisation is an array.. and the absolute sum of row is always 1
l2: result is an array... square of each element in a row and sum them we get 1.

- Normalised class in preprocessing
 we create object and pass data to get l1 normalization

 -Binarization: Setting limit to data 
  giving raw data -- >threshold then binerized to 1 and <threshold binerized to 0.

  -Label encoding: 
   machine cant understand text, it only understand numbers.
     number is labelled or assigned to text. processing based on label. 
   fit and transform is used for same excpt that transform can be used later using inverse_transform but fit cannot

-Data Analysis : iris
