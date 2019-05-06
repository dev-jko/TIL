package reactive

import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    listOf(1, 4, 7, 8, 4, 5, 6, 8, 2, 4, 1).toObservable()
            .sorted()
            .subscribe { println(it) }

    println("*-".repeat(10))

    listOf("alpha", "gamma", "beta", "theta").toObservable()
            .sorted()
            .subscribe { println(it) }

    println("*-".repeat(10))

    listOf(1, 67, 8, 2, 23, 5, 6, 21, 4, 7, 8, 9).toObservable()
            .sorted { item1, item2 -> if (item1 > item2) -1 else 1 }
            .subscribe { println(it) }

    println("*-".repeat(10))
}