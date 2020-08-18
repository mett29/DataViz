# An analysis of the digital divide in Italy and Europe

## Overview

In a world that is every day more connected, it is crucial to support this change with suitable infrastructure. Moreover, the last months have forced all the countries to face a tough challenge in terms of technological development (and not only), due to COVID19. Sustaining the digital economy is critical to deal with such extreme scenarios, but also to guarantee a better state of life and to give more opportunities to the people, and thus introducing new lymph in the economy of the country. The digital divide is a phenomenon that affects many nations, with different levels of intensity.

With this project, we aim to carry on a detailed analysis of the current situation in Italy and Europe for what regards the digital society and digital economy aspects. More precisely, the focus will be on Italy itself, performing the first analysis at a regional level, trying to find and show what are the differences among the different regions, and trying to emphasize the unbalances. Then, our magnifying glass will do a step back, to show the differences at a European level. 

### Our datasets
The data we used to perform our analysis came from the ISTAT and Eurostat websites. In particular, we used **I.Stat data warehouse** for Italy, while we used the **Digital Agenda for Europe** for the analysis at a European level.

### Our libraries
Following is a list of the main libraries and tools we used to carry on the analysis:
   - pandas
   - geopandas
   - matplotlib
   - seaborn
   - plotly

## Analysis

### Italy
These sections contain an analysis of the technological innovation in the Italian enterprises. The goal is to understand and show if and where the most recent technologies are changing the way of working of the Italian production sector and how much these technologies are take into consideration.

#### 1. FIRST BLOCK

#### TODO...

---

#### 2. SECOND BLOCK

#### TODO...

---

#### 3. Enterprises and digitization
The survey covers the universe of enterprises with 10 or more persons employed active, according to the classification of economic activities adopted in Italy (Ateco 2002), in the areas of manufacturing, construction, wholesale and detail, hotels, transport, storage and communication, real estate activities, renting, research and development and audiovisual.

***3.1 Enterprises which had acquired goods/services in technological areas in the previous three years (2017)***

The graph shows two interesting aspects:
- there is not a clear difference between the macro-areas of the Italian territory;
- nevertheless, except for the "IT security area", the percentages show an overall low acquisition of the other services.
  
<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_1.png">
</div><br>

***3.2 Enterprises indicating the first five technological areas with greater impact on development in the two-year period (2017)***

This graph is a continuation of the previous one and it can be considered as complementary. Also in this case, the differences between macro-areas are not so marked, but equally there are some interesting aspects:
- the percentages of each area are rationally consistent with the ones in the previous graph;
- the values corresponding to the "online sales" and "social media" for the nord-ovest area are moderately smaller with respect to the others. This could indicate that these two aspects have already been considered by the nord-ovest enterprises in the past and thus they did not have a great impact in the years of the survey;
- critically, the percentages corresponding to the "do not know how to respond" are fairly high.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_2.png">
</div><br>

***3.3 The main digitization factors considered important by enterprises (2018)***

This graph follows the same line of the previous one, but with a focus on the so-called "digitization factors", namely those factors deemed important to sustain the development of the productive sector. 

- firstly, it's interesting to note that there are two clear winners in this analysis: the "ultra-broadband" and the "funding and tax incentives" factors. The latter, in particular, reaches a percentage of about 50%, especially in the south of Italy;
- also in this case, the percentages corresponding to the "do not know how to respond" value are fairly high.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_3.png">
</div><br>

#### 4. Enterprises and innovation

The Community Innovation Survey (CIS) was designed to complement the traditional indicators, such as R&D expenditure and patent statistics, in the measurement of innovation. In particular, the CIS provides a sound statistical basis for better understanding the innovation process and its effects on the economy and for monitoring and evaluating the innovation policies of the Member States and the European Union.

***4.1 Enterprises with innovation activities (2016)***

The two choropleth maps below show the number of enterprises with innovation activities by region and the percentage on the total number of enterprises by region respectively. They are complementary visualizations, since even if the first one shows a sharp distinction between the regions, where north and Lombardia in particular are dominant, the second one reveals that if we consider the percentage on the total number of enterprises, the situation is notable uniform. Nevertheless, the difference in quantitative terms is still meaningful.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_4.svg" width=850px height=550px>
</div><br>

***4.2 Innovation expenditure by region (2016)***

The last consideration in the previous section is supported by this other graph, in which it is shown how much each region spends in innovation (data of year 2016). Indeed, it essentially traces the graph showing the number of enterprises with innovation activities, with the exception of the Lazio region.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_5.svg" width=450px height=550px>
</div><br>

***4.3 Product/process innovation activities and organisation/marketing innovations (2016)***

This other graph ends the analysis on the innovation aspect in Italian enterprises. It takes into consideration the number of product and process innovation activities, thus at a finer-grained level with respect to the previous ones. However, the data are aggregated by macro-areas, as shown in the visualization. Again, it clearly demonstrates the presence of a relatively big gap between northern and southern regions.  

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_6.svg" width=550px height=500px>
</div><br>

#### 5. ICT of the enterprises

In this section we focused on some specific aspects that are somehow relevant to understand the technological level present in the italian enterprises. 

***5.1 Percentage of enterprises with a website or a homepage (2019)***

As one can see, the percentages are all over the 50%, but there is a clear distinction between northern and center/southern regions.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_7.svg" width=550px height=500px>
</div><br>

***5.2 Enterprises connected via fixed broadband - Download speed (2019)***

Visibly, the download speeds in the three different classes are not so different among the different regions, with an interesting exception of the Calabria region. It is also worth to mention that from the graph it can be seen that on average about 50% of the enterprises have a fixed broadband connection with a download speed below 30 Mb/s, showing a clear infrastructural problem.

<br><div style="text-align:center">
   <img src="../assets/img/3rd_block/fig_8.svg" width=900px height=500px>
</div><br>