import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.spark.streaming._
import org.apache.spark.streaming.twitter._
import org.apache.spark.streaming.StreamingContext._
import TutorialHelper._

object Tutorial {
  def main(args: Array[String]) {

    // Location of the Spark directory
    val sparkHome = "$SPARK_HOME"

    // URL of the Spark cluster
    val sparkUrl = "local[22"

    // Location of the required JAR files
    val jarFile = "target/scala-2.10/team2app_2.10-0.1-SNAPSHOT.jar"

    // HDFS directory for checkpointing
    val checkpointDir = tutorial.getHdfsUrl() + "/checkpoint/"

    // Configure Twitter credentials using twitter.txt
    tutorial.configureTwitterCredentials()

    // Your code goes here
  }
}
