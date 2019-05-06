package reactive

import io.reactivex.BackpressureStrategy
import io.reactivex.Observable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

fun main(args: Array<String>) {
    val source = Observable.range(1, 500)
    source.toFlowable(BackpressureStrategy.DROP).map { MyItem(it) }.observeOn(Schedulers.io())
            .subscribe {
                println("Rec. $it")
                runBlocking { delay(50) }
            }
    runBlocking { delay(20000) }
}