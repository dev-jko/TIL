package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observable = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).toObservable()
    observable.flatMap { Observable.just("Transforming Int to String $it") }
            .subscribe { println("Received $it") }
}