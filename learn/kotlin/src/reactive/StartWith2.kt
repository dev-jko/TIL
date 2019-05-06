package reactive

import io.reactivex.Observable

fun main(args: Array<String>) {
    Observable.range(5, 10)
            .startWith(listOf(1, 2, 3, 4))
            .subscribe { println("Received $it") }

    Observable.range(5, 10)
            .startWith(Observable.just(1, 2, 3, 4))
            .subscribe { println("Received $it") }
}