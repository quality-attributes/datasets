# Databases

Official data sources for the Quality Attributes project to train, test and validate if `Non-Functional Requirements` related to Quality Attributes can be found on GitHub Issues reports.

## Training Set

On December 14th, 2019 the site http://ctp.di.fct.unl.pt/RE2017/pages/submission/data_papers/ was visited to get the PROMISE dataset, included as part of a data challenge.

> Sayyad Shirabad, J. and Menzies, T.J. (2005) The PROMISE Repository of Software Engineering Databases. School of Information Technology and Engineering, University of Ottawa, Canada. Available: http://promise.site.uottawa.ca/SERepository

The non-functional requirements' labels in this dataset (involving 15 different projects) are distributed as follows:

| Class                | Quantity | Percentage |
| -------------------- | -------: | ---------: |
| Funcional (F)        |      255 |     40.80% |
| Availability (A)     |       21 |      3.36% |
| Fault Tolerance (FT) |       10 |      1.60% |
| Legal (L)            |       13 |      2.08% |
| Look & Feel (LF)     |       38 |      6.08% |
| Maintainability (MN) |       17 |      2.72% |
| Operational (O)      |       62 |      9.92% |
| Performance (PE)     |       54 |      8.64% |
| Portability (PO)     |        1 |      0.16% |
| Scalability (SC)     |       21 |      3.36% |
| Security (SE)        |       66 |     10.56% |
| Usability (US)       |       67 |     10.72% |
| **Total**            |  **625** |   **100%** |

For the purposes of this study, only a subset of this dataset was considered, as part of the quality attributes categories and due to imbalanced classes:

| Class                | Quantity | Percentage |
| -------------------- | -------: | ---------: |
| Availability (A)     |       21 |      8.20% |
| Fault Tolerance (FT) |       10 |      3.91% |
| Maintainability (MN) |       17 |      6.64% |
| Performance (PE)     |       54 |     21.09% |
| Scalability (SC)     |       21 |      8.21% |
| Security (SE)        |       66 |     25.78% |
| Usability (US)       |       67 |     26.17% |
| **Total**            |  **256** |   **100%** |

## Test Set

Based upon the study:

> Slankas, J. and Williams, L. (2013) Automated extraction of non-functional requirements in available documentation. 1st International Workshop on Natural Language Analysis in Software Engineering (NaturaLiSE), San Francisco, CA, 2013, pp. 9-16.
> doi: 10.1109/NAturaLiSE.2013.6611715

This project tests the classification models using a subset of the examples categorized by the [NFRLocator project](https://github.com/RealsearchGroup/NFRLocator), described in the paper. Only the datasets with syntactically structured requirements were collected, which involves the following projects:
- CCHIT Certified 2011 Ambulatory EHR Criteria 20110517 - parsed.json
- LACountyEHR_Requirements - parsed.json

## Validation Set

According to [the State of the Octoverse](https://octoverse.github.com) in 2019, the most contributed open source project at GitHub were as follows:

| Place | Repository                                                                                          | Contributors |
| :---: | --------------------------------------------------------------------------------------------------- | -----------: |
|  01   | [microsoft/vscode](https://github.com/microsoft/vscode)                                             |        19.1k |
|  02   | [MicrosoftDocs/azure-docs](https://github.com/MicrosoftDocs/azure-docs)                             |          14k |
|  03   | [flutter/flutter](https://github.com/flutter/flutter)                                               |          13k |
|  04   | [firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions) |        11.6k |
|  05   | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)                                   |         9.9k |
|  06   | [facebook/react-native](https://github.com/facebook/react-native)                                   |         9.1k |
|  07   | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)                                   |         6.9k |
|  08   | [DefinitelyTyped/DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)               |         6.9k |
|  09   | [ansible/ansible](https://github.com/ansible/ansible)                                               |         6.8k |
|  10   | [home-assistant/home-assistant](https://github.com/home-assistant/home-assistant)                   |         6.3k |

The repositories selected describe different software systems, excluding documentations and projects with the same scope (i.e. flutter and react-native. Data collected using [quality-attributes/issue-collector](https://github.com/quality-attributes/issue-collector) for the following repositories:

1. [microsoft/vscode](https://github.com/microsoft/vscode)
2. [flutter/flutter](https://github.com/flutter/flutter)
3. [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)
4. [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)
5. [ansible/ansible](https://github.com/ansible/ansible)

**Note:** Only the latest 100 issues (as of `02/20/2020`) for each repository were collected, due to GitHub's API v4 limitations