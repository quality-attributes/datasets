# Preparing the dataset

The steps followed after the dataset was cleaned of unwanted characters was as follows:

1. Some specific time-expresiones were normalized on `pre_tag.py`, before the Time Tagging
2. **Time labeling:** to dispose of all the time-context information. Using the SUTime module of Stanford CoreNLP. Module available on the `labeling` java project enclosed.
3. Once the taggs were identified, the temporal-information were replaced with **Temporal Rules** inspired by the study made by Abad, et. al. (2017)
   > Abad, Z. S. H., Karras, O., Ghazi, P., Glinz, M., Ruhe, G., & Schneider, K. (2017). _What Works Better? A Study of Classifying Requirements_. 2017 IEEE 25th International Requirements Engineering Conference (RE), 496–501. https://doi.org/10.1109/RE.2017.36 
4. 