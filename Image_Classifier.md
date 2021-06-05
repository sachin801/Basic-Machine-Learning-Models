```python
import turicreate as tc
```


```python
image_train=tc.SFrame('image_train_data')
```


```python
image_test=tc.SFrame('image_test_data')
```


```python
image_train['image'].head(20).explore()
```


<html lang="en">                                                     <head>                                                               <style>                                                              .sframe {                                                            font-size: 12px;                                                   font-family: HelveticaNeue;                                        border: 1px solid silver;                                        }                                                                  .sframe thead th {                                                   background: #F7F7F7;                                               font-family: HelveticaNeue-Medium;                                 font-size: 14px;                                                   line-height: 16.8px;                                               padding-top: 16px;                                                 padding-bottom: 16px;                                              padding-left: 10px;                                                padding-right: 38px;                                               border-top: 1px solid #E9E9E9;                                     border-bottom: 1px solid #E9E9E9;                                  white-space: nowrap;                                               overflow: hidden;                                                  text-overflow:ellipsis;                                            text-align:center;                                                 font-weight:normal;                                              }                                                                  .sframe tbody th {                                                   background: #FFFFFF;                                               text-align:left;                                                   font-weight:normal;                                                border-right: 1px solid #E9E9E9;                                 }                                                                  .sframe td {                                                         background: #FFFFFF;                                               padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr {                                                         padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr:hover {                                                   background: silver;                                              },                                                               </style>                                                         </head>                                                            <body>                                                               <h1>  </h1>                                             <table border="1" class="dataframe sframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SArray</th>
    </tr>
  </thead>
</table>                          </body>                                                          </html>


#Train a Classifier on the raw image pixels


```python
raw_pixel_model=tc.logistic_classifier.create(image_train,target='label',features=['image_array'])
```

    PROGRESS: Creating a validation set from 5 percent of training data. This may take a while.
              You can set ``validation_set=None`` to disable validation tracking.
    



<pre>Logistic regression:</pre>



<pre>--------------------------------------------------------</pre>



<pre>Number of examples          : 1904</pre>



<pre>Number of classes           : 4</pre>



<pre>Number of feature columns   : 1</pre>



<pre>Number of unpacked features : 3072</pre>



<pre>Number of coefficients      : 9219</pre>



<pre>Starting L-BFGS</pre>



<pre>--------------------------------------------------------</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| Iteration | Passes   | Step size | Elapsed Time | Training Accuracy | Validation Accuracy |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| 0         | 5        | 0.015956  | 1.220904     | 0.265756          | 0.247525            |</pre>



<pre>| 1         | 11       | 5.441038  | 1.521276     | 0.392857          | 0.336634            |</pre>



<pre>| 2         | 12       | 5.441038  | 1.607568     | 0.329307          | 0.297030            |</pre>



<pre>| 3         | 15       | 0.453885  | 1.773775     | 0.419118          | 0.277228            |</pre>



<pre>| 4         | 18       | 2.269426  | 1.958307     | 0.455882          | 0.415842            |</pre>



<pre>| 9         | 29       | 1.851979  | 2.639387     | 0.543067          | 0.485149            |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>


#MAking prediction with above models


```python
image_test[0:3]['image'].explore()
```


<html lang="en">                                                     <head>                                                               <style>                                                              .sframe {                                                            font-size: 12px;                                                   font-family: HelveticaNeue;                                        border: 1px solid silver;                                        }                                                                  .sframe thead th {                                                   background: #F7F7F7;                                               font-family: HelveticaNeue-Medium;                                 font-size: 14px;                                                   line-height: 16.8px;                                               padding-top: 16px;                                                 padding-bottom: 16px;                                              padding-left: 10px;                                                padding-right: 38px;                                               border-top: 1px solid #E9E9E9;                                     border-bottom: 1px solid #E9E9E9;                                  white-space: nowrap;                                               overflow: hidden;                                                  text-overflow:ellipsis;                                            text-align:center;                                                 font-weight:normal;                                              }                                                                  .sframe tbody th {                                                   background: #FFFFFF;                                               text-align:left;                                                   font-weight:normal;                                                border-right: 1px solid #E9E9E9;                                 }                                                                  .sframe td {                                                         background: #FFFFFF;                                               padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr {                                                         padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr:hover {                                                   background: silver;                                              },                                                               </style>                                                         </head>                                                            <body>                                                               <h1>  </h1>                                             <table border="1" class="dataframe sframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SArray</th>
    </tr>
  </thead>
</table>                          </body>                                                          </html>



```python
image_test[0:3]['label']
```




    dtype: str
    Rows: 3
    ['cat', 'automobile', 'cat']




```python
raw_pixel_model.predict(image_test[0:3])
```




    dtype: str
    Rows: 3
    ['bird', 'cat', 'bird']



#Evaluating raw pixel modl on test data


```python
raw_pixel_model.evaluate(image_test)
```




    {'accuracy': 0.48975, 'auc': 0.7373671250000002, 'confusion_matrix': Columns:
     	target_label	str
     	predicted_label	str
     	count	int
     
     Rows: 16
     
     Data:
     +--------------+-----------------+-------+
     | target_label | predicted_label | count |
     +--------------+-----------------+-------+
     |     bird     |       cat       |  152  |
     |     cat      |       cat       |  311  |
     |     dog      |       cat       |  217  |
     |     bird     |       dog       |  141  |
     |  automobile  |       bird      |  121  |
     |     bird     |       bird      |  567  |
     |     cat      |       bird      |  203  |
     |     dog      |       dog       |  414  |
     |     cat      |       dog       |  331  |
     |     dog      |    automobile   |   99  |
     +--------------+-----------------+-------+
     [16 rows x 3 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns., 'f1_score': 0.4840439689901386, 'log_loss': 1.1801779660030325, 'precision': 0.48227179783761254, 'recall': 0.48974999999999996, 'roc_curve': Columns:
     	threshold	float
     	fpr	float
     	tpr	float
     	p	int
     	n	int
     	class	int
     
     Rows: 4004
     
     Data:
     +-----------+----------------+-------+------+------+-------+
     | threshold |      fpr       |  tpr  |  p   |  n   | class |
     +-----------+----------------+-------+------+------+-------+
     |    0.0    |      1.0       |  1.0  | 1000 | 3000 |   0   |
     |   0.001   | 0.998666666667 |  1.0  | 1000 | 3000 |   0   |
     |   0.002   | 0.996333333333 |  1.0  | 1000 | 3000 |   0   |
     |   0.003   | 0.992333333333 |  1.0  | 1000 | 3000 |   0   |
     |   0.004   | 0.985333333333 |  1.0  | 1000 | 3000 |   0   |
     |   0.005   | 0.981666666667 |  1.0  | 1000 | 3000 |   0   |
     |   0.006   |     0.978      |  1.0  | 1000 | 3000 |   0   |
     |   0.007   | 0.972333333333 | 0.998 | 1000 | 3000 |   0   |
     |   0.008   | 0.965666666667 | 0.996 | 1000 | 3000 |   0   |
     |   0.009   | 0.960333333333 | 0.996 | 1000 | 3000 |   0   |
     +-----------+----------------+-------+------+------+-------+
     [4004 rows x 6 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.}



#Using Deep Features


```python
len(image_train)
```




    2005




```python
deep_learning_model=tc.load_model('imagenet_model')
image_train['deep_features']=deep_learning_model.extract_features(image_train)
```


```python
image_train.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">deep_features</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">image_array</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">24</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.242871761322,<br>1.09545373917, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[73.0, 77.0, 58.0, 71.0,<br>68.0, 50.0, 77.0, 69.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">33</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.525087952614, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[7.0, 5.0, 8.0, 7.0, 5.0,<br>8.0, 5.0, 4.0, 6.0, 7.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.566015958786, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[169.0, 122.0, 65.0,<br>131.0, 108.0, 75.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">70</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.12979578972, 0.0, 0.0,<br>0.778194487095, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[154.0, 179.0, 152.0,<br>159.0, 183.0, 157.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">90</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.71786928177, 0.0, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[216.0, 195.0, 180.0,<br>201.0, 178.0, 160.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">97</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">automobile</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.57818555832, 0.0, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[33.0, 44.0, 27.0, 29.0,<br>44.0, 31.0, 32.0, 45.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">107</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">dog</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0,<br>0.220677852631, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[97.0, 51.0, 31.0, 104.0,<br>58.0, 38.0, 107.0, 61.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">121</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.23753464222, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[93.0, 96.0, 88.0, 102.0,<br>106.0, 97.0, 117.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">136</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">automobile</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0, 0.0, 0.0, 0.0,<br>0.0, 7.5737862587, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[35.0, 59.0, 53.0, 36.0,<br>56.0, 56.0, 42.0, 62.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">138</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">bird</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.658935725689, 0.0,<br>0.0, 0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[205.0, 193.0, 195.0,<br>200.0, 187.0, 193.0, ...</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>



# Training a classifier


```python
deep_features_model=tc.logistic_classifier.create(image_train,features=['deep_features'],target='label')
```

    PROGRESS: Creating a validation set from 5 percent of training data. This may take a while.
              You can set ``validation_set=None`` to disable validation tracking.
    



<pre>Logistic regression:</pre>



<pre>--------------------------------------------------------</pre>



<pre>Number of examples          : 1904</pre>



<pre>Number of classes           : 4</pre>



<pre>Number of feature columns   : 1</pre>



<pre>Number of unpacked features : 4096</pre>



<pre>Number of coefficients      : 12291</pre>



<pre>Starting L-BFGS</pre>



<pre>--------------------------------------------------------</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| Iteration | Passes   | Step size | Elapsed Time | Training Accuracy | Validation Accuracy |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| 0         | 3        | 0.500000  | 0.241945     | 0.753676          | 0.752475            |</pre>



<pre>| 1         | 6        | 0.250000  | 0.532700     | 0.759979          | 0.772277            |</pre>



<pre>| 2         | 8        | 0.207867  | 0.752519     | 0.769433          | 0.772277            |</pre>



<pre>| 3         | 12       | 0.623600  | 1.140080     | 0.789916          | 0.782178            |</pre>



<pre>| 4         | 14       | 0.700386  | 1.360156     | 0.819328          | 0.801980            |</pre>



<pre>| 9         | 21       | 1.000000  | 2.296218     | 0.911765          | 0.811881            |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>


# Applying deep features model to first few images


```python
image_test[0:3]['image'].explore()
```


<html lang="en">                                                     <head>                                                               <style>                                                              .sframe {                                                            font-size: 12px;                                                   font-family: HelveticaNeue;                                        border: 1px solid silver;                                        }                                                                  .sframe thead th {                                                   background: #F7F7F7;                                               font-family: HelveticaNeue-Medium;                                 font-size: 14px;                                                   line-height: 16.8px;                                               padding-top: 16px;                                                 padding-bottom: 16px;                                              padding-left: 10px;                                                padding-right: 38px;                                               border-top: 1px solid #E9E9E9;                                     border-bottom: 1px solid #E9E9E9;                                  white-space: nowrap;                                               overflow: hidden;                                                  text-overflow:ellipsis;                                            text-align:center;                                                 font-weight:normal;                                              }                                                                  .sframe tbody th {                                                   background: #FFFFFF;                                               text-align:left;                                                   font-weight:normal;                                                border-right: 1px solid #E9E9E9;                                 }                                                                  .sframe td {                                                         background: #FFFFFF;                                               padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr {                                                         padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr:hover {                                                   background: silver;                                              },                                                               </style>                                                         </head>                                                            <body>                                                               <h1>  </h1>                                             <table border="1" class="dataframe sframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SArray</th>
    </tr>
  </thead>
</table>                          </body>                                                          </html>



```python
deep_features_model.predict(image_test[0:3])
```




    dtype: str
    Rows: 3
    ['cat', 'automobile', 'cat']



# Computing test data accuracy of above model


```python
deep_features_model.evaluate(image_test)
```




    {'accuracy': 0.79375, 'auc': 0.9413818333333334, 'confusion_matrix': Columns:
     	target_label	str
     	predicted_label	str
     	count	int
     
     Rows: 16
     
     Data:
     +--------------+-----------------+-------+
     | target_label | predicted_label | count |
     +--------------+-----------------+-------+
     |     bird     |       dog       |   59  |
     |     dog      |       cat       |  223  |
     |     bird     |       bird      |  795  |
     |  automobile  |       bird      |   17  |
     |  automobile  |       cat       |   21  |
     |  automobile  |    automobile   |  953  |
     |     bird     |    automobile   |   13  |
     |  automobile  |       dog       |   9   |
     |     dog      |    automobile   |   10  |
     |     cat      |       dog       |  206  |
     +--------------+-----------------+-------+
     [16 rows x 3 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns., 'f1_score': 0.7952918155791855, 'log_loss': 0.5947225590583349, 'precision': 0.7979992910711539, 'recall': 0.79375, 'roc_curve': Columns:
     	threshold	float
     	fpr	float
     	tpr	float
     	p	int
     	n	int
     	class	int
     
     Rows: 4004
     
     Data:
     +-----------+----------------+-------+------+------+-------+
     | threshold |      fpr       |  tpr  |  p   |  n   | class |
     +-----------+----------------+-------+------+------+-------+
     |    0.0    |      1.0       |  1.0  | 1000 | 3000 |   0   |
     |   0.001   | 0.436333333333 |  1.0  | 1000 | 3000 |   0   |
     |   0.002   | 0.338666666667 | 0.999 | 1000 | 3000 |   0   |
     |   0.003   | 0.290666666667 | 0.998 | 1000 | 3000 |   0   |
     |   0.004   | 0.257666666667 | 0.998 | 1000 | 3000 |   0   |
     |   0.005   | 0.236666666667 | 0.998 | 1000 | 3000 |   0   |
     |   0.006   |     0.218      | 0.998 | 1000 | 3000 |   0   |
     |   0.007   | 0.203666666667 | 0.998 | 1000 | 3000 |   0   |
     |   0.008   |      0.19      | 0.998 | 1000 | 3000 |   0   |
     |   0.009   | 0.179333333333 | 0.998 | 1000 | 3000 |   0   |
     +-----------+----------------+-------+------+------+-------+
     [4004 rows x 6 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.}




```python

```
