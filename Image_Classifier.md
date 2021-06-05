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
  <tbody>
    <tr>
      <th>0</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>1</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>2</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>3</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>4</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>5</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>6</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>7</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>8</th>
      <td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAJp0lEQVR4nCXUSW8c6XkA4O/9tlq6qnplkxRJUaSoGY4EjSbxyDNxnIPh2B7Ah+QawHf/rRyDLJcAARwMJkAcx8YkHkuiKI42biKbzd6rq2v79hzy/IgH7v/lUzCEc98aRwAfPNqwsCzTijC/KrSzoCXVyklbhiE464SQQqC//sXfcp+8fvOCAFDg/fU96fKqmqeLBXZNhsO13XtPvnhqREEBOaVqKepGEFEAWVZ+QmVtZJYzygERqzRYAGktxlIpY12Vy9cnzxsxvXx/GvKw1Uy4x2o7GQ/HdQmMZlG4Rib263/9ozWEFnnhtOWMy7qI4oRZ4lvW8SKFldWkXEmOCOO4qJ2plSiF0NY5e3l62u74PvE8zFWpJqMP4AtZWVGaGtWiLhWMlKiqStMf/dlTi/Dg7PTz3YOP9g4iz4sbPicMYTAKSakUQhajoq7LulxM58PZfJSlS5E7o5UywKzRRqTG+dIYC8YoZaUswxi0QMgh+OZ3f0iF/s0//P1dRh7u30882mA+sZxbP2EBiyIa+pSH9TKtLq/rVb4S1bIWqTMpEh8Wi2udjaoszVeWKiG1ktpIZMF1+741tiwVPTo+mmTi8sNgGpKyHTtZpZO5G2dPBC4IdX6DhclmsxVk1a1cSQarrJDSaguAHEN4rxG2MT+i1VIrURqMyMHOLnhRbXPGSLdD6B//5TdXdTGbXOw++vxWRvV8OZ1Wm1k5kOh0r12VZbe93mhFqlzFv/zJ2cL84ZvfYVyNb2eUMGNtCxQIG0be2gbutA98MCR5UsX3hTYGuAFM93bZ6rzOg6C3hUV9s8pvysU01NYFEel4oqpQrPOuDQr/fJSeTUyJE4Zxssm7/Z6oi/5ey1C/Gs2++HTO/dZgSp99uAjxKA6iyQdzenRO93/SGNdEQ9LxCSGuBVwOIJFEJ7rXcTevU1JhxoXJ9XwgA9woSlnOF0nkDtei6ZV68VLeuUc67f5wsko6y1fvPd2ALEckIPlqbOYndDEsfiRD/PHaxYqkUpZTnTAvduW3F0WeqVK6wZtJQ7FHK5Z0E9TwqEs96gJukzabD0WdLmWuvbVwliaFroajqr3lI1Ss5ia9mficUHg/ffLWqLqx6Xuo35l+1L+cjnvZ6XbDu6UcWTU8yxZXYru7OTHsAmVM1pggipgusDOwHqGNVqOT8JvpxmSBN3YSRkut0nxShySi7S7Vi8JoJYfVvo2iuS67Scj5+g++/HNHLpeLi3R2zqKBlhTQWlYflxVowZDjyKveTf3cREUdzSj3sVnovKDCYzgMvKjf2+H7D5DIUwoC3cS6DmhnvKSXS5gljZD5W9vbjd6DO/fLnfvT+ex6MfeVMw5vVsIpi52LGPFua+UMBuKvsD7NN7W55vF/fnj7YTGDsL2+3W92uoo2aRu5/yrzOUV312M2KlKzVAsVDScybpM7O0F/c6/bv7+1vxRCB/6T4cSdn9uq5H4IHtfcw0nbJk2FwDVbaTP+rHv5duAfT9Lv3xwdaydoSNO2d/wOB8nWlSmaYEvipEOUobpe6gvhDa5ps0u292zoBwe7jb/43H360E3n9nZihfbjFgpCSzmnzGEaCNdf2/601/+qrGbz9MVo9PXgkqrDtr3MEYGBow+sVQZpbZSzivvYZ6LMw+vsdjRI4+CT81P/4GPy8JAefoQOD9Eyt+O5EQprRarcGKOENEpF1vqEtyh9tLPzN0lEg653/2G34e2bybgY3CpOHXYOuNYaysX/V93UKMxB51fF1TU7ekEPD+nHh3j/rnt8F//PyfLlu0KreDAoy3xVlZW1iyhcKARRvOUBzYv9RvhulZUiX33SjXUtjNYGnAGLKXIOmdogp4izAnNsjBhekemIHb8kDw7ow4c6K5/ttr/LswfHQzKfTbGdW5et7Wb5xAzf03s7dJh/HFFzp89+e/LK4vJhJ2pdK+WsRoYYAG2Vs8Ja7IAANmApIKxsNb3BizF6eXR1b+fk509nevohrKOK+Ts7lRYLI12/aRNeBIZO5kW2amzH5c1s9fr2+vV666cs3qWMWOOsQdYijMA6z7ljI17W9YYX/tBnUVlpXcsq+45kL8+6m/sP5EOznGb1Wq/WMitmCrta+ErklDE7LrXJznrrthaN17OsJDJLmk89f4NisBIR4kXRQsl/Xk5PALpBOHb6l+DAqLHVt5VKx7Ow/4hv33s3+a2+HiohqjxV1iCgAJYidRN7VSuAuwdb6eON9yfjN69v/3EyehvGP++uHTY4VNUCm5emvuLw4OCjpNN7Phj35OyBcSNGlFbw7L8V90aovj17xZhPOJPGOMwxBmQtzUZvsKMrXnUbqNegjXAragYvXwx+P1+dC/lXcfPHvt92+lxVLolXVaFTx/vtb4uyZ7R0utDWo0Tks9vZrUPYUaIBI4fBamuJrzFd2/+SuWo1eoaxb5ENE/bJ441mm756Mbq+TP9pMvzOD55EjVOCLCXSlnfaaxr4kNIP1hhTasbChI8Xw7KuCPcQZgDAqUekJQrj5jaNDn56x198P36OEaWMKJES5jZ2mq1u4/3J7NXR8MWsOK6LTpJsULx3sPt3v/r1N//+H6++//4kYHdphy2Ws7OrPO7E7ZbTGCRFNETNLbi3q/0GckN6+aevT9OLxdn5xnqPB4QAC7inmPZ99PgHa+1ecPz8djBYLstqnXJM/G//92g6X4DFyY+/+NnPfvHNv/1+OkoRcpK3W712qxPPa1uk1yp7np9ddXoO7hzuCyF6UfjVV1utnicq5XFKGDZWa10i6xUFOT6eXp7ONrp3H3/2ZDk/X8zq4TjvtFqfffnlUPHZXKvVvMzmoDNO5TJbFPkSGVfLorsZ05U02LlamWVmwhgJo600PnDGHLLEAfR78Q+/8LbuJOkI7t87yDret5M/1VI8f3V09Ow5MPABuNWFUDXG8VoTHK6EdIAwd3kt6VqntxhdCyWub+ZhhIOII+SUFsg5h7B22qmCEri7G7ditFoMudcC7JVFZrWx2lplK2cdQhYhTFBRCOdAGeHAEgdopalaZao2rSYtK3F5kd7b73LPae1wyIx1QgrPMz7zjIO4B7Pxu9l7NJ6Ms6JQxgABjAkG7AAhZBE4qWsEgBhQSoFihzCdziRGQcAwY3yZiXdvR1vbUX8tMtYYhBhpYOw5jBxClLj2BpKwaheoVftFoZQyCBBCFlNsEQWEMAbAgDAQggkBIIgqRxhG2oJ1zhFXlHowyIMwaLeZUpoxbiwSZQXYMaCe5/U3Yj/Ge4f98WgxmeZFbVVtykIp46x1gBAhAAQIAYwBOfd/pgg3CAEElcIAAAAASUVORK5CYII="/></td>
    </tr>
    <tr>
      <th>9</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>10</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>11</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>12</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>13</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>14</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>15</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>16</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>17</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>18</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>19</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <th>0</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>1</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>2</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
  </tbody>
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
  <tbody>
    <tr>
      <th>0</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>1</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>2</th>
      <td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAI+0lEQVR4nC3V2Y5l11kA4P9fw957rT2cserU0KOdJk6IiJRcRIoFOFzBPULimmdDURAS74EUJFt2EmIbd3d1dVWd+Zw9rLXX9HMBT/BdfrharAKTzJufvbz4l3/8h6sp8+C8z+0YGRuanEOiREAEBICcxUjH8/jt+6fvn/aTyxue2F++efaTT1Zo2gwxECFDjoxiohgTJQGIQASIu+O5N2Pz4qp3nafMBXQJo/eNLjjnKaUYQpI5KyqlU2ly92R/eL9+tVrc3txUpUaBGTLPYmKEBClECiERCQBAIMb5abAft/uff3btQhoceT6BcnpqH8aBphMFmJAlyHPM1ayqflZetJb+8/f/VahidrHgGQmBnADIJwxIQBgj8hTD/wOIzAb48LTrzTj0gx1IXcyg1qmQh/XHgoppXUqOImcAJIklcFMlnl0tXv3odb2YC7LkeHABIjLiAhFEShCJRcEQgYgAE5P3T/vd8eTHwfRpciOLZs6w6nv/uDm0Z1OpbLGoVSGCc4PpgdHl7eXNJy9QZ1IIRjpYD85BCNGHFEKEEL0XiCgQCRGQP+2P9+vtxSTjmNzQL3KV6UlZ7R4+PGyGM6ewul42TQURD+eOVc3N6kpPJ0/HQ61EWRSyUIHLTAoO4EfHYwreCcEg+ICMM8LOun3ib16+zlufeOTIGEFdVUrrw3atcrnZdW8/rJuq7o2dX1z89NPP5otlN6whZZxmmJBJhEwCei4dQ1Cciy+++OVXX359OBylLP727z7/xV//TV1h5+/8OHrvkafptPn0R28ywWN0Qz+0mz3jOSKnQDmTGcuS91WzuL167Z1huRyje3x6KzNUSslMiX/657//4je//PrrPxSF/tWvP6+bKrqzNeP9/Z2unl3drmSWLZfLUuX73XrztIkrAgAhBOP8dD6rmQaMuRbEfWLOh2533O4Od1qrqn4hMylms6oq1fJyXuQqVxXjjGEWY/J+HEzb9WUmGUPUSo+6PObtqb2fTKcJcAxxdH60ZrGcNrPS0ygVAoXObgMNnRkPJ63LUkipKHlVgBR5nhcyR3s2zvmLi0VVK6KUCBlDa+0wDKfzmcuMACJAijGm1LZdOVVZLjnPAF1KTCqGfQKAU3+oey04Y0opROFd5By5gBijKnSh5tNZzXiRUgSC0/G0Xq8Ph0NelM1kaoxhjAFw79L52DkfVcYSYEqgdAUMY/LWdQ/r9wKZTwm4SCF45ylEij4sFxfWsa47iywO/YBEjLMsy6q60fX06ub68fGxKkvGRfAEIEOgmAgF51LV1bxp9ud2l1IMMQghmXVjopSCF4Jv7u5j76+fv373uH94uO+GAIA3NzcQyRO7Xj1bXFw48EWjdF31pmcCrrMriAmTBULJ8qZc3FwlY4KQfDlfCmSSmEcEjCxLcng4mkP/F29+Pl+yyRTb3hGy+WzRnvvhw8ft08eryxVJBB5CMLP5DHkKzmUcBYQYGSWmMh31TBezsil1WTFg6ENIQMgZS6zk1dh6RnI2vyzryeVqVdf1drsNMT5/8fJ6dXHYPeqMTXVm2+OsVpLjfrN9+93342AwEgKFNB7P+6rRzaRCBowLkYgOp1PX911rJnqBSe52p0KVPtBms00pccG7rivy/Ob2+vvv/rT9eLea1L4/P7x/S27cPT7+27/+9j9+9+8f3t750Xbd8bDfIMQiZ4wlgZyJXJ7bNvaJJF5W009//NO2N8r5+WJeNxOl1GazRTgwxrwLyOj+/bvb1SJDCKNZTl6Yo56V1R+//KZtx8/+6idKZy661e2VBIaMC2QsL4pCq8EaWWnMymVVHdN4bA/L+bKuykLpsqy0qtu27zFd3t6+/+6PT49rKXMhpDM9je7Nq08W09PT9vTuT/8znTejt9G6ShbNbCKAMS7EfLHIqKumU4KcAk11+Xjer5/ui3ySF0qKXJdacGHG7vbV6xTser19/vJVoavten0+HCaVVlkxa3CqpyUvovGPPzx0u/OrH38iGBOS51pXg3QuhqzgNhh0YVrpcbCBRt/a86ldXl4pmc+bppreXC/n337zVVVWgxl22621o9alkGq1WpRaj+MwdCMgtWH49pvvBEVgIPNMi7zrulaJqtDaDr0SWT1beIGP7z4ctg+iYInniYTNuJDZ1c2NN93641079HUzgUzJTOVFYaw5t60LsShyIny8W4sYIxFIKbJCHrZtrKKeTFWuUwgMGUtRMaFkFv1IyGOI7enAKDKGp9Px6elBN5OqrjmTiQgAATER5Xne90PbtsYMgghC8IwzrTICH2JIwLKsQElE0XVnzfKr+RKqLAPOMYHgKQTr/eFwYFzUVSWECD4Skdaaki+KIqV0Op0IqKpqkVKKKcbkgMVc8YTOxxi9R0gMYrve3//396vn19XFxFvDkYg8Uezbc4xJlyUXIoQwGMtQWGtTIs5527ZFUeR57p0XRJBSimm0ts8KjGgjOSLmncHk/vzVH/78+y9/9ZvPm9t5jD7YkQCMMX3fAaL3MaU0jmMIgSFuNhtKIQQHAIyxruuMMQIAUgoxeufM6NrIKNJVJjUBumEUCRVmPJKzY9+e/WABsO1aMwx933vvY4gpkRlMnuvz+Tz0rdbFdDpNKWmt8zwXQJRiDN4755y3jpIZrc4ZJx5SvH55u6ybxbPlfr/t2gO5YOxorbXOb7abuq59CDGmGOM4WmP6ELy1YK1tmiYvCjeOIgXnjPXBkwc3jiGG0UFIAMgSSHlZ62XZmb49HUzXIqF3wdrxcD4ZaxbLZfABAIUQROn/lkOWM84JIMZgrBXn8/lwOBBEmYkY4+nUDRPjqsAxMsajYGYcjR/H0Y12lDwzdux7s98fpcwAoO8HKWVRFIhIRHmRa62JqG1bInLOi/VuczoeCyVrWRVFMXzcPD08LptVniUgkDKDEDab7f3bd+RdnivkfLDWh7iYzUbnKSUpJefM2lEpJaWMMZ5PJyGlKoqyVGKz3R0OO10Wg+m5DHawH7v724vnTZM7O1o77DdPb39493B3Z7qurOpmOhu901WdAI1zAhARnQ8pJUQ8Ho8hhLwoaq0zKb33/wsZJes/eaoYwAAAAABJRU5ErkJggg=="/></td>
    </tr>
  </tbody>
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
