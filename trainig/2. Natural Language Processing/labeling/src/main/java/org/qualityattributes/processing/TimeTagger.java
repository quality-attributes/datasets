package org.qualityattributes.processing;

import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.time.*;

import com.google.common.io.Files;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Properties;

/**
 * @author Manolomon
 * @version 1.0
 */
public class TimeTagger {

    public static String[] examples = {
            "The concert will be on February 4th at the ampitheater.",
            "The meeting will be held at 4:00pm in the library",
            "The conflict has lasted for over 15 years and shows no signs of abating.",
            "The system shall be available for use between the hours of 8am and 6pm"
    };


    public static void main(String[] args) {
        // set up pipeline properties
        Properties props = new Properties();
        // general properties
        props.setProperty("annotators", "tokenize, ssplit,pos,lemma,ner");
        props.setProperty("ner.docdate.usePresent", "true");
        props.setProperty("sutime.includeRange", "true");
        props.setProperty("sutime.markTimeRanges", "true");

        // read some text from the file..
        File inputFile = new File("../../1. Text Cleaning/nfr-text.txt");
        File outputFile = new File("../temporaltags.csv");
        String rawText = null;
        try {
            rawText = Files.toString(inputFile, Charset.forName("UTF-8"));
            if(outputFile.exists()) {
                outputFile.delete();
            }
            outputFile.createNewFile();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] text = rawText.split("\n");

        // build pipeline
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // Write headers
        try {
            Files.append("line,tag\n", outputFile, Charset.forName("UTF-8"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // For each sentence
        Timex tempTag;
        String tagParsed;
        for (int i = 0; i < text.length; i++) {
            CoreDocument document = new CoreDocument(text[i]);
            pipeline.annotate(document);
            for (CoreEntityMention cem : document.entityMentions()) {
                tempTag = cem.coreMap().get(TimeAnnotations.TimexAnnotation.class);
                tagParsed = null;
                if (tempTag != null) {
                    // replace all " to match csv format
                    tagParsed = tempTag.toString().replaceAll("\"","\"\"");
                }

                try {
                    Files.append(i + ",\"" + tagParsed + "\"\n", outputFile, Charset.forName("UTF-8"));
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }


}