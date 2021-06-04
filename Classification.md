```python
import turicreate as tc
```


```python
products=tc.SFrame('Amazon_baby.sframe')
```


```python
products
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Flannel Wipes</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">These flannel wipes are<br>OK, but in my opinion ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Wipe Pouch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">it came early and was not<br>disappointed. i love ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Annas Dream Full Quilt<br>with 2 Shams ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Very soft and comfortable<br>and warmer than it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This is a product well<br>worth the purchase.  I ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">All of my kids have cried<br>non-stop when I tried to ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">When the Binky Fairy came<br>to our house, we didn't ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A Tale of Baby's Days<br>with Peter Rabbit ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lovely book, it's bound<br>tightly so you may no ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Perfect for new parents.<br>We were able to keep ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A friend of mine pinned<br>this product on Pinte ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This has been an easy way<br>for my nanny to record ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
    </tr>
</table>
[183531 rows x 3 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
products['word_count']=tc.text_analytics.count_words(products['review'])
```


```python
products.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">word_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Flannel Wipes</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">These flannel wipes are<br>OK, but in my opinion ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 5.0, 'stink':<br>1.0, 'months': 1.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Wipe Pouch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">it came early and was not<br>disappointed. i love ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'love': 1.0,<br>'it': 3.0, 'highly':  ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Annas Dream Full Quilt<br>with 2 Shams ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Very soft and comfortable<br>and warmer than it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'quilt':<br>1.0, 'it': 1.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This is a product well<br>worth the purchase.  I ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'ingenious':<br>1.0, 'love': 2.0, 'is': ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">All of my kids have cried<br>non-stop when I tried to ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'this': 2.0,<br>'all': 2.0, 'love': 1.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">When the Binky Fairy came<br>to our house, we didn't ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'cute': 1.0,<br>'help': 2.0, 'habit': ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A Tale of Baby's Days<br>with Peter Rabbit ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lovely book, it's bound<br>tightly so you may no ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'shop': 1.0, 'be': 1.0,<br>'is': 1.0, 'bound': 1.0, ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Perfect for new parents.<br>We were able to keep ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'all': 1.0,<br>'right': 1.0, 'able': ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A friend of mine pinned<br>this product on Pinte ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 1.0, 'fantastic':<br>1.0, 'help': 1.0, 'gi ...</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This has been an easy way<br>for my nanny to record ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'pre': 1.0, 'all': 1.0,<br>'standarad': 1.0, ...</td>
    </tr>
</table>
[10 rows x 4 columns]<br/>
</div>




```python


```


```python
products['name'].show()
```


<pre>Materializing SArray</pre>



<html>                 <body>                     <iframe style="border:0;margin:0" width="920" height="770" srcdoc='<html lang="en">                         <head>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega/5.4.0/vega.js"></script>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega-embed/4.0.0/vega-embed.js"></script>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega-tooltip/0.5.1/vega-tooltip.min.js"></script>                             <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/vega-tooltip/0.5.1/vega-tooltip.min.css">                             <style>                             .vega-actions > a{                                 color:white;                                 text-decoration: none;                                 font-family: "Arial";                                 cursor:pointer;                                 padding:5px;                                 background:#AAAAAA;                                 border-radius:4px;                                 padding-left:10px;                                 padding-right:10px;                                 margin-right:5px;                             }                             .vega-actions{                                 margin-top:20px;                                 text-align:center                             }                            .vega-actions > a{                                 background:#999999;                            }                             </style>                         </head>                         <body>                             <div id="vis">                             </div>                             <script>                                 var vega_json = "{\"signals\": [{\"on\": [{\"events\": \"mousemove\", \"update\": \"isTuple(group()) ? group() : unit\"}], \"name\": \"unit\", \"value\": {}}, {\"name\": \"pts_store\", \"update\": \"data(\\\"pts_store_store\\\").length &amp;&amp; {count: data(\\\"pts_store_store\\\")[0].values[0]}\"}, {\"on\": [{\"force\": true, \"events\": [{\"source\": \"scope\", \"type\": \"click\"}], \"update\": \"datum &amp;&amp; item().mark.marktype !== &apos;group&apos; ? {unit: \\\"\\\", encodings: [\\\"x\\\"], fields: [\\\"count\\\"], values: [datum[\\\"count\\\"]]} : null\"}], \"name\": \"pts_store_tuple\", \"value\": {}}, {\"on\": [{\"events\": {\"signal\": \"pts_store_tuple\"}, \"update\": \"modify(\\\"pts_store_store\\\", pts_store_tuple, true)\"}], \"name\": \"pts_store_modify\"}], \"autosize\": {\"contains\": \"padding\", \"type\": \"fit\", \"resize\": false}, \"axes\": [{\"scale\": \"x\", \"title\": \"Count\", \"tickCount\": {\"signal\": \"ceil(width/40)\"}, \"zindex\": 1, \"labelOverlap\": true, \"orient\": \"top\"}, {\"domain\": false, \"scale\": \"x\", \"ticks\": false, \"labels\": false, \"tickCount\": {\"signal\": \"ceil(width/40)\"}, \"zindex\": 0, \"grid\": true, \"minExtent\": 0, \"gridScale\": \"y\", \"orient\": \"top\", \"maxExtent\": 0}, {\"zindex\": 1, \"title\": \"Values\", \"scale\": \"y\", \"orient\": \"left\", \"labelOverlap\": true}], \"title\": \"Distribution of Values [string]\", \"config\": {\"style\": {\"cell\": {\"stroke\": \"transparent\"}, \"rect\": {\"stroke\": \"rgba(200, 200, 200, 0.5)\"}, \"group-title\": {\"fontWeight\": \"normal\", \"font\": \"HelveticaNeue, Arial\", \"fontSize\": 29, \"fill\": \"rgba(0,0,0,0.65)\"}}, \"title\": {\"color\": \"rgba(0,0,0,0.847)\", \"fontWeight\": \"normal\", \"font\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"fontSize\": 18, \"offset\": 30}, \"axisY\": {\"minExtent\": 30}, \"range\": {\"heatmap\": {\"scheme\": \"greenblue\"}}, \"legend\": {\"labelFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelColor\": \"rgba(0,0,0,0.847)\", \"titleFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"cornerRadius\": 30, \"titleColor\": \"rgba(0,0,0,0.847)\", \"gradientLength\": 608}, \"axis\": {\"titlePadding\": 20, \"titleColor\": \"rgba(0,0,0,0.847)\", \"titleFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelPadding\": 10, \"labelFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelFontSize\": 12, \"labelColor\": \"rgba(0,0,0,0.847)\", \"gridColor\": \"rgba(204,204,204,1.0)\", \"titleFontSize\": 14, \"tickColor\": \"rgb(136,136,136)\", \"titleFontWeight\": \"normal\"}}, \"scales\": [{\"domain\": {\"field\": \"count\", \"data\": \"data_0\"}, \"name\": \"x\", \"zero\": true, \"range\": [0, {\"signal\": \"width\"}], \"type\": \"linear\", \"nice\": true}, {\"paddingInner\": 0.1, \"domain\": {\"sort\": {\"field\": \"label_idx\", \"order\": \"descending\", \"op\": \"mean\"}, \"field\": \"label\", \"data\": \"data_0\"}, \"name\": \"y\", \"paddingOuter\": 0.05, \"range\": [{\"signal\": \"height\"}, 0], \"type\": \"band\"}], \"style\": \"cell\", \"height\": 550, \"padding\": 8, \"width\": 720, \"marks\": [{\"encode\": {\"hover\": {\"fill\": {\"value\": \"#7EC2F3\"}}, \"update\": {\"x2\": {\"scale\": \"x\", \"value\": 0}, \"x\": {\"field\": \"count\", \"scale\": \"x\"}, \"fill\": {\"value\": \"#108EE9\"}, \"y\": {\"field\": \"label\", \"scale\": \"y\"}, \"height\": {\"band\": true, \"scale\": \"y\"}}}, \"from\": {\"data\": \"data_0\"}, \"style\": [\"bar\"], \"type\": \"rect\", \"name\": \"marks\"}], \"$schema\": \"https://vega.github.io/schema/vega/v4.json\", \"data\": [{\"name\": \"pts_store_store\"}, {\"values\": [{\"count\": 785, \"percentage\": \"0.427721%\", \"label_idx\": 0, \"label\": \"Vulli Sophie the Giraffe Teether\"}, {\"count\": 562, \"percentage\": \"0.306215%\", \"label_idx\": 1, \"label\": \"Simple Wishes Hands-Free Breastpump Bra, Pink, XS-L\"}, {\"count\": 561, \"percentage\": \"0.30567%\", \"label_idx\": 2, \"label\": \"Infant Optics DXR-5 2.4 GHz Digital Video Baby Monitor with Night Vision\"}, {\"count\": 547, \"percentage\": \"0.298042%\", \"label_idx\": 3, \"label\": \"Baby Einstein Take Along Tunes\"}, {\"count\": 520, \"percentage\": \"0.283331%\", \"label_idx\": 4, \"label\": \"Cloud b Twilight Constellation Night Light, Turtle\"}, {\"count\": 489, \"percentage\": \"0.26644%\", \"label_idx\": 5, \"label\": \"Fisher-Price Booster Seat, Blue/Green/Gray\"}, {\"count\": 450, \"percentage\": \"0.24519%\", \"label_idx\": 6, \"label\": \"Fisher-Price Rainforest Jumperoo\"}, {\"count\": 419, \"percentage\": \"0.228299%\", \"label_idx\": 7, \"label\": \"Graco Nautilus 3-in-1 Car Seat, Matrix\"}, {\"count\": 388, \"percentage\": \"0.211408%\", \"label_idx\": 8, \"label\": \"Leachco Snoogle Total Body Pillow\"}, {\"count\": 374, \"percentage\": \"0.20378%\", \"label_idx\": 9, \"label\": \"Regalo Easy Step Walk Thru Gate, White\"}, {\"count\": 333, \"percentage\": \"0.181441%\", \"label_idx\": 10, \"label\": \"Baby Trend Diaper Champ\"}, {\"count\": 286, \"percentage\": \"0.155832%\", \"label_idx\": 11, \"label\": \"Skip Hop Zoo Pack Little Kid Backpack, Dog\"}, {\"count\": 177817, \"percentage\": \"96.8866%\", \"label_idx\": 12, \"label\": \"Other (32407 labels)\"}], \"name\": \"source_2\"}, {\"source\": \"source_2\", \"name\": \"data_0\", \"transform\": [{\"expr\": \"toNumber(datum[\\\"count\\\"])\", \"as\": \"count\", \"type\": \"formula\"}, {\"expr\": \"datum[\\\"count\\\"] !== null &amp;&amp; !isNaN(datum[\\\"count\\\"])\", \"type\": \"filter\"}]}], \"metadata\": {\"bubbleOpts\": {\"fields\": [{\"field\": \"count\"}, {\"field\": \"label\"}, {\"field\": \"percentage\"}], \"showAllFields\": false}}}";                                 var vega_json_parsed = JSON.parse(vega_json);                                 var toolTipOpts = {                                     showAllFields: true                                 };                                 if(vega_json_parsed["metadata"] != null){                                     if(vega_json_parsed["metadata"]["bubbleOpts"] != null){                                         toolTipOpts = vega_json_parsed["metadata"]["bubbleOpts"];                                     };                                 };                                 vegaEmbed("#vis", vega_json_parsed).then(function (result) {                                     vegaTooltip.vega(result.view, toolTipOpts);                                  });                             </script>                         </body>                     </html>' src="demo_iframe_srcdoc.htm">                         <p>Your browser does not support iframes.</p>                     </iframe>                 </body>             </html>



```python
gi=products[products['name']=='Vulli Sophie the Giraffe Teether']
```


```python
len(gi)
```




    785




```python
gi['rating'].show()
```


<pre>Materializing SArray</pre>



<html>                 <body>                     <iframe style="border:0;margin:0" width="920" height="770" srcdoc='<html lang="en">                         <head>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega/5.4.0/vega.js"></script>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega-embed/4.0.0/vega-embed.js"></script>                             <script src="https://cdnjs.cloudflare.com/ajax/libs/vega-tooltip/0.5.1/vega-tooltip.min.js"></script>                             <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/vega-tooltip/0.5.1/vega-tooltip.min.css">                             <style>                             .vega-actions > a{                                 color:white;                                 text-decoration: none;                                 font-family: "Arial";                                 cursor:pointer;                                 padding:5px;                                 background:#AAAAAA;                                 border-radius:4px;                                 padding-left:10px;                                 padding-right:10px;                                 margin-right:5px;                             }                             .vega-actions{                                 margin-top:20px;                                 text-align:center                             }                            .vega-actions > a{                                 background:#999999;                            }                             </style>                         </head>                         <body>                             <div id="vis">                             </div>                             <script>                                 var vega_json = "{\"signals\": [{\"name\": \"bins\", \"update\": \"data(\\\"bins_data\\\")[0]\"}, {\"name\": \"binCount\", \"update\": \"(bins.stop - bins.start) / bins.step\"}, {\"name\": \"nullGap\", \"update\": \"data(\\\"nulls\\\").length ? 10 : 0\"}, {\"name\": \"barStep\", \"update\": \"(width - nullGap) / (1 + binCount)\"}], \"autosize\": {\"contains\": \"padding\", \"type\": \"fit\", \"resize\": false}, \"axes\": [{\"grid\": true, \"scale\": \"xscale\", \"tickMinStep\": 1, \"orient\": \"bottom\", \"title\": \"Values\"}, {\"scale\": \"xscale-null\", \"orient\": \"bottom\"}, {\"scale\": \"yscale\", \"title\": \"Count\", \"tickCount\": 5, \"grid\": true, \"offset\": {\"signal\": \"nullGap ? 5 : 0\"}, \"orient\": \"left\"}], \"description\": \"A simple bar chart with embedded data.\", \"title\": \"Distribution of Values [float]\", \"config\": {\"style\": {\"cell\": {\"stroke\": \"transparent\"}, \"rect\": {\"stroke\": \"rgba(200, 200, 200, 0.5)\"}, \"group-title\": {\"fontWeight\": \"normal\", \"font\": \"HelveticaNeue, Arial\", \"fontSize\": 29, \"fill\": \"rgba(0,0,0,0.65)\"}}, \"title\": {\"color\": \"rgba(0,0,0,0.847)\", \"fontWeight\": \"normal\", \"font\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"fontSize\": 18, \"offset\": 30}, \"axisY\": {\"minExtent\": 30}, \"range\": {\"heatmap\": {\"scheme\": \"greenblue\"}}, \"legend\": {\"labelFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelColor\": \"rgba(0,0,0,0.847)\", \"titleFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"cornerRadius\": 30, \"titleColor\": \"rgba(0,0,0,0.847)\", \"gradientLength\": 608}, \"axis\": {\"titlePadding\": 20, \"titleColor\": \"rgba(0,0,0,0.847)\", \"titleFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelPadding\": 10, \"labelFont\": \"\\\"San Francisco\\\", HelveticaNeue, Arial\", \"labelFontSize\": 12, \"labelColor\": \"rgba(0,0,0,0.847)\", \"gridColor\": \"rgba(204,204,204,1.0)\", \"titleFontSize\": 14, \"tickColor\": \"rgb(136,136,136)\", \"titleFontWeight\": \"normal\"}}, \"scales\": [{\"domain\": {\"fields\": [{\"field\": \"count\", \"data\": \"counts\"}, {\"field\": \"count\", \"data\": \"nulls\"}]}, \"name\": \"yscale\", \"range\": \"height\", \"type\": \"linear\", \"round\": true, \"nice\": true}, {\"domain\": {\"signal\": \"[bins.start, bins.stop]\"}, \"name\": \"xscale\", \"range\": [{\"signal\": \"nullGap ? barStep + nullGap : 0\"}, {\"signal\": \"width\"}], \"type\": \"linear\", \"round\": true, \"bins\": {\"signal\": \"bins\"}}, {\"range\": [{\"signal\": \"nullGap ? 0 : 1\"}, {\"signal\": \"nullGap ? barStep : 0\"}], \"type\": \"band\", \"name\": \"xscale-null\", \"domain\": [{\"signal\": \"nullGap ? null : &apos;&apos;\"}], \"round\": true}], \"style\": \"cell\", \"height\": 550, \"padding\": 8, \"width\": 720, \"marks\": [{\"encode\": {\"hover\": {\"fill\": {\"value\": \"#7EC2F3\"}}, \"update\": {\"x2\": {\"field\": \"right\", \"scale\": \"xscale\"}, \"x\": {\"field\": \"left\", \"scale\": \"xscale\", \"offset\": 1}, \"y2\": {\"scale\": \"yscale\", \"value\": 0}, \"y\": {\"field\": \"count\", \"scale\": \"yscale\"}, \"fill\": {\"value\": \"#108EE9\"}}}, \"from\": {\"data\": \"counts\"}, \"type\": \"rect\"}, {\"encode\": {\"hover\": {\"fill\": {\"value\": \"#7EC2F3\"}}, \"update\": {\"x2\": {\"band\": 1, \"scale\": \"xscale-null\"}, \"x\": {\"scale\": \"xscale-null\", \"value\": null, \"offset\": 1}, \"y2\": {\"scale\": \"yscale\", \"value\": 0}, \"y\": {\"field\": \"count\", \"scale\": \"yscale\"}, \"fill\": {\"value\": \"#108EE9\"}}}, \"from\": {\"data\": \"nulls\"}, \"type\": \"rect\"}], \"$schema\": \"https://vega.github.io/schema/vega/v4.json\", \"data\": [{\"values\": [{\"count\": 56, \"right\": 1.1594, \"left\": 0.9546}, {\"count\": 0, \"right\": 1.3642, \"left\": 1.1594}, {\"count\": 0, \"right\": 1.569, \"left\": 1.3642}, {\"count\": 0, \"right\": 1.7738, \"left\": 1.569}, {\"count\": 0, \"right\": 1.9786, \"left\": 1.7738}, {\"count\": 37, \"right\": 2.1834, \"left\": 1.9786}, {\"count\": 0, \"right\": 2.3882, \"left\": 2.1834}, {\"count\": 0, \"right\": 2.593, \"left\": 2.3882}, {\"count\": 0, \"right\": 2.7978, \"left\": 2.593}, {\"count\": 62, \"right\": 3.0026, \"left\": 2.7978}, {\"count\": 0, \"right\": 3.2074, \"left\": 3.0026}, {\"count\": 0, \"right\": 3.4122, \"left\": 3.2074}, {\"count\": 0, \"right\": 3.617, \"left\": 3.4122}, {\"count\": 0, \"right\": 3.8218, \"left\": 3.617}, {\"count\": 95, \"right\": 4.0266, \"left\": 3.8218}, {\"count\": 0, \"right\": 4.2314, \"left\": 4.0266}, {\"count\": 0, \"right\": 4.4362, \"left\": 4.2314}, {\"count\": 0, \"right\": 4.641, \"left\": 4.4362}, {\"count\": 0, \"right\": 4.8458, \"left\": 4.641}, {\"count\": 535, \"right\": 5.0506, \"left\": 4.8458}, {\"start\": 0.9546, \"step\": 0.2048, \"stop\": 5.0506}], \"name\": \"source_2\"}, {\"source\": \"source_2\", \"name\": \"counts\", \"transform\": [{\"expr\": \"datum[\\\"missing\\\"] !== true &amp;&amp; datum[\\\"count\\\"] != null\", \"type\": \"filter\"}]}, {\"source\": \"source_2\", \"name\": \"nulls\", \"transform\": [{\"expr\": \"datum[\\\"missing\\\"] === true &amp;&amp; datum[\\\"count\\\"] != null\", \"type\": \"filter\"}]}, {\"source\": \"source_2\", \"name\": \"bins_data\", \"transform\": [{\"expr\": \"datum[\\\"start\\\"] != null &amp;&amp; datum[\\\"stop\\\"] != null &amp;&amp; datum[\\\"step\\\"] != null\", \"type\": \"filter\"}]}]}";                                 var vega_json_parsed = JSON.parse(vega_json);                                 var toolTipOpts = {                                     showAllFields: true                                 };                                 if(vega_json_parsed["metadata"] != null){                                     if(vega_json_parsed["metadata"]["bubbleOpts"] != null){                                         toolTipOpts = vega_json_parsed["metadata"]["bubbleOpts"];                                     };                                 };                                 vegaEmbed("#vis", vega_json_parsed).then(function (result) {                                     vegaTooltip.vega(result.view, toolTipOpts);                                  });                             </script>                         </body>                     </html>' src="demo_iframe_srcdoc.htm">                         <p>Your browser does not support iframes.</p>                     </iframe>                 </body>             </html>



```python
products =products[products['rating']!=3]
```


```python
products['sentiment']=products['rating']>=4
```


```python
products.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">word_count</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">sentiment</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Wipe Pouch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">it came early and was not<br>disappointed. i love ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'love': 1.0,<br>'it': 3.0, 'highly':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Annas Dream Full Quilt<br>with 2 Shams ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Very soft and comfortable<br>and warmer than it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'quilt':<br>1.0, 'it': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This is a product well<br>worth the purchase.  I ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'ingenious':<br>1.0, 'love': 2.0, 'is': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">All of my kids have cried<br>non-stop when I tried to ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'this': 2.0,<br>'all': 2.0, 'love': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">When the Binky Fairy came<br>to our house, we didn't ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'cute': 1.0,<br>'help': 2.0, 'habit': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A Tale of Baby's Days<br>with Peter Rabbit ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lovely book, it's bound<br>tightly so you may no ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'shop': 1.0, 'be': 1.0,<br>'is': 1.0, 'bound': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Perfect for new parents.<br>We were able to keep ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'all': 1.0,<br>'right': 1.0, 'able': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A friend of mine pinned<br>this product on Pinte ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 1.0, 'fantastic':<br>1.0, 'help': 1.0, 'gi ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This has been an easy way<br>for my nanny to record ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'pre': 1.0, 'all': 1.0,<br>'standarad': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I love this journal and<br>our nanny uses it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'all': 2.0, 'forget':<br>1.0, 'just': 1.0, 'fo ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>




```python
train_data,test_data = products.random_split(.8,seed=0)
```


```python
sentiment_model=tc.logistic_classifier.create(train_data,target='sentiment',features=['word_count'],validation_set=test_data)
```


<pre>Logistic regression:</pre>



<pre>--------------------------------------------------------</pre>



<pre>Number of examples          : 133448</pre>



<pre>Number of classes           : 2</pre>



<pre>Number of feature columns   : 1</pre>



<pre>Number of unpacked features : 57356</pre>



<pre>Number of coefficients      : 57357</pre>



<pre>Starting L-BFGS</pre>



<pre>--------------------------------------------------------</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| Iteration | Passes   | Step size | Elapsed Time | Training Accuracy | Validation Accuracy |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



<pre>| 0         | 4        | 0.250000  | 0.549812     | 0.841421          | 0.840019            |</pre>



<pre>| 1         | 9        | 3.250000  | 1.308790     | 0.931359          | 0.911362            |</pre>



<pre>| 2         | 11       | 2.669978  | 1.752481     | 0.938650          | 0.916466            |</pre>



<pre>| 3         | 12       | 2.669978  | 2.019142     | 0.927417          | 0.901814            |</pre>



<pre>| 4         | 14       | 1.326072  | 2.420291     | 0.945200          | 0.918088            |</pre>



<pre>| 9         | 20       | 1.326072  | 3.818848     | 0.977654          | 0.917698            |</pre>



<pre>+-----------+----------+-----------+--------------+-------------------+---------------------+</pre>



```python
sent_model.evaluate(test_data,metric='roc_curve')
```




    {'roc_curve': Columns:
     	threshold	float
     	fpr	float
     	tpr	float
     	p	int
     	n	int
     
     Rows: 1001
     
     Data:
     +-----------+----------------+----------------+-------+------+
     | threshold |      fpr       |      tpr       |   p   |  n   |
     +-----------+----------------+----------------+-------+------+
     |    0.0    |      1.0       |      1.0       | 27976 | 5328 |
     |   0.001   | 0.698948948949 | 0.993351444095 | 27976 | 5328 |
     |   0.002   | 0.661974474474 | 0.99220760652  | 27976 | 5328 |
     |   0.003   | 0.638513513514 | 0.990992279096 | 27976 | 5328 |
     |   0.004   | 0.62256006006  | 0.990384615385 | 27976 | 5328 |
     |   0.005   | 0.611298798799 | 0.989848441521 | 27976 | 5328 |
     |   0.006   | 0.600225225225 | 0.989419502431 | 27976 | 5328 |
     |   0.007   | 0.589527027027 | 0.988847583643 | 27976 | 5328 |
     |   0.008   | 0.581644144144 | 0.988382899628 | 27976 | 5328 |
     |   0.009   | 0.574512012012 | 0.98806119531  | 27976 | 5328 |
     +-----------+----------------+----------------+-------+------+
     [1001 rows x 5 columns]
     Note: Only the head of the SFrame is printed.
     You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.}




```python

```


```python
gi['predicted_sentiment']=sent_model.predict(gi,output_type='probability')
```


```python
gi.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">word_count</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">predicted_sentiment</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">He likes chewing on all<br>the parts especially the ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 1.0, 'all': 1.0,<br>'because': 1.0, 'it': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999365536568</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">My son loves this toy and<br>fits great in the diaper ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 1.0, 'right':<br>1.0, 'help': 1.0, 'ju ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999863379169</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">There really should be a<br>large warning on the  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'all': 1.0,<br>'being': 1.0, 'caused': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.254526819749</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">All the moms in my moms'<br>group got Sophie for ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'all': 1.0,<br>'love': 1.0, 'have':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.91656880839</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I was a little skeptical<br>on whether Sophie was ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'all': 1.0,<br>'old': 1.0, 'almost': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.685576820578</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I have been reading about<br>Sophie and was going  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 6.0, 'seven':<br>1.0, 'already': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999999944521</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">My neice loves her sophie<br>and has spent hours ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 4.0, 'drooling':<br>1.0, 'additionally':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.997935118109</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">What a friendly face!<br>And those mesmerizing ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'chew': 1.0,<br>'sweet': 1.0, 'is': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999974500483</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">We got this just for my<br>son to chew on instea ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'chew': 2.0, 'because':<br>1.0, 'just': 2.0, 'fe ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.946014442833</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">My baby seems to like<br>this toy, but I could ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'already':<br>1.0, 'in': 1.0, 'some': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.383011361413</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>




```python
gi=gi.sort('predicted_sentiment',ascending=False)
```


```python
gi.head()
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">word_count</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">predicted_sentiment</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I'll be honest...I bought<br>this toy because all the ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'all': 2.0, 'pops': 1.0,<br>'during': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">As a mother of 16month<br>old twins; I bought ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'cute': 1.0, 'all': 2.0,<br>'just': 1.0, 'able':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sophie, oh Sophie, your<br>time has come. My ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'giggles': 1.0, 'all':<br>1.0, '09': 1.0, 'food': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">We got this little<br>giraffe as a gift from a ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'all': 2.0, 'baby': 1.0,<br>'before': 1.0, 'seems': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">As every mom knows, you<br>always want to give your ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'cute': 1.0, 'all': 1.0,<br>'just': 2.0, 'food':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">My Mom-in-Law bought<br>Sophie for my son whe ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'think': 1.0, 'they':<br>1.0, 'just': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">My 4 month old son is<br>teething, and I've tried ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'cute': 1.0, 'all': 2.0,<br>'food': 1.0, 'when':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999999999999</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Let me just start off by<br>addressing the choking ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'just': 3.0, 'when':<br>3.0, 'still': 1.0, 'h ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999999999994</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I'm not sure why Sophie<br>is such a hit with the ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'peace': 1.0, 'month':<br>1.0, 'bright': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999999999987</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Vulli Sophie the Giraffe<br>Teether ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I admit, I didn't get<br>Sophie the Giraffe at ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'cute': 1.0, 'just':<br>1.0, 'being': 2.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.999999999983</td>
    </tr>
</table>
[10 rows x 5 columns]<br/>
</div>




```python
gi[0]['review']
```




    'I\'ll be honest...I bought this toy because all the hip parents seem to have one too and I wanted to be a part of the "hip parent" crowd. The price-tag was somewhat of a deterent but I prevailed and purchased this teether for my daughter.At first, Lily didn\'t know what to make of of Sophie and showed little interest in the polka-dotted creature. I continued to introduce Lily to Sophie and kept the toy in the carrier so that it was on-hand during transitions. Eventually, Lily discovered what a wonderful experience it was to gnaw on the hooves and ears and these two have never been far apart since.Lily really enjoys gumming all the different parts of Sophie like no other teether we have. The size of the toy is great as it is somewhat substantial and so easy for a little one to grasp and hold onto. Lily really enjoys hearing Sophie squeak and will smile whenever Sophie makes a noise or pops her head up from Mommy\'s lap to say hello.People have stopped and commented on Sophie and to them I have stated, "It\'s worth every penny." I can\'t imagine not having this toy, it has become part and parcel with Lily\'s daily existence. She is soothed by it, loves to chew on it and seems endlessly entertained by it.Someday, Sophie will have earned her retirement. She will relocate to Lily\'s keepsake box. But until then, this little French Giraffe will embark on many adventures alongside my daughter as they explore this big world around them.'




```python
gi[-1]['review']
```




    "This children's toy is nostalgic and very cute. However, there is a distinct rubber smell and a very odd taste, yes I tried it, that my baby did not enjoy. Also, if it is soiled it is extremely difficult to clean as the rubber is a kind of porus material and does not clean well. The final thing is the squeaking device inside which stopped working after the first couple of days. I returned this item feeling I had overpaid for a toy that was defective and did not meet my expectations. Please do not be swayed by the cute packaging and hype surounding it as I was. One more thing, I was given a full refund from Amazon without any problem."




```python
selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
```


```python
def awesome_count(dict) :
    for s, v in dict.items():
        if s=='awesome':
            return v
    return 0
```


```python
products['awesome'] = products['word_count'].apply(awesome_count)
```


```python
products['awesome'].sum()
```




    3892.0




```python
def great_count(dict) :
    for s, v in dict.items():
        if s=='great':
            return v
    return 0
products['great'] = products['word_count'].apply(great_count)
def fant_count(dict) :
    for s, v in dict.items():
        if s=='fantastic':
            return v
    return 0
products['fantastic'] = products['word_count'].apply(fant_count)
def amazing_count(dict) :
    for s, v in dict.items():
        if s=='amazing':
            return v
    return 0
products['amazing'] = products['word_count'].apply(amazing_count)
def love_count(dict) :
    for s, v in dict.items():
        if s=='love':
            return v
    return 0
products['love'] = products['word_count'].apply(love_count)
def horr_count(dict) :
    for s, v in dict.items():
        if s=='horrible':
            return v
    return 0
products['horrible'] = products['word_count'].apply(horr_count)
def bad_count(dict) :
    for s, v in dict.items():
        if s=='bad':
            return v
    return 0
products['bad'] = products['word_count'].apply(bad_count)
def terr_count(dict) :
    for s, v in dict.items():
        if s=='terrible':
            return v
    return 0
products['terrible'] = products['word_count'].apply(terr_count)
def awf_count(dict) :
    for s, v in dict.items():
        if s=='awful':
            return v
    return 0
products['awful'] = products['word_count'].apply(awf_count)
def wow_count(dict) :
    for s, v in dict.items():
        if s=='wow':
            return v
    return 0
products['wow'] = products['word_count'].apply(wow_count)
def hate_count(dict) :
    for s, v in dict.items():
        if s=='hate':
            return v
    return 0
products['hate'] = products['word_count'].apply(hate_count)
```


```python
products
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">review</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rating</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">word_count</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">sentiment</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">awesome</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Planetwise Wipe Pouch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">it came early and was not<br>disappointed. i love ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'love': 1.0,<br>'it': 3.0, 'highly':  ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Annas Dream Full Quilt<br>with 2 Shams ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Very soft and comfortable<br>and warmer than it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'quilt':<br>1.0, 'it': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This is a product well<br>worth the purchase.  I ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 3.0, 'ingenious':<br>1.0, 'love': 2.0, 'is': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">All of my kids have cried<br>non-stop when I tried to ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'this': 2.0,<br>'all': 2.0, 'love': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stop Pacifier Sucking<br>without tears with ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">When the Binky Fairy came<br>to our house, we didn't ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'cute': 1.0,<br>'help': 2.0, 'habit': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A Tale of Baby's Days<br>with Peter Rabbit ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lovely book, it's bound<br>tightly so you may no ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'shop': 1.0, 'be': 1.0,<br>'is': 1.0, 'bound': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Perfect for new parents.<br>We were able to keep ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 2.0, 'all': 1.0,<br>'right': 1.0, 'able': ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">A friend of mine pinned<br>this product on Pinte ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'and': 1.0, 'fantastic':<br>1.0, 'help': 1.0, 'gi ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">This has been an easy way<br>for my nanny to record ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'pre': 1.0, 'all': 1.0,<br>'standarad': 1.0, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Baby Tracker&amp;reg; - Daily<br>Childcare Journal, ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">I love this journal and<br>our nanny uses it ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">{'all': 2.0, 'forget':<br>1.0, 'just': 1.0, 'fo ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
    </tr>
</table>
<table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">great</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">fantastic</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">amazing</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">love</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">bad</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">terrible</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">awful</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">wow</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">hate</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">horrible</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
</table>
[166752 rows x 16 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
train_data,test_data = products.random_split(.8, seed=0)
```


```python
sent_model=tc.logistic_classifier.create(train_data,target='sentiment',features=selected_words,validation_set=test_data)
```


<pre>Logistic regression:</pre>



<pre>--------------------------------------------------------</pre>



<pre>Number of examples          : 133448</pre>



<pre>Number of classes           : 2</pre>



<pre>Number of feature columns   : 11</pre>



<pre>Number of unpacked features : 11</pre>



<pre>Number of coefficients      : 12</pre>



<pre>Starting Newton Method</pre>



<pre>--------------------------------------------------------</pre>



<pre>+-----------+----------+--------------+-------------------+---------------------+</pre>



<pre>| Iteration | Passes   | Elapsed Time | Training Accuracy | Validation Accuracy |</pre>



<pre>+-----------+----------+--------------+-------------------+---------------------+</pre>



<pre>| 1         | 2        | 0.086952     | 0.847401          | 0.845874            |</pre>



<pre>| 2         | 3        | 0.147989     | 0.847514          | 0.846085            |</pre>



<pre>| 3         | 4        | 0.202417     | 0.847626          | 0.846115            |</pre>



<pre>| 4         | 5        | 0.251063     | 0.847708          | 0.846385            |</pre>



<pre>| 5         | 6        | 0.301337     | 0.847708          | 0.846385            |</pre>



<pre>| 6         | 7        | 0.348771     | 0.847708          | 0.846385            |</pre>



<pre>+-----------+----------+--------------+-------------------+---------------------+</pre>



<pre>SUCCESS: Optimal solution found.</pre>



<pre></pre>



```python
sent_model
```




    Class                          : LogisticClassifier
    
    Schema
    ------
    Number of coefficients         : 12
    Number of examples             : 133448
    Number of classes              : 2
    Number of feature columns      : 11
    Number of unpacked features    : 11
    
    Hyperparameters
    ---------------
    L1 penalty                     : 0.0
    L2 penalty                     : 0.01
    
    Training Summary
    ----------------
    Solver                         : newton
    Solver iterations              : 6
    Solver status                  : SUCCESS: Optimal solution found.
    Training time (sec)            : 0.3698
    
    Settings
    --------
    Log-likelihood                 : 52926.808
    
    Highest Positive Coefficients
    -----------------------------
    love                           : 1.3593
    (intercept)                    : 1.3366
    awesome                        : 1.1335
    amazing                        : 1.1001
    fantastic                      : 0.8858
    
    Lowest Negative Coefficients
    ----------------------------
    horrible                       : -2.2513
    terrible                       : -2.2237
    awful                          : -2.0529
    hate                           : -1.3484
    bad                            : -0.9915




```python
diaper_champ_reviews=products[products['name']=='Baby Trend Diaper Champ']
```


```python
sent_model.predict(diaper_champ_reviews[0:1], output_type='probability')
```




    dtype: float
    Rows: 1
    [0.7919288370624453]




```python
mx=products['awesome'].sum()
for s in selected_words:
    if mx > products[s].sum():
        mx=products[s].sum()
        res=s
print(res)
```

    wow



```python
sentiment_model.predict(diaper_champ_reviews[0:1], output_type='probability')
```




    dtype: float
    Rows: 1
    [0.995012293557031]




```python

```
