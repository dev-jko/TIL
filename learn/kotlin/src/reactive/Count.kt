package reactive

import io.reactivex.rxkotlin.subscribeBy
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    listOf(1, 2, 3, 4, 5, 6, 2, 34).toObservable()
            .count()
            .subscribeBy { println("count : $it") }
}