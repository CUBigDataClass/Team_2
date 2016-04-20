import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object helloscala {
	def main(args: Array[String]) {
		val conf = new SparkConf().setAppName("helloscala")
		val sc = new SparkContext(conf)
		println("Hello, World")
		sc.stop()
		}
	}
