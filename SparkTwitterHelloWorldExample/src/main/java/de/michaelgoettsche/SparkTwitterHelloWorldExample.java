package de.michaelgoettsche;

import org.apache.spark.*;
import org.apache.spark.api.java.function.*;
import org.apache.spark.streaming.*;
import org.apache.spark.streaming.api.java.*;
import org.apache.spark.streaming.twitter.*;
import twitter4j.GeoLocation;
import twitter4j.Status;
import java.io.FileReader;
import java.util.Scanner;
import java.io.IOException;
import org.apache.log4j.Logger;
import org.apache.log4j.Level;

public class SparkTwitterHelloWorldExample {
    public static void main(String[] args) {
        try{
            Scanner in = new Scanner(new FileReader("/home/ec2-user/tokens.txt"));
            final String consumerKey = in.next();
            final String consumerSecret = in.next();
            final String accessToken = in.next();
            final String accessTokenSecret = in.next();

        SparkConf conf = new SparkConf().setMaster("local[2]").setAppName("SparkTwitterHelloWorldExample");
        JavaStreamingContext jssc = new JavaStreamingContext(conf, new Duration(1000));
	
	Logger.getLogger("org").setLevel(Level.OFF);
	Logger.getLogger("akka").setLevel(Level.OFF);
        
	System.setProperty("twitter4j.oauth.consumerKey", consumerKey);
        System.setProperty("twitter4j.oauth.consumerSecret", consumerSecret);
        System.setProperty("twitter4j.oauth.accessToken", accessToken);
        System.setProperty("twitter4j.oauth.accessTokenSecret", accessTokenSecret);

        JavaReceiverInputDStream<Status> twitterStream = TwitterUtils.createStream(jssc);

        // Without filter: Output text of all tweets
        /*JavaDStream<String> statuses = twitterStream.map(
                new Function<Status, String>() {
                    public String call(Status status) { return status.getText(); }
                }
        );
	*/
        // With filter: Only use tweets with geolocation and print location+text.
        JavaDStream<Status> tweetsWithLocation = twitterStream.filter(
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

        statuses.print();
        jssc.start();
	} 
	catch(IOException e){
		System.out.println("auth problem");
    	}
}
}
