---
layout: archive
title: "Data, Code & Research Software"
permalink: /data_code/
author_profile: false
---

This page provides selected interactive tools, code, models, and data products developed through my research.

---

## Interactive Tools

### 🌐 GSM3 Viewer — Global Soil Moisture Explorer

[Interactive App](https://jayhydro.github.io/gsm3-viewer/) | [Dataset](https://doi.org/10.5281/zenodo.7344484) | [Paper](https://doi.org/10.5194/gmd-16-1553-2023)

- Interactive visualization of daily global soil moisture predictions at 9 km resolution.
- Supports spatial exploration, temporal animation, and data access.
- Based on the GSM3 global multitask soil moisture dataset.

---

## Code & Models

### 🌍 Geospatial Foundation Embeddings for Hydrologic Prediction

[Paper](https://doi.org/10.1029/2026GL122814) | [Code & Data](https://doi.org/10.5281/zenodo.19157884)

- Evaluates geospatial foundation model embeddings as transferable catchment descriptors for rainfall–runoff prediction.
- Uses representations from AlphaEarth and StefaLand across U.S. and global catchments.
- Demonstrates the value of learned embeddings for spatial transfer and prediction in ungauged basins.

---

### 🔄 Transformer Models for Hydrologic Prediction

[Code](https://doi.org/10.5281/zenodo.13664154) | [Paper](https://doi.org/10.1016/j.jhydrol.2024.131389)

- Benchmarks Transformer architectures against LSTM for large-sample rainfall–runoff prediction.
- Shows that architectural modifications substantially improve Transformer performance relative to the vanilla architecture.
- Provides a benchmark for exploring non-recurrent and pretrained architectures in hydrologic prediction.

---

### 🛰️ Multiscale Deep Learning for Soil Moisture

[Code](https://zenodo.org/records/6363140) | [Paper](https://doi.org/10.1029/2021GL096847)

- Multiscale deep learning framework that jointly learns from satellite and in situ soil moisture observations.
- Produces daily soil moisture predictions at 9 km resolution across the conterminous United States.
- Provides a general framework for learning from observations available at different spatial scales.

---

## Data Sets

### 🌐 Global Soil Moisture from a Multitask Model (GSM3)

[Dataset](https://doi.org/10.5281/zenodo.7344484) | [Interactive Viewer](https://jayhydro.github.io/gsm3-viewer/) | [Paper](https://doi.org/10.5194/gmd-16-1553-2023)

GSM3 is a global daily soil moisture dataset generated using a multitask deep learning model trained jointly with satellite and in situ observations.

| Field | Value |
|-------|-------|
| **Short name** | GSM3 |
| **Long name** | Global Soil Moisture Dataset From a Multitask Model |
| **Version** | 1.0 |
| **Format** | GeoTIFF |
| **Spatial coverage** | Global |
| **Temporal coverage** | 2015-01-01 to 2020-12-31 |
| **Spatial resolution** | 9 km |
| **Temporal resolution** | Daily |
| **CRS** | EPSG:6933 – WGS 84 / NSIDC EASE-Grid 2.0 Global |