# Preparing the dataset

The steps followed after the dataset was cleaned of unwanted characters was as follows:

1. Some specific time-expresiones were normalized on `pre_tag.py`, before the Time Tagging.
2. **Time labeling:** to dispose of all the time-context information. Using the SUTime module of Stanford CoreNLP. Module available on the `labeling` java project enclosed.
3. Once the taggs were identified, the temporal-information were replaced with **Temporal Rules** inspired by the study made by Abad, et. al. (2017)
   > Abad, Z. S. H., Karras, O., Ghazi, P., Glinz, M., Ruhe, G., & Schneider, K. (2017). _What Works Better? A Study of Classifying Requirements_. 2017 IEEE 25th International Requirements Engineering Conference (RE), 496–501. https://doi.org/10.1109/RE.2017.36 
4. Once the text was normalized, the Named-Entity-Recognition module from the StanfordCoreNLP was used to add the entity taggs. The words associated to the following labels were removed:
   1. NATIONALITY
   2. NUMBER
   3. ORGANIZATION
   4. COUNTRY
   5. TIME
   6. URL
5. Finally, with the Part-of-Speech module, all the nouns on the requirements were highlighted and uploaded to `doccano`. Based on the subjects, the reviewer manually selected the words associated to the system and the users.
6. With the custom `pos` tags, the domain-information such as the system name or the stakeholders where masked. This way, the requirements weren't associated to an specific project. Therefore, limiting the domain-specific vocabulary.