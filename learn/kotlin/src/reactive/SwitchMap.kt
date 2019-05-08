package reactive

import io.reactivex.Observable
import java.util.*
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    println("Without delay")
    Observable.range(1, 10)
            .switchMap {
                val randDelay = Random().nextInt(10)
                return@switchMap Observable.just(it)
            }.blockingSubscribe { println("Received $it") }

    println("With delay")

    Observable.range(1, 10)
            .switchMap {
                val randDelay = Random().nextInt(10)
                return@switchMap Observable.just(it)
                        .delay(randDelay.toLong(), TimeUnit.MILLISECONDS)
            }.blockingSubscribe { println("Received $it") }
}