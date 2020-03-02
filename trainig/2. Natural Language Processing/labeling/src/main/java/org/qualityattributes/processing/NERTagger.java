package org.qualityattributes.processing;

import com.google.common.io.Files;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.CoreEntityMention;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.time.TimeAnnotations;
import edu.stanford.nlp.time.Timex;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Properties;

public class NERTagger {

    public static void main(String[] args) {
        // set up pipeline properties
        Properties props = new Properties();
        // general properties
        props.setProperty("annotators", "tokenize,ssplit,pos,lemma,ner");
        props.setProperty("file", "../parsed-req.txt");
        props.setProperty("outputFormat" ,"conll");
        props.setProperty("output.columns", "ner");

        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
    }
}
