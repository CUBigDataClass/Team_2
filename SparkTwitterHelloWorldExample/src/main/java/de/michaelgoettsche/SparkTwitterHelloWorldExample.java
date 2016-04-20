package de.michaelgoettsche;

import org.apache.spark.*;
import org.apache.spark.api.java.*;
import org.apache.spark.streaming.api.java.*;
import org.apache.spark.api.java.function.*;
import org.apache.spark.streaming.*;
import org.apache.spark.streaming.twitter.*;
import twitter4j.GeoLocation;
import twitter4j.Status;
import twitter4j.*;
import java.io.FileReader;
import java.util.Scanner;
import java.util.Properties;
import java.io.PrintStream;
import java.io.OutputStream;
import java.io.IOException;
import org.apache.log4j.Logger;
import org.apache.log4j.Level;
import java.util.Arrays;
import scala.Tuple2;
import scala.Tuple3;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.neural.rnn.RNNCoreAnnotations;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations;
import edu.stanford.nlp.trees.Tree;
import edu.stanford.nlp.util.CoreMap;


public class SparkTwitterHelloWorldExample {
	public static int findSentiment(String line) {
		int mainSentiment = 0; 
		PrintStream err = System.err;
		System.setErr(new PrintStream(new OutputStream() {
    			public void write(int b) {
    			}
		}));	
		//set up properties
		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, parse, sentiment");
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
		//estimate the mood score of each tweet
		if (line != null && line.length() > 0) {
                int longest = 0;
          	Annotation annotation = pipeline.process(line);
		for (CoreMap sentence : annotation.get(CoreAnnotations.SentencesAnnotation.class)) {
			Tree tree = sentence.get(SentimentCoreAnnotations.AnnotatedTree.class);
		        int sentiment = RNNCoreAnnotations.getPredictedClass(tree);
		        String partText = sentence.toString();
		        if (partText.length() > longest) {
		        	mainSentiment = sentiment;
		                longest = partText.length();
		        }
		}
	}
System.setErr(err);         
return mainSentiment;

}
    public static void main(String[] args) {
        try{
            Scanner in = new Scanner(new FileReader("/home/ec2-user/tokens.txt"));
            final String consumerKey = in.next();
            final String consumerSecret = in.next();
            final String accessToken = in.next();
            final String accessTokenSecret = in.next();

        SparkConf conf = new SparkConf().setMaster("local[2]").setAppName("SparkTwitterHelloWorldExample");
        JavaStreamingContext jssc = new JavaStreamingContext(conf, new Duration(10000));
	jssc.checkpoint("hdfs://ec2-52-34-173-2.us-west-2.compute.amazonaws.com:9000/checkpoint");	
	Logger.getLogger("org").setLevel(Level.OFF);
	Logger.getLogger("akka").setLevel(Level.OFF);
        
	System.setProperty("twitter4j.oauth.consumerKey", consumerKey);
        System.setProperty("twitter4j.oauth.consumerSecret", consumerSecret);
        System.setProperty("twitter4j.oauth.accessToken", accessToken);
        System.setProperty("twitter4j.oauth.accessTokenSecret", accessTokenSecret);

	String[] filters={"hillary", "bernie", "hillaryclinton", "elections", "berniesanders", "vote", "election2016" , "democrats",  "tedcruz", "democrat", "republican", "donaldtrump", "trump", "cruz", "tedcruz"
};
        JavaReceiverInputDStream<Status> twitterStream = TwitterUtils.createStream(jssc, filters);

        // Without filter: Output text of all tweets
        JavaDStream<String> statuses = twitterStream.map(
                new Function<Status, String>() {
			public String call(Status status) { return status.getText(); }
                }
        );
	JavaDStream<String> words = statuses.flatMap(
		new FlatMapFunction<String, String>(){
			public Iterable<String> call(String in) {
				return Arrays.asList(in.split(" "));
			}
		}
	);
	/*
	JavaDStream<String> hashTags = words.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) { return  word.startsWith("#");}
		}
	);
	*/
	JavaDStream<String> trumptweets = statuses.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) {return word.toLowerCase().contains("trump") & !word.toLowerCase().contains("hillary") & !word.toLowerCase().contains("bernie") & !word.toLowerCase().contains("cruz");}
		}
	  );
	JavaPairDStream<String, Integer> trumptuples = trumptweets.mapToPair(
		new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("trump", findSentiment(in));
			}
		}
	);
	JavaPairDStream<String, Integer> trumpcounts = trumptuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);

		JavaDStream<String> hillarytweets = statuses.filter(
			new Function<String, Boolean>() {
				public Boolean call(String word) {return !word.toLowerCase().contains("trump") & (word.toLowerCase().contains("hillary") || word.toLowerCase().contains("clinton")) & !word.toLowerCase().contains("bernie") & !word.toLowerCase().contains("cruz");}
		}
	  );	
		JavaPairDStream<String, Integer> hillarytuples = hillarytweets.mapToPair(
			new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("hillary", findSentiment(in));
			}
		}
	);
	JavaPairDStream<String, Integer> hillarycounts = hillarytuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);
		JavaDStream<String> bernietweets = statuses.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) {return !word.toLowerCase().contains("trump") & !word.toLowerCase().contains("hillary") & (word.toLowerCase().contains("bernie") || word.toLowerCase().contains("sanders")) & !word.toLowerCase().contains("cruz");}
		}
	  );	JavaPairDStream<String, Integer> bernietuples = bernietweets.mapToPair(
		new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("bernie", findSentiment(in));
			}
		}
	);
	JavaPairDStream<String, Integer> berniecounts = bernietuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);
			JavaDStream<String> cruztweets = statuses.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) {return !word.toLowerCase().contains("trump") & !word.toLowerCase().contains("hillary") & !word.toLowerCase().contains("bernie") & word.toLowerCase().contains("cruz");}
		}
	  );	JavaPairDStream<String, Integer> cruztuples = cruztweets.mapToPair(
		new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("cruz", findSentiment(in));
			}
		}
	);
		
	JavaPairDStream<String, Integer> cruzcounts = cruztuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);
		
	JavaDStream<String> demtweets =  statuses.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) {return word.toLowerCase().contains("democrat") & !word.toLowerCase().contains("republican");}
		}
	  );
	JavaPairDStream<String, Integer> demtuples = demtweets.mapToPair(
		new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("dems", findSentiment(in));
			}
		}
	);

	JavaPairDStream<String, Integer> demcounts = demtuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);
	JavaDStream<String> goptweets =  statuses.filter(
		new Function<String, Boolean>() {
			public Boolean call(String word) {return !word.toLowerCase().contains("democrat") & word.toLowerCase().contains("republican") & word.toLowerCase().contains("gop");}
		}
	  );
		JavaPairDStream<String, Integer> goptuples = goptweets.mapToPair(
		new PairFunction<String, String, Integer>(){
			public Tuple2<String, Integer> call(String in) {
				return new Tuple2<String, Integer>("gop", findSentiment(in));
			}
		}
	);
		JavaPairDStream<String, Integer> gopcounts = goptuples.reduceByKey(
      		new Function2<Integer, Integer, Integer>() {
        		public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      }
);		
	/*
	String wordSentimentFilePath = "AFINN/AFINN-111.txt";
	final JavaPairRDD<String, Double> wordSentiments = jssc.sparkContext().textFile(wordSentimentFilePath).mapToPair(new PairFunction<String, String, Double>(){
		public Tuple2<String, Double> call(String line) {
			String[] columns = line.split("\t");
			return new Tuple2<String, Double>(columns[0], Double.parseDouble(columns[1]));
}});
	JavaPairDStream<String, Integer> tuples = hashTags.mapToPair(
      		new PairFunction<String, String, Integer>() {
        		public Tuple2<String, Integer> call(String in) {
          			return new Tuple2<String, Integer>(in, 1);
        }
      }
    );

    JavaPairDStream<String, Integer> counts = tuples.reduceByKeyAndWindow(
      new Function2<Integer, Integer, Integer>() {
        public Integer call(Integer i1, Integer i2) { return i1 + i2; }
      },
      new Function2<Integer, Integer, Integer>() {
        public Integer call(Integer i1, Integer i2) { return i1 - i2; }
      },
      new Duration(60 * 5 * 10000),
      new Duration(1 * 10000)
    );
	
        // With filter: Only use tweets with geolocation and print location+text.
        /*JavaDStream<Status> tweetsWithLocation = twitterStream.filter(
                new Function<Status, Boolean>() {
                    public Boolean call(Status status){
                        if (status.getGeoLocation() != null) {
                            return true;
                        } else {
                            return false;
                        }
                    }
                }
        );

        JavaDStream<String> statuses = tweetsWithLocation.map(
                new Function<Status, String>() {
                    public String call(Status status) {
                        return status.getGeoLocation().toString() + ": " + status.getText();
                    }
                }
        );
*/
	trumpcounts.print();
        hillarycounts.print();
	berniecounts.print();
	cruzcounts.print();
	gopcounts.print();
	demcounts.print();
	jssc.start();
	} 
	catch(IOException e){
		System.out.println("auth problem");
    	}
}
}
