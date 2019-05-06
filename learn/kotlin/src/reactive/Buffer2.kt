package reactive

import io.reactivex.Flowable

fun main(args: Array<String>) {
    val flowable = Flowable.range(1, 111)
    flowable.buffer(10, 15).subscribe {
        println("Subscription 1: $it")
    }
    flowable.buffer(15, 7).subscribe {
        println("Subscription 2: $it")
    }
    flowable.buffer(15, 10).subscribe {
        println("Subscription 3: $it")
    }
}