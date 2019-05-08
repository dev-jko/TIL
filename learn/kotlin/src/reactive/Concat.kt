package reactive

import io.reactivex.Observable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val observable1 = Observable.interval(500, TimeUnit.MILLISECONDS).take(2)
            .map { "Observable1 $it" }
    val observable2 = Observable.interval(100, TimeUnit.MILLISECONDS)
            .map { "Observable2 $it" }

    Observable.concat(observable1, observable2)
            .subscribe { println("Received $it") }

    runBlocking { delay(1500) }
}