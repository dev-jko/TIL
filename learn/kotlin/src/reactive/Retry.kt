package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    Observable.just(1, 2, 3, 4, 5)
            .map { it / (3 - it) }
            .retry(3)
            .subscribeBy(
                    onNext = { println(it) },
                    onError = { println("Error") }
            )

    println(" Whit Predicate")

    var retryCount = 0
    Observable.just(1, 2, 3, 4, 5)
            .map { it / (3 - it) }
            .retry { _, _ ->
                (++retryCount) < 3
            }
            .subscribeBy(
                    onNext = { println("Received $it") },
                    onError = { println("Error") }
            )
}