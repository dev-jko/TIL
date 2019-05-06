package reactive

import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import io.reactivex.functions.Function3

fun main(args: Array<String>) {
    val observable1 = Observable.range(1, 10)
    val observable2 = Observable.range(11, 10)
    Observable.zip(observable1, observable2, BiFunction<Int, Int, Int> { emission1, emission2 ->
        emission1 + emission2
    }).subscribe { println("Received $it") }

    val observable3 = Observable.range(1, 10)
    Observable.zip(observable1, observable2, observable3, Function3<Int, Int, Int, Int> { t1, t2, t3 -> t1 + t2 + t3 })
            .subscribe { println(it) }
}