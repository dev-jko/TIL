package reactive

import io.reactivex.Observable

fun main(args: Array<String>) {
    Observable.range(1, 10)
            .map { it / (3 - it) }
            .onErrorResumeNext(Observable.range(15, 5))
            .subscribe { println("Received $it") }
}