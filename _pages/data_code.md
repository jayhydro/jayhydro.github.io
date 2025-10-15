---
layout: archive
permalink: /data_code/
author_profile: false
---

<!-- ====== MODELS / CODE ====== -->
## Code & Models

### 🔥 Probing the Limit of Hydrologic Predictability with the **Transformer**
[Code](https://doi.org/10.5281/zenodo.13664154) || [Paper](https://doi.org/10.1016/j.jhydrol.2024.131389)
- **First rigorous benchmark** comparing Transformers against LSTM on the CAMELS streamflow data set.  
- Shows vanilla Transformers lag on high-flow metrics, while the modified variant **matches or slightly exceeds** LSTM in KGE and other scores—hinting we are near the data-set predictability limit.  
- Take-home: non-recurrent designs are promising for large-scale, knowledge-stored hydrologic models.  
<details><summary>Full abstract</summary>For a number of years since their introduction to hydrology, recurrent neural networks like long short-term memory (LSTM) networks have proven remarkably difficult to surpass in terms of daily hydrograph metrics on community-shared benchmarks. Outside of hydrology, Transformers have now become the model of choice for sequential prediction tasks, making it a curious architecture to investigate for application to hydrology. Here, we first show that a vanilla (basic) Transformer architecture is not competitive against LSTM on the widely benchmarked CAMELS streamflow dataset, and lagged especially prominently for the high-flow metrics, perhaps due to the lack of memory mechanisms. However, a recurrence-free variant of the Transformer model obtained mixed comparisons with LSTM, producing very slightly higher Kling-Gupta efficiency coefficients (KGE), along with other metrics. The lack of advantages for the vanilla Transformer network is linked to the nature of hydrologic processes. Additionally, similar to LSTM, the Transformer can also merge multiple meteorological forcing datasets to improve model performance. Therefore, the modified Transformer represents a rare competitive architecture to LSTM in rigorous benchmarks. Valuable lessons were learned: (1) the basic Transformer architecture is not suitable for hydrologic modeling; (2) the recurrence-free modification is beneficial, so future work should continue to test such modifications; and (3) the performance of state-of-the-art models may be close to the prediction limits of the dataset. As a non-recurrent model, the Transformer may bear scale advantages for learning from bigger datasets and storing knowledge. This work lays the groundwork for future explorations into pretraining models, serving as a foundational benchmark that underscores the potential benefits in hydrology.</details>

### 🛰️ A Multiscale Deep Learning Model for Soil Moisture
[Code](https://zenodo.org/records/6363140) || [Paper](https://doi.org/10.1029/2021GL096847)
- Unified multiscale scheme jointly learns from satellite and in-situ data to predict **daily 9 km 5 cm-depth soil moisture**.  
- Spatial cross-validation over CONUS sites: median corr = 0.901, RMSE = 0.034 m³/m³—outperforming SMAP 9 km, in-situ-only DL, and land-surface models.  
- Generic blueprint for other geoscience problems that span multiple spatial scales.  
<details><summary>Full abstract</summary>Deep learning (DL) models trained on hydrologic observations can perform extraordinarily well, but they can inherit deficiencies of the training data, such as limited coverage of in situ data or low resolution/accuracy of satellite data. Here we propose a novel multiscale DL scheme learning simultaneously from satellite and in situ data to predict 9 km daily soil moisture (5 cm depth). Based on spatial cross-validation over sites in the conterminous United States, the multiscale scheme obtained a median correlation of 0.901 and root-mean-square error of 0.034 m3/m3. It outperformed the Soil Moisture Active Passive satellite mission's 9 km product, DL models trained on in situ data alone, and land surface models. Our 9 km product showed better accuracy than previous 1 km satellite downscaling products, highlighting limited impacts of improving resolution. Not only is our product useful for planning against floods, droughts, and pests, our scheme is generically applicable to geoscientific domains with data on multiple scales, breaking the confines of individual data sets.</details>

---

<!-- ====== DATA SETS ====== -->
## Data Sets

### 🌐 Global Soil Moisture from a Multitask Model (**GSM3**)
[Dataset](https://doi.org/10.5281/zenodo.7344484) || [Paper](https://doi.org/10.5194/gmd-16-1553-2023)
- **Global multitask LSTM product**; median corr = 0.792 in random hold-out and continental hold-out tests.  
- Performs surprisingly well in Africa & Australia even when those continents are excluded from training; integrated into an operational advisory platform serving **13 M African farmers**.

| Field | Value |
|-------|-------|
| **Short name** | GSM3 |
| **Long name** | Global Soil Moisture Dataset From a Multitask Model |
| **Version** | 1.0 |
| **Format** | GeoTIFF |
| **Spatial coverage** | Global |
| **Temporal coverage** | 2015-01-01 → 2020-12-31 |
| **Resolution** | 9 km (spatial) • daily (temporal) |
| **CRS** | EPSG:6933 – WGS 84 / NSIDC EASE-Grid 2.0 Global |
| **File size** | ≈ 10.3 MB per tile |

<details><summary>Full abstract</summary>Climate change threatens our ability to grow food for an ever-increasing population. There is a need for high-quality soil moisture predictions in under-monitored regions like Africa. However, it is unclear if soil moisture processes are globally similar enough to allow our models trained on available in situ data to maintain accuracy in unmonitored regions. We present a multitask long short-term memory (LSTM) model that learns simultaneously from global satellite-based data and in situ soil moisture data. This model is evaluated in both random spatial holdout mode and continental holdout mode (trained on some continents, tested on a different one). The model compared favorably to current land surface models, satellite products, and a candidate machine learning model, reaching a global median correlation of 0.792 for the random spatial holdout test. It behaved surprisingly well in Africa and Australia, showing high correlation even when we excluded their sites from the training set, but it performed relatively poorly in Alaska where rapid changes are occurring. In all but one continent (Asia), the multitask model in the worst-case scenario test performed better than the soil moisture active passive (SMAP) 9 km product. Factorial analysis has shown that the LSTM model's accuracy varies with terrain aspect, resulting in lower performance for dry and south-facing slopes or wet and north-facing slopes. This knowledge helps us apply the model while understanding its limitations. This model is being integrated into an operational agricultural assistance application which currently provides information to 13 million African farmers.</details>
