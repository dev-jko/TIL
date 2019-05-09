package reactive

import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val observable = Observable.range(1, 20)
    observable.take(5)
            .subscribe(object : Observer<Int> {
                override fun onComplete() {
                    println("Complete")
                }

                override fun onSubscribe(d: Disposable) {
                    println("starting take(5)")
                }

                override fun onNext(t: Int) {
                    println("Received $t")
                }

                override fun onError(e: Throwable) {
                    e.printStackTrace()
                }
            })

    val observable2 = Observable.interval(100, TimeUnit.MILLISECONDS)
    observable2.take(400, TimeUnit.MILLISECONDS)
            .subscribe(object : Observer<Long> {
                override fun onComplete() {
                    println("Complete")
                }

                override fun onSubscribe(d: Disposable) {
                    println("starting ")
                }

                override fun onNext(t: Long) {
                    println("Received $t")
                }

                override fun onError(e: Throwable) {
                    e.printStackTrace()
                }
            })

    runBlocking { delay(1000) }
}