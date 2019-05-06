package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observable = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).toObservable()
    observable.flatMap { number ->
        Observable.create<String> {
            it.onNext("The Number $number")
            it.onNext("number/2 ${number / 2}")
            it.onNext("number%2 ${number % 2}")
            it.onComplete()
        }
    }.subscribeBy(
            onNext = { item ->
                println("Received $item")
            },
            onComplete = {
                println("Complete")
            }
    )
}