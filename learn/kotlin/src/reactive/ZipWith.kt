package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.toObservable
import io.reactivex.rxkotlin.zipWith

fun main(args: Array<String>) {
    val observable1 = Observable.range(1, 10)
    val observable2 = listOf("String 1", "String 2", "String 3", "String 4").toObservable()

    observable1.zipWith(observable2) { e1, e2 -> "$e1, $e2" }
            .subscribe { println(it) }


}