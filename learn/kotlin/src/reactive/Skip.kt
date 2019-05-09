package reactive

import io.reactivex.Observable
import io.reactivex.Observer
import io.reactivex.disposables.Disposable
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import java.util.concurrent.TimeUnit

fun main(args: Array<String>) {
    val observable = Observable.range(1, 20)
    observable.skip(5)
            .subscribe(object : Observer<Int> {
                override fun onComplete() {
                    println("Completed")
                }

                override fun onSubscribe(d: Disposable) {
                    println("Subscribe, starting skip(count)")
                }

                override fun onNext(t: Int) {
                    println("Received $t")
                }

                override fun onError(e: Throwable) {
                    e.printStackTrace()
                }
            })

    val observable2 = Observable.interval(100, TimeUnit.MILLISECONDS)
    observable2.skip(400, TimeUnit.MILLISECONDS)
            .subscribe(object : Observer<Long> {
                override fun onComplete() {
                    println("observable2 Completed")
                }

                override fun onSubscribe(d: Disposable) {
                    println("starting skip(time)")
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