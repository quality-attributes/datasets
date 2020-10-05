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

public class POSTagger {

    public static void main(String[] args) {
        // set up pipeline properties
        Properties props = new Properties();
        // general properties
        props.setProperty("annotators", "tokenize, ssplit, pos");

        // read some text from the file..
        File inputFile = new File("../../ner_normalized.txt");
        File posOutputFile = new File("../parsed-req-pos.conll");

        String rawText = null;
        try {
            rawText = Files.toString(inputFile, Charset.forName("UTF-8"));
            if(posOutputFile.exists()) {
                posOutputFile.delete();
            }
            posOutputFile.createNewFile();
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
                // this is the POS tag of the token
                String pos = token.get(CoreAnnotations.PartOfSpeechAnnotation.class);

                System.out.println("word: " + word + " pos: " + pos);

                try {
                    if (pos.equals("NN") || pos.equals("NNS") || pos.equals("NNP") || pos.equals("NNPS")) { //
                        Files.append(word + "   " + pos + "\n", posOutputFile, Charset.forName("UTF-8"));
                    } else {
                        Files.append(word + "\n", posOutputFile, Charset.forName("UTF-8"));
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            try {
                Files.append("\n", posOutputFile, Charset.forName("UTF-8"));
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
