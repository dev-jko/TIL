package reactive

import io.reactivex.Observable
import io.reactivex.Scheduler
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

import java.util.concurrent.Executors

fun main() {
    val executor = Executors.newFixedThreadPool(2)
    val scheduler: Scheduler = Schedulers.from(executor)

    Observable.range(1, 10)
            .subscribeOn(scheduler)
            .subscribe {
                runBlocking { delay(200) }
                println("Observable 1 Item Received $it - ${Thread.currentThread().name}")
            }

    Observable.range(21, 10)
            .subscribeOn(scheduler)
            .subscribe {
                runBlocking { delay(100) }
                println("Observable 2 Item Received $it - ${Thread.currentThread().name}")
            }

    Observable.range(51, 10)
            .subscribeOn(scheduler)
            .subscribe {
                runBlocking { delay(100) }
                println("Observable 2 Item Received $it - ${Thread.currentThread().name}")
            }

    runBlocking { delay(10000) }
}