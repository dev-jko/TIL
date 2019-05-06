package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    val observable = Observable.range(1, 10)
    observable.first(2).subscribeBy { println(it) }
    observable.last(2).subscribeBy { println(it) }
    Observable.empty<Int>().first(2).subscribeBy { println(it) }
}