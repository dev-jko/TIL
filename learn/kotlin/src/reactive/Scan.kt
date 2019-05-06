package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.toObservable

fun main(args: Array<String>) {
    Observable.range(1, 10)
            .scan { previousAccumlation, newEmission ->
                previousAccumlation + newEmission
            }
            .subscribe { println(it) }

    listOf("String 1", "String 2", "String 3", "String 4").toObservable()
            .scan { previousAccumulation, newEmission ->
                "$previousAccumulation $newEmission"
            }
            .subscribe { println(it) }

    Observable.range(1, 5)
            .scan { previousAccumulation, newEmission ->
                previousAccumulation * 10 + newEmission
            }
            .subscribe { println(it) }
}