package reactive

import io.reactivex.Observable

fun main() {
    Observable.range(1, 10)
            .compose<List<Int>> { upstream: Observable<Int> ->
                upstream.toList().toObservable()
            }.subscribe { println("Next - $it") }
}