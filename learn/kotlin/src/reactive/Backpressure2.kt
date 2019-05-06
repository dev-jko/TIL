import io.reactivex.BackpressureStrategy
import io.reactivex.Observable
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import reactive.MyItem

fun main(args: Array<String>) {
    val source = Observable.range(1, 500)
    source.toFlowable(BackpressureStrategy.MISSING).onBackpressureBuffer(20).map { MyItem(it) }
            .observeOn(Schedulers.io()).subscribe({
                println(it)
                runBlocking { delay(20) }
            }, {
                println("Error : ${it.message}")
                it.printStackTrace()
            })
    runBlocking { delay(30000) }
}