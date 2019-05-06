package reactive

import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    val observable = listOf(1, 2, 10, 3, 4, 5, 6).toObservable()
    observable.elementAt(1).subscribe { println(it) }
    observable.elementAt(5).subscribe { println(it) }
    observable.elementAt(50).subscribe { println(it) }
    observable.elementAt(1).subscribe { println(it) }
}