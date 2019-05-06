package reactive

import io.reactivex.Observable

fun main(args: Array<String>) {
    Observable.range(1, 10)
            .filter { it % 2 == 0 }
            .subscribe { println(it) }
}