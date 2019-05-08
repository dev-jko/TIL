package reactive

import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val observable = Observable.interval(100, TimeUnit.MILLISECONDS)
    val observable2 = Observable.interval(250, TimeUnit.MILLISECONDS)

    Observable.zip(observable, observable2, BiFunction { t1: Long, t2: Long -> "t1 : $t1, t2: $t2" })
            .subscribe { println("1: Received $it") }

    runBlocking { delay(1100) }

    println("_*_*_*".repeat(10))

    Observable.combineLatest(observable, observable2, BiFunction { t1: Long, t2: Long -> "t1: $t1, t2: $t2" })
            .subscribe { println("2: Received $it") }

    runBlocking { delay(1100) }

}