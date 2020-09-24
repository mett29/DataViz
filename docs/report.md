# An analysis of the digital divide in Italy and Europe

## Overview

In a world that is every day more connected, it is crucial to support this change with suitable infrastructure. Moreover, the last months have forced all the countries to face a tough challenge in terms of technological development (and not only that), due to COVID19. Sustaining the digital economy is critical to deal with such extreme scenarios, but also to guarantee a better state of life and to give more opportunities to the people, and thus introducing new lymph in the economy of the country. The digital divide is a phenomenon that affects many nations, with different levels of intensity.

With this project, we aim to carry on a detailed analysis of the current situation in Italy and Europe for what regards the digital society and digital economy aspects. More precisely, the focus will be on Italy itself, performing the first analysis at a regional level, trying to find and show what are the differences among the different regions, and trying to emphasize the imbalances. Then, our magnifying glass will do a step back, to show the differences at a European level. 

### Our datasets
The data we used to perform our analysis came from the ISTAT and Eurostat websites. In particular, we used **I.Stat data warehouse** for Italy, while we used the **Digital Agenda for Europe** for the analysis at a European level.

### Our libraries
Outlined below is a list of the main libraries and tools we used to carry out the analysis:
   - pandas
   - geopandas
   - matplotlib
   - seaborn
   - plotly
   - dash

## Analysis

### Italy

#### 1. Household internet access and sentiment
This section focuses on the disparities in Italian people's approach towards technology, internet and e-commerce, capturing the findings of the most recent survey (2019), as well as the evolution of some parameters across the years.
The survey provides information on the citizens' habits and the problems they face in every day life. The thematic areas are on different social aspects, allowing to assess the quality of individual life: here we specifically focus on the citizens' internet usage.

***1.1 Households with internet access at home by region (2019)***

The graph shows the different distribution in household internet access thoroghout the regions: it highlights how the southern regions of the country are (mostly) below average, while the center-northern regions are above average, albeit the difference is not extremely pronounced. The bar chart and the choropleth map provide a look at this data from different perspectives.

<br><div style="text-align:center">
   <img src="../assets/img/1st_block/fig_1_1.svg" width=59%>
   <img src="../assets/img/1st_block/fig_1_2.svg" width=40%>
</div><br>

***1.2 Households with internet access at home by age group (2019)***

Together with the geographic imbalance, the age gap is especially pronounced in Italy: it is a country with an older population than most, and this is reflected in many of the indicators analyzed in this report.

The following chart shows the percentage of households with and without an internet connection, by age group: the most noticeable discrepancy lies in the households with over-65 members, since most (64.7%) of those don't even have an internet connection.

<br><div style="text-align:center">
   <img src="../assets/img/1st_block/fig_1_3.svg">
</div><br>

***1.3 Households without internet access at home by age group and reason (2019)***

The next chart analyzes the previous data in more detail, looking at the same age groups and breaking down the reasons for not having internet at home. In general, the predominant reasons are "lack of skills", and finding the internet "not useful, not interesting", which highlights a widespread disinterest and a  noticeable cultural hindrance to the modernization of the country. These findings are especially evident in the over-65 age group.

<br><div style="text-align:center">
   <img src="../assets/img/1st_block/fig_1_4.svg">
</div><br>

#### 2. Household internet usage and services

***2.1 Internet usage by age over time (2001-2019)***

TODO

<br><div style="text-align:center">
   <img src="../assets/img/1st_block/fig_2_1.svg">
</div><br>

***2.2 Interaction with the public authorities***

TODO

***2.3 Frequency in online purchases by region (2019)***

TODO

<br><div style="text-align:center">
   <img src="../assets/img/1st_block/fig_2_2.svg">
</div><br>

#### 3. E-commerce

***3.1 TODO***

TODO


---

#### E-invoicing

These sections contain an analysis of the technological innovation in the Italian enterprises. The goal is to understand and show if and where the most recent technologies are changing the way of working of the Italian production sector and how much these technologies are take into consideration.

The survey covers the universe of enterprises with 10 or more persons  employed active, according to the classification of economic activities  adopted in Italy (Ateco 2002), in the areas of manufacturing (D),  construction (F), wholesale and detail (G), hotels (H), transport,  storage and communication (I), real estate activities, renting, research and development (K) and audiovisual (O).

The object of the survey are the equipments of ICT enterprises and the  measurement of e-commerce. The technique chosen is the investigation of a postal self-completion questionnaire.

The sampling design used for the survey is stratified random type.  Businesses universe were divided into homogeneous layers for level of  economic activity, geographical area and number of employees. 

The graph represent the percentage of the enterprises that use different types of invoicing.  In particular, the specific indicators represent:

- Enterprises sending invoices to other enterprises or government with paper sending (**Paper sending**)
- Enterprises sending invoices to other enterprises or government with sending of electronic Invoice suitable for automated processing (**eInvoice suitable**)
- Enterprises sending invoices to other enterprises or government using electronic invoice not suitable for automated processing (**Electronic not suitable**)

##### Analysis of the results

- It emerges that the results are very similar throughout Italy, no relevant difference arise. 

- Paper invoices are still the preferred/most supported medium for most companies.

<img src="../assets/img/2nd_block/fig_1.png">

#### Big data analysis (2018)

In this section we analyze the big data analysis aspects of the Italian enterprises. Big data analytics examines large amounts of data to uncover hidden patterns, correlations and other insights. 

**Source type of analyzed data**

The y-axis represent the percentages of the data type analyzed, from the total collected data. The percentages are overall low, and anomalous value can be seen in:

- Analysis of data from the social media source, higher in center than in every other territories;
-  The analysis of the data  from smart devices sensors show the usual descending trend from north to south

<img src="../assets/img/2nd_block/fig_4.png">

**Division by percentages of enterprises analysis type**

Data analysis in general has a low percentage, which does not exceed 8% of companies in both the north and south. It is a result that can be expected as most companies are not interested in this type of analysis, but only those strongly connected to the world of ICT benefit from it.

Therefore, among these companies, which ones carry out analyzes through external providers and which ones directly in the company?

- The preferred way is mostly the analysis through internal work of the company
- A lower part, on the other hand, prefers an analysis via external providers, which provide all the searches already done
- Little difference between north and south, the percentages in scale remain very low in any case

<img src="../assets/img/2nd_block/fig_5.svg">

#### Cloud Computing (2018)

Another indicator of technological development can be found in the data and statistics of the use of services in the 'cloud', with operations not carried out directly on the company's physical machine.

**Level of cloud services**

The level of service here indicates the level of the machines/service bought by the enterprise. The higher is the level, the more efficient and more curated is the service (and likely, higher is the price). 

We can see how the descending trend (thought with small gaps) is maintained also in this indicator. The relative proportion between the 3 levels in a single area are more or less the same for every area, while the general tendency to invest in any kind of cloud service is higher in north than in south.

<img src="report/fig_3.png">

**Type of cloud services**

The representation below shows, speaking of type of service, what companies are interested in. The email and storage services (as expected) are the most in demand, while pure computational power is given little consideration in both the north and south.

Among all, the service that remains most stable in the differences between the territories is the cloud hosting of databases, fundamental for any company dealing with ICT.

The trend remains downward between the northern and southern territories.

<img src="../assets/img/2nd_block/fig_2.png">

#### Skills and training in ICT (2019)

In this section we want to highlight  the difference between territories of skills and the type of employees with technological skills among the various companies.

**Investment in ICT skilled employers by the enterprise** and **ICT functions performed by internal/external suppliers**

Both the maps are complementary graphs, and we try to show the difference between IT work done inside the company compared to that done outside.

You immediately notice the big difference in favor of external work: companies prefer to turn to other consulting companies for this type of operation. This result shows the many IT specialist companies to be fundamental both north and south for carrying out these jobs, which normal companies cannot afford to do internally.

The "recruited personnel for ICT" represent the percentages of enterprises that have recruited/tried to recruit personnel for jobs requiring ICT specialist skills in previous year.

Although the number of companies employing ICT specialists is already higher in the north, it remains even higher than in the other territories also for the personnel hired in the last year and the willingness to invest in strengthening the skills of employees. This result highlights how the north invests more resources in recruiting people with IT skills despite already having a higher number of employees with these skills.

<img src="../assets/img/2nd_block/fig_6.svg">

<img src="../assets/img/2nd_block/fig_7.png">

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



### Europe

#### TODO

#### Digital Economy and Society Index (DESI)

The Digital Economy and Society Index (DESI) is a composite index that summarises relevant indicators on Europe’s digital performance and tracks the evolution of EU Member States in digital competitiveness.

The majority of DESI indicators come from Eurostat, the statistical office of the European Union. Some broadband indicators are collected by the Commission services from the Member States through the Communications Committee. Other indicators, such as some e-government and broadband indicators, are based on data derived from studies prepared for the Commission.


The DESI is composed of five principal policy areas:

1. Connectivity  
   Fixed broadband take-up, fixed broadband coverage, mobile broadband and broadband prices
2. Human capital  
   Internet user skills and advanced skills
3. Use of internet  
   Citizens' use of internet services and online transactions
4. Integration of digital technology  
   Business digitisation and e-commerce
5. Digital public services  
   e-Government

The data is proposed here in two interactive visualizations.

##### Choropleth map
The interactive map allows to choose one of the 5 Dimensions which make up the DESI and to select on a slider the year to visualize the score for said indicator.

The scores go from 0 to 100 and are obtained by weighting a specific set of indicators. The can be visualized by hovering over each country.

TODO

[//]: # "<iframe src="https://europe-dash.herokuapp.com/" width=1200 height=1200>"

##### Bar chart
TODO