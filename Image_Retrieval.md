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
image_train.head(5)
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
</table>
[5 rows x 5 columns]<br/>
</div>



# Train a nearest-neighbors model for retreiving images using deep features


```python
knn_model= tc.nearest_neighbors.create(image_train,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>


# Use image retreival model with deep features to find similar images


```python
cat= image_train[18:19]
cat['image'].explore()
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
knn_model.query(cat)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 9.666ms      |</pre>



<pre>| Done         |         | 100         | 87.825ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">query_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">reference_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">distance</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">384</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">6910</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.9403137951</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39777</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.4634888975</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36870</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.7559623119</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41734</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">39.7866014148</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
def get_images(query_result) :
    return image_train.filter_by(query_result['reference_label'],'id')
```


```python
cat_neighbours=get_images(knn_model.query(cat))
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 6.329ms      |</pre>



<pre>| Done         |         | 100         | 83.189ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
cat_neighbours['image'].explore()
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
car =image_train[8:9]
car['image'].explore()
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
car_neighbors=get_images(knn_model.query(car))
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 6.944ms      |</pre>



<pre>| Done         |         | 100         | 61.162ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
car_neighbors['image'].explore()
```


<html lang="en">                                                     <head>                                                               <style>                                                              .sframe {                                                            font-size: 12px;                                                   font-family: HelveticaNeue;                                        border: 1px solid silver;                                        }                                                                  .sframe thead th {                                                   background: #F7F7F7;                                               font-family: HelveticaNeue-Medium;                                 font-size: 14px;                                                   line-height: 16.8px;                                               padding-top: 16px;                                                 padding-bottom: 16px;                                              padding-left: 10px;                                                padding-right: 38px;                                               border-top: 1px solid #E9E9E9;                                     border-bottom: 1px solid #E9E9E9;                                  white-space: nowrap;                                               overflow: hidden;                                                  text-overflow:ellipsis;                                            text-align:center;                                                 font-weight:normal;                                              }                                                                  .sframe tbody th {                                                   background: #FFFFFF;                                               text-align:left;                                                   font-weight:normal;                                                border-right: 1px solid #E9E9E9;                                 }                                                                  .sframe td {                                                         background: #FFFFFF;                                               padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr {                                                         padding-left: 10px;                                                padding-right: 38px;                                               padding-top: 14px;                                                 padding-bottom: 14px;                                              border-bottom: 1px solid #E9E9E9;                                  max-height: 0px;                                                   transition: max-height 5s ease-out;                                vertical-align: middle;                                            font-family: HelveticaNeue;                                        font-size: 12px;                                                   line-height: 16.8px;                                               background: #FFFFFF;                                             }                                                                  .sframe tr:hover {                                                   background: silver;                                              },                                                               </style>                                                         </head>                                                            <body>                                                               <h1>  </h1>                                             <table border="1" class="dataframe sframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SArray</th>
    </tr>
  </thead>
</table>                          </body>                                                          </html>


# creating lambda to find and show neighbor images


```python
show_neighbors= lambda i: get_images(knn_model.query(image_train[i:i+1]))['image'].explore()
```


```python
show_neighbors(26)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 5.611ms      |</pre>



<pre>| Done         |         | 100         | 90.136ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



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
  </tbody>
</table>                          </body>                                                          </html>



```python
show_neighbors(1222)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 6.214ms      |</pre>



<pre>| Done         |         | 100         | 97.784ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



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
      <td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAEFElEQVR4nK2WTW8cRRCG37e6e2bHu+uN7Tgk5EOR+JIAcciFAz+EK/+HfwUniIWUkCAUIARCgMQfcWzHuzszXS+HXTtrvI6NSR3m0K2qt6um+qnmF19+JTlA/G+TdHwxAgRI/l8BSXODRJJv5PgnHdHeRPDXmf1XBwKEgGm5BQF+sHNOAUImMFOZbo7grTBuIcFby9lGQOOIc53nrx4JL5l8ckgn6+BAgjoAYpthHVkgxmINzUni9AxEiRBMiEJqgjJCyuzm9QGedbKb9wQD63NmIIQRE+FUNtV9DKs8XPAX1txpc92GWwjvAgnycwoACEChYc92umE4iMNe8IWwi3rv+1+3m8EIccxspgjm0wU07QYCBghyU9vDsKf1gf5cLYdlGhtbKu/uYTy+bulaQyY4YXPu8awA5aJlBELucLeSbZXq0p93d37a+ev+2Dera8scXEBIL7e3v/72SfXe5zENLDcgACd5nBdHMhBIICKXYb9Mw+Cj6DscP213fmn2HjNpf9RfWCyo6scHa0+e1R9+uuqWgwOgIE4uCTRfQCSAyJxfbm9uPKpsVKSUkrfjl91m7AJZFuWg6i1ubO0+ePiou/IxQpjHtxMzIABC9NZSX9X1nBZyCr2lnfLp1ihuMJQWqhAXvrtze3ekW5994kWZZxROoulheAnMslQtlv1ek8rssZUSR/XuGEgWoog/nmx+s3av6GB3zG4o5HNu1yxZbXYZkCPUVjZeoGZsWLXme83eblsU3cGFC2XVub12d+v5/vrW/tPNIXh6l0eC08RIIwUBBpjJKAOQcyx6K91qb2X54m+/v7j3w8NOqTr0OoMbTuO0eY7UZxbd8RUEaQCC8gSVbgKyABSFqtVcxL+fj9bu/pyRYmEol7uDKy4/jEVy7j84xqJjc4OhLJbfrzs37j9+sTGqY1VldnpLb1f9gftpPTQR4NGkyFcTlBBCYvdqU11fH8YcS8YiW3fp8jup6vtR/nCexbmnnvUC0CII3Tp3gqXQqTq4dOnqB84CbE9ym5TrQOAUcwKCReuUFq3kxaUrg9WrWQF4ncCkDGeYB0AmZEW/vxKQWJSLl2/G3hI8h5N/wWGRz4RrB2JRFYurobeaOmFx5aZiyTb/mzvnEyBgUAv137rmPlZT9/tXoAnddOqT50wCFFog9Zculh9x1MSyl/M0/Kl2hhJNYEN3MKYqhgXBJ08Vvbb/ThKYuMwwkqBIZAKUZQCc9tVR+h9qafohAMTsLZSBGGF0iQDNIdBnNEhx+t6yqS8PYgkUzURqQpeGcBKAOy12sC+0hgKgDGJ0hGMDdjqtDtDM2V3KITfPHSpGwerc1mVKCGodsbKx1BrUGDxYlpQlBSicVl4IBBSREz2GJiKnQLBV9GRybwLDP9sWBaPTqZv5AAAAAElFTkSuQmCC"/></td>
    </tr>
    <tr>
      <th>1</th>
      <td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAE3klEQVR4nHVWW28VVRhd65s5N6g9PW25CtKqhIYQNCQY1BAT/RO++7989dHoA4oPxEiIl0QJSQ1qYqTQFsEeSm1pey7zLR/23jNzWtzZzZnOnr2+2/ouvPVgIDlAHFqCymcyvAFBIh6QgBi/rdbEm9zMpIPoAkRRBKi6cKa/8i0DkNU+EVAKRk4SEhj0pUAJguIXwQoSgBRRVSJXksVJK0BAIJBXehESBXqAqhtU2ih5uk8waC+IyZDoRSRNhFxC0EygAEnCYZ9Vtyf/C7gJXVFu0okgckEOAXQBkADx5SFTTUJyiFSdM2hd3g225I5otSeECSBCABOHREEiUyAPqgFNslFAXgQDBTFKd9XYp/pPxJIiVRPYgZBNrFyAhyAm2iveVVDMMiuGo9H+sHm0A0IOkvQS3mtJUVc9Gp0LcFCVySUHCMBVPH2w9v2NrwebGxffe3fp2jtZq+NyVnAEFRkSb6o6gnKXHAItCU6xBkiOR8Ofbt25+dmn8z1tPfnDWFz44COIpJXcVaVT7Sce0kASBAgFmjJcJCmpdaR95frVcxcvnVp4rdMZ3//m8yf37tLoLoBSpbdCkmJCDAAzwBjTv252+IrM2ken8yO9qU7nxFTeerHy6LsvBpsbWZ6VOIqUECEoLUa6W6kBATLtUDQAE7KMY+HZzu7sbPf0uePPH/76bPkejYRiIOp5w0lGEUYyOihsiSHbKJLyojfXO7+0tFU0+rujqfljWbfz252bO6uP8jyDw0ATrCbByBoFYDHBSYs+AQkjjMwIONqd5ltXrzTa07+vrD/e+Ld7fPbBn8t3b94oBntGJ2SQpbyhDmyZkQQCurG2ARIZWYyKhfOLZ8++ubb+9Iefl5fv/9Xf2Vz+5c52v99oMEAbkEEZZHDCCZECRcIyKQMIhVAbaICBISpGcuzTM91r719vtU8839b644E1pgzCcECQZNKJaUf9MsCAnECWKoPHTGAsiXDCQOTMXpluH5898+HHn5y9sPDj7W831tZn5noYu0VCxJLMlKFxKTWcRAco1ty4AckgFN1u71jv6NxcZ/Hy5XZv5vaXX+3u7Mx3Z0ejgoArVUnUwQHCLMYVrNlFRhalJES3N9dqN/t/rw72h7OnTp9cOPdkZa3ZpEFmMZMYbUhboGCI0SBDTpcRRqwWsXDmnOr1OBjIi0Yzf/X1xa3+8+FgmJlB4ZYYfTyxLDWYwyaWzCakvNmenek1aDQbD/zY6dP7g0H/8VPLU1HihPMrAdGSlwlgGTLjaLhf7L6YmZ/L8ob7uNVpL719qdVueRErPVOBOSQgkDKu6qnMRklm3O5vrq+uN2e6oBGQcOaNxanujLyI3FBK2VJVEqQZSgZVRupQC2s0m+7w4bicW8bjwv1A9QzDT63V1Qem/1sk5D7V655cXByNRmTo4TSzwPB6vwoTSVlKXYpl6kCcQzOIC5Ara7Qa091/NrcKH5c+EeiABA9JmnpQuOeSAItn6UZ5XJmQJrrtvdHKw9XB3p5ExwR6qGweKhHgqlIvj9apctvk6KHoJGk4HKIozOhkaP1eDpjBA2GqCWELPgDy2CPL3hGtKeEZ5iIVjtFwbn4WzbYXqnXHOJYGYSU6ACeQxhbUP/aJ6YwCzLi3s7u7tbVw4pQDBQjCy6avhJueVetr/wGhad7TTZG0+QAAAABJRU5ErkJggg=="/></td>
    </tr>
    <tr>
      <th>2</th>
      <td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAFY0lEQVR4nH1W264kRxGMyKq5nvvZtfd4wRZG4gGeLNlIXP6An+Br+Bj+gw9ACCSMQLLkxfZe4dz2nOnujOChunvOmoXUTEvTU5WZFRkVmfzd7/8aBbUGw7YBALDhJAADgDG+BgACnH8GWQIAGYRZQBoGCCX7bpBdZYYBhKx3AtgAyWk7OPqcwgIG2Va11WHAHFMyjbBdAUoahjSlaStNum0ExjhmM4OcVmGMK6mlNZtNpWVXOAznIIVFjBkDdXKzB6fZfJYZssmx9CCAYMNilQyYdFoKByP+y/X/tzlvSbZB0LQjE7Zr2gCiwWwRZMNxH4YiTTkYMJl0MQII2uEx74YlRqJYsCgDNce/SmFUJ8EYkYoZGgGOBAuRZGcvYcIkSGiqCCJKagTQhItt1IdgzvjyIc4GjVBWZmHSCQ8YCTMW7ftgjbUByZam/YDr9v5CtLXmkihFogyD4OSYBGCTJKYv3glTbcMW1QI2wpVSJM2kIRTDXbFKDWFw9lZxFtYV6gJARBgwGIZtSY1aBGs7GW0ZtGzPWdgmA9aqu7w4uD5flN6u69LvMjNuru6+e9Xj/NPFapUw/gf15hrQVloACqNdMgIGCvJweLG9enZ+tD19dP62u8mK1fbwKq9fff3yevV4tdlIg/3+CHUC3wKBQpIRZi3I8K7HclF0ffXyL3/8w9lCv/7Fz09PV/d9d+1Vf3N1GMOd7mBVDz2XD08xXgiyWrbVcARogwKDMSqFg3r578s/ffnVSR0ub++ePjk/OjlZb0839OXVffmwdixkGViJ/VX2xLAqqQWYhACyQkLACNgVCePFq9eX+fb45PjZ8zdRVmfnj3/5+WePLj68PVjfwEGKDrzHaiMsgEabdg4ChAWSqO7V3VbayhzyzV23U//VixdD0cVHH3989uNatvBA9PJSkx4FKQJEHfF68CTZyGYjSPS3/3r2j08eHz05u1ivqhbHPVC0+O6bv/39yz8//eftZ7/57bKWtNVIvzfDrEpJ2WoQEbYzE4Ao0xXW7u3pYtheHJ9sl6XWEy+d/elmVZZnl7vV1dEnioOOpbmbfctOCUQVbFIw7fkS2BZMhtMc8umj46xvloXUsFks1rFdL7s8OHz6+IvXx1/clJUAWJPuNS2AEURUESRNyqZUSiFpQ0QBYRBxuFlu6sF6vYy7222guGrh45/+7Or8V9++3hb1BFLj/eWo29H0r4LTW5vW3LUABeASinpwdHzmWyIzdwtn5nD4wUcXP/n821erIUVAgFKpPT6SBBKIfVUmGXHrQQI0yBi44GItu+97lIUQWsThxac3/OD59dDIMHHdbvhITTEtV1tja49xJADJiHFhqsNix9Vdr+x69yr9sH10uHnyo6/fbq93bxttGjvbcKCxlrAMuLY7h1nUxxNxltYhll2s7zN290PXA51/sNlqc/78uXpFcN8GGrMxjRmSGU3sjHe10HjQPBKlw6q49CgDKyLq0dmtlpc3Kc9tDwYkN4UwKLuxpoZBC2pdhAAkk73CHaNIdkluBhbTFCqXB4c/vNPx/ZBhiIE2NBgKthOkkFNPDhrwfvQYiwMbUmOYKVQhBCmzMrYHZ7f37ge1bMZP22OmnBqbovF+gfqe0QgjZAxSWdSjo5PdbhikdGpv2bjUbD9delKh0VnTVE9DqQ3CKGY1w/R6u16uN30GWOcpYe7ibTSa5YBgBOeJ7d0qT4gBJBdGaScYlP2gXSd57vPzZMEWZ++PqKM+zzEfrMY4+pBRZQ6pzOyzH1K7LtNhKxiYiN1ct5xmROoExFTfNpwaFGAI6KVOWIhDr0wNUi902VtmCkibsGzCRIowAEG2aP4HvkJL6aoFXOEAAAAASUVORK5CYII="/></td>
    </tr>
    <tr>
      <th>3</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
    <tr>
      <th>4</th>
      <td><img src="data:image/png;base64,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"/></td>
    </tr>
  </tbody>
</table>                          </body>                                                          </html>



```python
show_neighbors(2000)
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.0498753   | 5.057ms      |</pre>



<pre>| Done         |         | 100         | 110.615ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



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
  </tbody>
</table>                          </body>                                                          </html>



```python
sketch= tc.Sketch(image_train['label'])
```


```python
sketch
```




    
    +------------------+-------+----------+
    |       item       | value | is exact |
    +------------------+-------+----------+
    |      Length      |  2005 |   Yes    |
    | # Missing Values |   0   |   Yes    |
    | # unique values  |   4   |    No    |
    +------------------+-------+----------+
    
    Most frequent items:
    +------------+-------+
    |   value    | count |
    +------------+-------+
    | automobile |  509  |
    |    cat     |  509  |
    |    dog     |  509  |
    |    bird    |  478  |
    +------------+-------+





```python
dog_data=image_train[image_train['label']=='dog']
```


```python
cat_data=image_train[image_train['label']=='cat']
```


```python
car_data=image_train[image_train['label']=='automobile']
```


```python
bird_data=image_train[image_train['label']=='bird']
```


```python
dog_knn_model=tc.nearest_neighbors.create(dog_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
cat_knn_model=tc.nearest_neighbors.create(cat_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
image_cats1=cat_knn_model.query(image_test[0:1])
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 5.366ms      |</pre>



<pre>| Done         |         | 100         | 31.691ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
cat_neigh1=get_images(image_cats1)
```


```python
cat_neigh1['image'].explore()
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
  </tbody>
</table>                          </body>                                                          </html>



```python
cat_neigh1
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
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">331</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.0, 0.0,<br>0.510963916779, 0.0,  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[45.0, 65.0, 92.0, 72.0,<br>95.0, 110.0, 106.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">16289</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.964287519455, 0.0,<br>0.0, 0.0, 1.12515509129, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[215.0, 219.0, 231.0,<br>215.0, 219.0, 232.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">25713</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.536971271038, 0.0,<br>0.0, 0.0894458889961, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[228.0, 222.0, 236.0,<br>224.0, 213.0, 222.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">32139</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[1.29409468174, 0.0, 0.0,<br>0.513800263405, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[217.0, 220.0, 205.0,<br>221.0, 227.0, 218.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45646</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Height: 32 Width: 32</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[0.983677506447, 0.0,<br>0.0, 0.0, 0.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">[51.0, 42.0, 26.0, 56.0,<br>47.0, 31.0, 59.0, 50.0, ...</td>
    </tr>
</table>
[5 rows x 5 columns]<br/>
</div>




```python
image_cats1
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">query_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">reference_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">distance</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">16289</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.623719208</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45646</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.0068799284</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">32139</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.5200813436</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">25713</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.7548502521</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">331</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.8731228168</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
image_test[0:1]['image'].explore()
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
  </tbody>
</table>                          </body>                                                          </html>



```python
image_cats1['distance'].mean()
```




    36.15573070978294




```python
dog_knn_model=tc.nearest_neighbors.create(dog_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
dog_neigh1=dog_knn_model.query(image_test[0:1])
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 4.829ms      |</pre>



<pre>| Done         |         | 100         | 30.368ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_neigh1
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">query_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">reference_label</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">distance</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">16976</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.4642628784</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">13387</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.5666832169</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">35867</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.6047267079</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">44603</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.7065585153</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">6094</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.5113254907</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
dog_neigh1['distance'].mean()
```




    37.77071136184157




```python
image_test_cat=image_test[image_test['label']=='cat']
```


```python
image_test_dog=image_test[image_test['label']=='dog']
```


```python
image_test_bird=image_test[image_test['label']=='bird']
```


```python
image_test_car=image_test[image_test['label']=='automobile']
```


```python
car_knn_model=tc.nearest_neighbors.create(car_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
dog_knn_model=tc.nearest_neighbors.create(dog_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
bird_knn_model=tc.nearest_neighbors.create(bird_data,features=['deep_features'],label='id')
```


<pre>Starting brute force nearest neighbors model training.</pre>



<pre>Validating distance components.</pre>



<pre>Initializing model data.</pre>



<pre>Initializing distances.</pre>



<pre>Done.</pre>



```python
dog_cat_neighbors=cat_knn_model.query(image_test_dog)['distance']
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 8</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 64000   | 12.5737     | 259.459ms    |</pre>



<pre>| Done         | 509000  | 100         | 315.196ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_dog_neighbors=dog_knn_model.query(image_test_dog)['distance']
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 8</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 64000   | 12.5737     | 278.405ms    |</pre>



<pre>| Done         | 509000  | 100         | 327.792ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_car_neighbors=car_knn_model.query(image_test_dog)['distance']
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 8</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 64000   | 12.5737     | 257.451ms    |</pre>



<pre>| Done         | 509000  | 100         | 319.887ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_bird_neighbors=bird_knn_model.query(image_test_dog)['distance']
```


<pre>Starting blockwise querying.</pre>



<pre>max rows per data block: 4348</pre>



<pre>number of reference data blocks: 8</pre>



<pre>number of query data blocks: 1</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 1000         | 60000   | 12.5523     | 242.189ms    |</pre>



<pre>| Done         | 478000  | 100         | 305.351ms    |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



```python
dog_distances=tc.SFrame({'dog-car':dog_car_neighbors,'dog-bird':dog_bird_neighbors,'dog-cat':dog_cat_neighbors,'dog-dog':dog_dog_neighbors})
```


```python
dog_distances.head(5)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-bird</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-car</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-cat</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">dog-dog</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.7538647304</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.9579761457</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.4196077068</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">33.4773590373</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.8665828436</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">44.1437321415</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">36.5151634774</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.415221599</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41.9679651276</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">44.477613787</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.0642580438</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.8138630061</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">42.2266731821</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45.1042420361</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.1217725492</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">34.9289313468</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">42.330722322</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">45.286528164</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">38.2837145836</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">37.1546409194</td>
    </tr>
</table>
[5 rows x 4 columns]<br/>
</div>




```python
def is_dog_correct(dog_distances):
    if min(dog_distances['dog-bird'],dog_distances['dog-car'],dog_distances['dog-cat']) < dog_distances['dog-dog'] :
        return 1
    else :
        return 0
```


```python
predicted_dog=dog_distances.apply(is_dog_correct)
```


```python
predicted_dog.sum()
```




    1446




```python
len(image_test_dog)
```




    1000




```python
len(bird_data)
```




    478




```python
len(cat_data)
```




    509




```python
len(dog_data)
```




    509




```python
len(car_data)
```




    509




```python
len(car_data)
```




    509




```python
len(image_train)
```




    2005




```python
get_images(dog_knn_model.query(image_test[0:1]))['image'].explore()
```


<pre>Starting pairwise querying.</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| Query points | # Pairs | % Complete. | Elapsed Time |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



<pre>| 0            | 1       | 0.196464    | 4.836ms      |</pre>



<pre>| Done         |         | 100         | 30.566ms     |</pre>



<pre>+--------------+---------+-------------+--------------+</pre>



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
  </tbody>
</table>                          </body>                                                          </html>



```python

```
