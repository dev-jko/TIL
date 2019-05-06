package reactive

import io.reactivex.Observable
import io.reactivex.rxkotlin.subscribeBy

fun main(args: Array<String>) {
    Observable.range(1, 10)
            .reduce { previousAccumulation, newEmission ->
                previousAccumulation + newEmission
            }
            .subscribeBy { println("accumulation : $it") }

    Observable.range(1, 5)
            .reduce { acc, new ->
                acc * 10 + new
            }
            .subscribeBy { println("acc : $it") }
}