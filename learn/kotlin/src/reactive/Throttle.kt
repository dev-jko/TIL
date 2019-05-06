package reactive

import io.reactivex.Flowable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val flowable = Flowable.interval(100, TimeUnit.MILLISECONDS)
    flowable.throttleFirst(200, TimeUnit.MILLISECONDS).subscribe {
        println(it)
    }
    runBlocking { delay(1000) }
}