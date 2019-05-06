package reactive

import io.reactivex.Flowable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val boundaryFlowable = Flowable.interval(350, TimeUnit.MILLISECONDS)
    val flowable = Flowable.interval(100, TimeUnit.MILLISECONDS)
//    flowable.buffer(1, TimeUnit.SECONDS).subscribe {
    flowable.buffer(boundaryFlowable).subscribe {
        println("Subscription 1: $it")
    }

    runBlocking { delay(5000) }

}