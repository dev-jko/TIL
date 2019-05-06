package reactive

import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observable = listOf(1, 2, 2, 3, 4, 6, 6, 6, 76, 8, 9, 5, 1, 2, 3).toObservable()

    observable.distinct().subscribe {
        println("Received $it")
    }
    println("****************************************")
    observable.distinctUntilChanged().subscribe {
        println("Received $it")
    }

}