import json
import pandas as pd
from bs4 import BeautifulSoup
import re

template = [{
    "repository": "ansible",
    "tags": [
        "<h5>SUMMARY</h5>",
        "<h5>ISSUE TYPE</h5>",
        "<h5>COMPONENT NAME</h5>",
        "<h5>ANSIBLE VERSION</h5>",
        "<h5>CONFIGURATION</h5>",
        "<h5>OS / ENVIRONMENT</h5>",
        "<h5>STEPS TO REPRODUCE</h5>",
        "<h5>EXPECTED RESULTS</h5>",
        "<h5>ACTUAL RESULTS</h5>",
        "<h5>ADDITIONAL INFORMATION</h5>"
    ],
    "list_items": []
},
    {
    "repository": "flutter",
    "tags": [
        "<h2>Steps to Reproduce</h2>",
        "<h2>Logs</h2>",
        "<h2>Use case</h2>",
        "<h2>Proposal</h2>",
        "<h2>Details</h2>",
        "<strong>Target Platform:</strong>",
        "<strong>Target OS version/browser:</strong>",
        "<strong>Devices:</strong>",
    ],
    "list_items": []
},
    {
    "repository": "kubernetes",
    "tags": [
        "<b>What happened</b>:",
        "<b>What you expected to happen</b>:",
        "<b>How to reproduce it (as minimally and precisely as possible)</b>:",
        "<b>Anything else we need to know?</b>:",
        "<b>Environment</b>:",
        "<b>What would you like to be added</b>:",
        "<b>Why is this needed</b>:",
        "<b>Which jobs are failing</b>:",
        "<b>Which test(s) are failing</b>:",
        "<b>Since when has it been failing</b>:",
        "<b>Testgrid link</b>:",
        "<b>Reason for failure</b>:",
        "<b>Anything else we need to know</b>:",
        "<b>Which jobs are flaking</b>:",
        "<b>Which test(s) are flaking</b>:",
    ],
    "list_items": [
        "Kubernetes version (use `kubectl version`):",
        "Cloud provider or hardware configuration:",
        "OS (e.g: `cat /etc/os-release`):",
        "Kernel (e.g. `uname -a`):",
        "Install tools:",
        "Network plugin and version (if this is a network-related bug):",
        "Others:",
        "links to go.k8s.io/triage appreciated",
        "links to specific failures in spyglass appreciated",
    ]
}, {
    "repository": "tensorflow",
    "tags": [
        "<p>You can collect some of this information using our environment capture script:</p>\n<p><a href=\"https://github.com/tensorflow/tensorflow/tree/master/tools/tf_env_collect.sh\">https://github.com/tensorflow/tensorflow/tree/master/tools/tf_env_collect.sh</a></p>",
        "<strong>Describe the current behavior</strong>",
        "<strong>Describe the expected behavior</strong>",
        "<strong>Standalone code to reproduce the issue</strong>",
        "<strong>Other info / logs</strong>",
        "<strong>Describe the problem</strong>",
        "<strong>Provide the exact sequence of commands / steps that you executed before running into the problem</strong>",
        "<p>Include any logs or source code that would be helpful to diagnose the problem. If including tracebacks, please include the full traceback. Large logs and files should be attached.</p>",

        "<p>Thank you for submitting a TensorFlow documentation issue. Per our GitHub\npolicy, we only address code/doc bugs, performance issues, feature requests, and\nbuild/installation issues on GitHub.</p>",
        "<p>The TensorFlow docs are open source! To get involved, read the documentation\ncontributor guide: https://www.tensorflow.org/community/contribute/docs</p>",
        "<h2>URL(s) with the issue:</h2>",
        "<p>Please provide a link to the documentation entry, for example:\n<a href='https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/MyMethod'>https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/MyMethod</a></p>"
        "<h2>Description of issue (what needs changing):</h2>",
        "<h3>Clear description</h3>",
        "<p>For example, why should someone use this method? How is it useful?</p>",
        "<h3>Correct links</h3>",
        "<p>Is the link to the source code correct?</p>",
        "<h3>Parameters defined</h3>",
        "<p>Are all parameters defined and formatted correctly?</p>",
        "<h3>Returns defined</h3>",
        "<p>Are return values defined?</p>",
        "<h3>Raises listed and defined</h3>",
        "<p>Are the errors defined? For example,</p>",
        "<a href='https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_file#raises'>https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/feature_column/categorical_column_with_vocabulary_file#raises</a>",
        "<h3>Usage example</h3>",
        "<p>Is there a usage example?</p>",
        "<p>See the API guide: <a href='https://www.tensorflow.org/community/contribute/docs_ref'>https://www.tensorflow.org/community/contribute/docs_ref</a>\non how to write testable usage examples.</p>",
        "<h3>Request visuals, if applicable</h3>",
        "<p>Are there currently visuals? If not, will it clarify the content?</p>",
        "<h3>Submit a pull request?</h3>",
        "<p>Are you planning to also submit a pull request to fix the issue? See the docs"
        "<p>docs API guide: <a href='https://www.tensorflow.org/community/contribute/docs_ref'>https://www.tensorflow.org/community/contribute/docs_ref</a> and the</p>",
        "<p>docs style guide: <a href='https://www.tensorflow.org/community/contribute/docs_style'>https://www.tensorflow.org/community/contribute/docs_style</a></p>",
        "<h3>System information</h3>",
        "<strong>System information</strong>",
        "<strong>Describe the feature and the current behavior/state.</strong>",
        "<strong>Will this change the current api? How?</strong>",
        "<strong>Who will benefit with this feature?</strong>",
        "<strong>Any Other info.</strong>",
        "<strong>Provide the text output from tflite_convert</strong>",
        "<strong>Standalone code to reproduce the issue</strong>",
        "<p>Provide a reproducible test case that is the bare minimum necessary to generate\nthe problem. If possible, please share a link to Colab/Jupyter/any notebook.</p>",
        "<p>Also, please include a link to a GraphDef or the model if possible.</p>",
        "<p>This template is for miscellaneous issues not covered by the other issue categories.</p>\n<p>For questions on how to work with TensorFlow, or support for problems that are not verified bugs in TensorFlow, please go to <a href='https://stackoverflow.com/questions/tagged/tensorflow'>StackOverflow</a>.</p>\n<p>If you are reporting a vulnerability, please use the <a href='https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md'>dedicated reporting process</a>.</p>\n<p>For high-level discussions about TensorFlow, please post to discuss@tensorflow.org, for questions about the development or internal workings of TensorFlow, or if you would like to know how to contribute to TensorFlow, please post to developers@tensorflow.org.</p>",
    ],
    "list_items": [
        "Have I written custom code (as opposed to using a stock example script provided in TensorFlow):",
        "OS Platform and Distribution (e.g., Linux Ubuntu 16.04):",
        "Mobile device (e.g. iPhone 8, Pixel 2, Samsung Galaxy) if the issue happens on mobile device:",
        "TensorFlow installed from (source or binary):",
        "TensorFlow version (use command below):",
        "Python version:",
        "Bazel version (if compiling from source):",
        "GCC/Compiler version (if compiling from source):",
        "CUDA/cuDNN version:",
        "GPU model and memory:",
        "TensorFlow version:",
        "TensorFlow version (you are using):",
        "Are you willing to contribute it (Yes/No):",
        "TensorFlow version (or github SHA if from source):",
    ]
}, {
    "repository": "vscode",
        "tags": [
            "<p>Steps to Reproduce:</p>",
            "<p>Does this issue occur when all extensions are disabled?: Yes/No</p>"
        ],
        "list_items": [
            "VSCode Version:",
            "OS Version:",
        ]
}
]


def issue_formatter(title, body, data):
    # Template Titles
    for tag in data['tags']:
        body = re.sub(tag, '', body)

    # Code chunks removal
    soup = BeautifulSoup(body, features="html.parser")
    for tag in soup.find_all('pre'):
        tag.replaceWith('')

    # <details>
    for tag in soup.find_all('details'):
        tag.replaceWith('')

    # System Details List
    for ul in soup.findAll('ul'):
        for li in ul.findAll('li'):
            for list_item in data['list_items']:
                if list_item in li.text:
                    li.replaceWith('')

    body = title + '\n' + soup.get_text()
    # Formatting
    body = re.sub('\n+', '\n', body)
    body = re.sub(' +', ' ', body)
    return body


if __name__ == "__main__":

    issues = pd.DataFrame()

    for repository in template:
        with open(repository['repository'] + '/' + repository['repository'] + '.json') as json_file:
            data = json.load(json_file)
        
        for element in data:
            row = {
                "source": repository['repository'],
                "author": element['repository']['issue']['author'],
                "number": element['repository']['issue']['number'],
                "resourcePath": element['repository']['issue']['resourcePath'],
                "state": element['repository']['issue']['state'],
                "publishedAt": element['repository']['issue']['publishedAt'],
                "closedAt": element['repository']['issue']['closedAt'],
                "text": issue_formatter(element['repository']['issue']['title'], element['repository']['issue']['bodyHTML'], repository)
            }

            issues = issues.append(row, ignore_index=True)

    issues.to_csv('issues.csv')