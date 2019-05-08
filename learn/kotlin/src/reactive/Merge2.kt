package reactive

import io.reactivex.Observable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit
import java.util.function.BiFunction

fun main(args: Array<String>) {
    val observable1 = Observable.interval(500, TimeUnit.MILLISECONDS).map { "Observable1 $it" }
    val observable2 = Observable.interval(100, TimeUnit.MILLISECONDS).map { "Observable2 $it" }

    Observable.merge(observable1, observable2)
            .subscribe { println(it) }

    runBlocking { delay(1500) }
}