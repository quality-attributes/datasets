package org.qualityattributes.processing;

import com.google.common.io.Files;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Properties;

public class NERTagger {

    public static void main(String[] args) {
        // set up pipeline properties
        Properties props = new Properties();
        // general properties
        props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner");

        // read some text from the file..
        File inputFile = new File("../../normalized.txt");
        File nerOutputFile = new File("../parsed-req-ner.conll");
        String rawText = null;
        try {
            rawText = Files.toString(inputFile, Charset.forName("UTF-8"));

            if(nerOutputFile.exists()) {
                nerOutputFile.delete();
            }
            nerOutputFile.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] text = rawText.split("\n");

        // build pipeline
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // For each sentence
        String tagParsed;
        for (int i = 0; i < text.length; i++) {
            CoreDocument document = new CoreDocument(text[i]);
            pipeline.annotate(document);
            for (CoreLabel token: document.annotation().get(CoreAnnotations.TokensAnnotation.class)) {
                // this is the text of the token
                String word = token.get(CoreAnnotations.TextAnnotation.class);
                // this is the NER label of the token
                String ner = token.get(CoreAnnotations.NamedEntityTagAnnotation.class);

                System.out.println("word: " + word + " ner:" + ner );

                try {
                    if (!ner.equals("O")) { //
                        Files.append(word + "   " + ner + "\n", nerOutputFile, Charset.forName("UTF-8"));
                    } else {
                        Files.append(word + "\n", nerOutputFile, Charset.forName("UTF-8"));
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            try {
                Files.append("\n", nerOutputFile, Charset.forName("UTF-8"));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

