package reactive

import io.reactivex.Observable

fun main(args: Array<String>) {
    val observable = Observable.range(1, 30)

    observable.groupBy { it % 5 }
            .blockingSubscribe {
                println("key ${it.key}")
                it.subscribe { println("Received $it") }
            }
}