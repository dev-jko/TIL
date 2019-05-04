import kotlinx.coroutines.*
import kotlin.system.measureTimeMillis

suspend fun longRunningTsk(): Long {
    return measureTimeMillis {
        println("Please wait")
        delay(2000)
        println("Delay Over")
    }
}

fun main(args: Array<String>) {
    val time = CoroutineScope(Dispatchers.Default).async { longRunningTsk() }
//    val time = async { longRunningTsk() }
    println("Print after async")
    runBlocking { println("Execution Time is ${time.await()}") }
}